#!/bin/bash
# collect-x-intel.sh — Search X → Filter → Store pipeline for IVCO
# Version: 2.1.0 (2026-02-11)
#
# Pipeline: bird search → ivco-filter (score+discard) → ivco-collect (POST to CMS)
# Runs via launchd: 07:00, 13:00, 20:00 (Asia/Taipei)
#
# Changelog:
#   v1.0.0 (2026-02-08) — Initial: bird → ivco-collect (raw, no filtering)
#   v2.0.0 (2026-02-10) — Added ivco-filter between bird and ivco-collect
#                          Garbage tweets (promo, spam, short) now auto-discarded
#   v2.1.0 (2026-02-11) — Fix: pass --auth-token/--ct0 explicitly to bird
#                          (bird has no env var support, was silently falling back to Chrome cookies)
#                          Consolidate credentials to ~/.config/env/bird.env (chmod 600)
#
# Rollback:
#   cp ~/AI-Workspace/memory/backups/collect-x-intel.sh.bak.20260211 \
#      ~/AI-Workspace/projects/allen-ivco/scripts/collect-x-intel.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="/Users/allenchenmac/AI-Workspace/memory/daily"
LOG_FILE="${LOG_DIR}/x-intel-collect.log"
TMP_DIR="/tmp/ivco-collect"
PAYLOAD_API="http://localhost:3000/api/company-events"
PAYPAL_COMPANY_ID=2
MAX_RESULTS=3

# Direct paths (no nvm loading needed)
BIRD="/Users/allenchenmac/.nvm/versions/node/v22.22.0/bin/bird"
PYTHON="/usr/local/bin/python3"
IVCO_FILTER="/Library/Frameworks/Python.framework/Versions/3.11/bin/ivco-filter"
FILTER_CONFIG="${SCRIPT_DIR}/../cli/ivco-filter/config/filter-rules.json"

mkdir -p "$TMP_DIR" "$LOG_DIR"

# Load bird credentials from secure location (chmod 600)
BIRD_ENV="$HOME/.config/env/bird.env"
if [ -f "$BIRD_ENV" ]; then
  BIRD_AUTH_TOKEN=$(grep '^BIRD_AUTH_TOKEN=' "$BIRD_ENV" | cut -d= -f2)
  BIRD_CT0=$(grep '^BIRD_CT0=' "$BIRD_ENV" | cut -d= -f2)
else
  echo "[$(date -Iseconds)] ERROR: bird.env not found at $BIRD_ENV" >> "$LOG_FILE"
  exit 1
fi

if [ -z "$BIRD_AUTH_TOKEN" ] || [ -z "$BIRD_CT0" ]; then
  echo "[$(date -Iseconds)] ERROR: BIRD_AUTH_TOKEN or BIRD_CT0 is empty in $BIRD_ENV" >> "$LOG_FILE"
  exit 1
fi

# Verify ivco-filter is available
if [ ! -x "$IVCO_FILTER" ]; then
  echo "[$(date -Iseconds)] ERROR: ivco-filter not found at $IVCO_FILTER" >> "$LOG_FILE"
  exit 1
fi

log() {
  echo "[$(date -Iseconds)] $1" >> "$LOG_FILE"
}

log "=== Collection run started (v2.1.0) ==="
total_raw=0
total_filtered=0
total_stored=0

for keyword in "paypal" "PYPL"; do
  log "Searching: ${keyword}"

  # Step 1: Bird search → raw JSON (explicit auth, no Chrome cookies dependency)
  "$BIRD" search "$keyword" -n "$MAX_RESULTS" --json \
    --auth-token "$BIRD_AUTH_TOKEN" --ct0 "$BIRD_CT0" \
    > "$TMP_DIR/raw.json" 2>/dev/null || echo "[]" > "$TMP_DIR/raw.json"

  raw_count=$("$PYTHON" -c "import json; print(len(json.load(open('$TMP_DIR/raw.json'))))" 2>/dev/null || echo "0")
  log "  Raw tweets: ${raw_count}"
  total_raw=$((total_raw + raw_count))

  # Step 2: ivco-filter → scored + filtered JSON (verbose logs to stderr → log file)
  "$IVCO_FILTER" \
    --config "$FILTER_CONFIG" \
    --input "$TMP_DIR/raw.json" \
    --output "$TMP_DIR/filtered.json" \
    --verbose 2>> "$LOG_FILE" || {
    log "  WARNING: ivco-filter failed, falling back to raw tweets"
    cp "$TMP_DIR/raw.json" "$TMP_DIR/filtered.json"
  }

  filtered_count=$("$PYTHON" -c "import json; print(len(json.load(open('$TMP_DIR/filtered.json'))))" 2>/dev/null || echo "0")
  discarded=$((raw_count - filtered_count))
  log "  After filter: ${filtered_count} kept, ${discarded} discarded"
  total_filtered=$((total_filtered + filtered_count))

  # Step 3: ivco-collect → POST filtered tweets to Payload CMS
  stored=$("$PYTHON" "$SCRIPT_DIR/ivco-collect" \
    --input "$TMP_DIR/filtered.json" \
    --api "$PAYLOAD_API" \
    --company-id "$PAYPAL_COMPANY_ID" \
    --keyword "$keyword" 2>> "$LOG_FILE")

  log "  Stored: ${stored} tweets"
  total_stored=$((total_stored + stored))
done

rm -f "$TMP_DIR/raw.json" "$TMP_DIR/filtered.json"
log "=== Collection complete: ${total_raw} raw → ${total_filtered} filtered → ${total_stored} stored ==="
