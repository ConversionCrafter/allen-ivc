# Dual-Agent Collaboration Setup: Claude Code (Jane) + OpenAI Codex

> **Version**: 1.0.0
> **Created**: 2026-02-11
> **Author**: Allen + Jane (Claude Code) + Codex
> **Status**: Active — Verified & Operational

---

## 1. Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                     Allen (Decision Maker)                       │
│                                                                  │
│  "我不要當 copy/paste 的傳令兵"                                   │
│  "資訊要同步，但 write/edit 權限只能一人主控"                       │
└──────────────────────┬───────────────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
┌───────────────────┐     ┌───────────────────────────┐
│  Jane (Claude Code)│◄───►│  Codex (OpenAI)            │
│  ═══════════════  │     │  ═══════════════════════  │
│  Role: Orchestrator│     │  Role: Execution Agent     │
│  Authority: WRITE │     │  Authority: READ + Propose │
│  Model: Opus 4.6  │     │  Model: ChatGPT 5.2       │
│  Git: Full access │     │  Git: Via Jane only        │
└───────────────────┘     └───────────────────────────┘
        │                             │
        │    ┌────────────────────┐   │
        └───►│  GitHub Repos      │◄──┘
             │  (Shared State)    │
             │  ────────────────  │
             │  allen-ivco (code) │
             │  obsidian (knowledge)│
             └────────────────────┘
```

### Core Principle: Single Writer Authority

| Aspect | Jane (Claude Code) | Codex (OpenAI) |
|--------|-------------------|----------------|
| **Read** | Full access — local filesystem + all repos | Full access — via MCP `read-only` or `workspace-write` |
| **Write/Edit** | **PRIMARY AUTHORITY** — all files, all repos | **Propose only** — writes go through Jane's review |
| **Git commit** | Full access — commit + push | NO direct git access |
| **Git push** | Full access — push to all remotes | NO direct push |
| **PR creation** | Full access — `gh pr create` | NO — Codex `make_pr` is metadata only |
| **Knowledge system** | Full CRUD — notes, AGs, tasks, signals | **READ ONLY** — Obsidian, rules, SCRATCHPAD |
| **IVCO code** | Full CRUD | Can write locally (workspace-write), Jane reviews + commits |

---

## 2. Communication Channels

### Channel A: Codex MCP (Primary — Direct Bidirectional)

**This is the working channel.** Jane calls Codex directly through MCP, no human intermediary.

```
Jane ──► mcp__codex__codex (prompt, sandbox, cwd) ──► Codex executes ──► Returns result
Jane ──► mcp__codex__codex-reply (threadId, prompt) ──► Continue conversation
```

**Configuration** (already registered):
```bash
claude mcp add codex --scope user -- codex mcp-server
```

**Sandbox modes**:
| Mode | Use Case |
|------|----------|
| `read-only` | Analysis, code review, PDCA root cause, documentation review |
| `workspace-write` | File creation, code generation (Jane reviews before commit) |
| `danger-full-access` | **NEVER USE** — violates Single Writer Principle |

**Verified** (2026-02-11):
- Connectivity test PASSED — Codex created `docs/codex-connectivity-test.md` via MCP `workspace-write`
- Jane verified file existence independently
- No human copy/paste involved

### Channel B: Codex Web Workspace (Reference Only — NOT for collaboration)

**Status**: Isolated sandbox. Cannot push to GitHub. `make_pr` generates metadata only.

| Capability | Status |
|------------|--------|
| `git clone` | Works (initial clone from GitHub) |
| `git commit` | Works (local sandbox only) |
| `git push` | **FAILS** — no `origin` remote configured |
| `make_pr` | **NOT a real GitHub PR** — internal metadata only |
| File read/write | Works (within sandbox only) |

**Conclusion**: Codex Web Workspace is useful for Allen's direct interaction with Codex (chatting, prototyping), but NOT part of the Jane↔Codex automated pipeline.

---

## 3. Permission Matrix

### IVCO Codebase (`allen-ivco/`)

| Path | Jane | Codex (MCP workspace-write) | Codex (Web Workspace) |
|------|------|----------------------------|----------------------|
| `cms/src/**` | Read + Write + Commit | Read + Write (local) | Read only (sandbox) |
| `cli/**` | Read + Write + Commit | Read + Write (local) | Read only (sandbox) |
| `scripts/**` | Read + Write + Commit | Read + Write (local) | Read only (sandbox) |
| `docs/**` | Read + Write + Commit | Read + Write (local) | Read only (sandbox) |
| `CLAUDE.md` | Read + Write + Commit | **Read only** | Read only (sandbox) |
| `.env*` | Read (with security DNA) | **NEVER** | **NEVER** |

### Knowledge System (`~/Vaults/Obsidian/`)

| Path | Jane | Codex |
|------|------|-------|
| `note/**` | Full CRUD + bidirectional links | **READ ONLY** |
| `research/**` | Full CRUD + AG DNA | **READ ONLY** |
| `task/**` | Full CRUD + index sync | **READ ONLY** |
| `inbox/**` | Full CRUD + routing | **READ ONLY** |

### System Configuration

| Path | Jane | Codex |
|------|------|-------|
| `~/.claude/rules/**` | Read + Write | **READ ONLY** |
| `~/.claude/agents/**` | Read + Write | **READ ONLY** |
| `~/.claude/skills/**` | Read + Write | **READ ONLY** |
| `memory/SCRATCHPAD.md` | Read + Write | **READ ONLY** |
| `~/.config/env/**` | Via credential-guard only | **NEVER** |

---

## 4. Collaboration Workflows

### Workflow 1: Codex Writes IVCO Code (Mixed Mode)

```
1. Jane plans the task (approach, files to modify, acceptance criteria)
2. Jane calls Codex MCP (workspace-write):
   - Provides: task description, relevant context, constraints
   - Codex: writes code to local filesystem
3. Jane reviews Codex output:
   - Read generated files
   - Verify against acceptance criteria
   - Check for security issues
4. Jane commits + pushes:
   - git add specific files
   - Semantic commit message
   - git push to origin
```

### Workflow 2: PDCA Root Cause Analysis (Read-Only)

```
1. Jane identifies issue, frames analysis direction
2. Jane calls Codex MCP (read-only):
   - Phase 1.5: Codex asks clarifying questions → Jane answers via codex-reply
   - Phase 2: Codex runs 5 Whys, impact scan, produces structured report
3. Jane reviews report:
   - Approves → executes improvements in Main Session
   - Rejects → sends feedback via codex-reply (max 2-3 rounds)
```

### Workflow 3: Code Review by Codex

```
1. Jane prepares diff or file list
2. Jane calls Codex MCP (read-only):
   - Provides: code to review, context, standards
   - Codex: analyzes code, identifies issues, suggests improvements
3. Jane evaluates suggestions:
   - Accepts: implements changes herself
   - Rejects: explains why (learning loop)
```

### Workflow 4: Documentation Generation

```
1. Jane identifies documentation need
2. Jane calls Codex MCP (workspace-write):
   - Provides: topic, existing docs for context, target audience
   - Codex: generates documentation files
3. Jane reviews + enriches:
   - Adds bidirectional links (if Obsidian)
   - Updates index files
   - Commits + pushes
```

---

## 5. Path Standardization

### Codex MCP Working Directories

| Task Type | `cwd` Parameter |
|-----------|----------------|
| IVCO development | `/Users/allenchenmac/AI-Workspace/projects/allen-ivco` |
| Knowledge analysis | `/Users/allenchenmac/Vaults/Obsidian` |
| System analysis | `/Users/allenchenmac/AI-Workspace` |
| Tool development | `/Users/allenchenmac/AI-Workspace/projects/allen-ivco/cli` |

### Git Remotes (Jane manages all pushes)

| Repo | Remote URL | Protocol |
|------|-----------|----------|
| allen-ivco | `https://github.com/ConversionCrafter/allen-ivco.git` | HTTPS |
| obsidian-public | `https://github.com/ConversionCrafter/obsidian-public.git` | HTTPS (PRIVATE) |

---

## 6. Safety Rails

### Codex MCP Constraints

1. **NEVER use `danger-full-access` sandbox** — violates Single Writer Principle
2. **Codex cannot access `~/.config/env/`** — credential isolation (Security DNA)
3. **Codex cannot modify `~/.claude/`** — agent configuration is Jane-only territory
4. **Codex output MUST be reviewed** before commit — no blind trust
5. **Codex cannot run destructive git commands** — no force push, no reset --hard

### Token Leak Prevention

- PreToolUse hook `token-leak-guard.sh` intercepts credentials in Write/Edit/Bash
- Codex MCP runs as subprocess — hook protection extends to its operations
- Credential files are in `~/.config/env/` (chmod 600) — outside Codex workspace scope

### Conflict Resolution

| Scenario | Resolution |
|----------|-----------|
| Codex writes file that Jane already modified | Jane's version takes priority (Single Writer) |
| Codex suggests conflicting architecture | Jane evaluates → Allen decides if needed |
| Codex output fails quality check | Jane sends feedback via `codex-reply`, max 2-3 rounds |
| Both want to modify same file | Sequential execution — Jane orchestrates, no parallel writes |

---

## 7. Verified Capabilities (2026-02-11)

| Test | Result | Evidence |
|------|--------|---------|
| Codex MCP connectivity | PASS | `docs/codex-connectivity-test.md` created by Codex |
| Codex MCP file write (workspace-write) | PASS | File verified by Jane independently |
| Codex MCP read-only analysis | PASS | PDCA root cause analysis (Session 9) |
| Codex MCP multi-turn conversation | PASS | `codex-reply` used in PDCA Phase 1.5→2→3 |
| Jane → Codex → Jane round-trip | PASS | No human copy/paste in loop |
| Codex Web Workspace git push | **FAIL** | No origin remote, sandbox isolation |
| Codex Web Workspace make_pr | **FAIL** | Metadata only, no actual GitHub PR |

---

## 8. Quick Reference

### Jane calls Codex for code generation:
```
mcp__codex__codex:
  prompt: "Write a TypeScript collection for {description}..."
  cwd: /Users/allenchenmac/AI-Workspace/projects/allen-ivco
  sandbox: workspace-write
  approval-policy: on-failure
```

### Jane calls Codex for analysis:
```
mcp__codex__codex:
  prompt: "Review the following code for {criteria}..."
  cwd: /Users/allenchenmac/AI-Workspace/projects/allen-ivco
  sandbox: read-only
  approval-policy: on-failure
```

### Jane continues Codex conversation:
```
mcp__codex__codex-reply:
  threadId: {from previous call}
  prompt: "Good analysis. Now focus on {specific area}..."
```

---

## Decision Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-02-11 | Single Writer = Jane | Allen: "write/edit 權限只能一人主控" — prevents conflict, ensures accountability |
| 2026-02-11 | Codex MCP as primary channel | Codex Web Workspace can't push to GitHub; MCP runs locally with full git access via Jane |
| 2026-02-11 | Mixed mode for IVCO code | Codex can write code (workspace-write), Jane reviews + commits. Knowledge system is read-only for Codex |
| 2026-02-11 | No `danger-full-access` | Violates Single Writer Principle; `workspace-write` is sufficient for all use cases |
| 2026-02-11 | Git as shared state layer | Both agents read from same repos; Jane is the only one who pushes |
