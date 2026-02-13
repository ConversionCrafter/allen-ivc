"""Load and validate filter rules from JSON config."""

import json
import os
import sys

DEFAULT_CONFIG = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "config",
    "filter-rules.json",
)


def load_rules(config_path: str | None = None) -> dict:
    """Load filter rules from JSON file. Falls back to default config."""
    path = config_path or DEFAULT_CONFIG
    try:
        with open(path, "r") as f:
            rules = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Config not found: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(1)

    validate_rules(rules)
    return rules


def validate_rules(rules: dict) -> None:
    """Basic validation of rules structure."""
    required = ["garbage_rules", "useful_rules", "score_threshold"]
    for key in required:
        if key not in rules:
            print(f"ERROR: Missing required key '{key}' in config", file=sys.stderr)
            sys.exit(1)


def save_rules(rules: dict, config_path: str | None = None) -> None:
    """Save rules back to JSON file (for blacklist/whitelist updates)."""
    path = config_path or DEFAULT_CONFIG
    with open(path, "w") as f:
        json.dump(rules, f, indent=2, ensure_ascii=False)
        f.write("\n")
