# Research Workflow Design

> Date: 2026-02-13
> Status: Approved by Allen
> Approach: B — SOP Reference File + Agent DNA Updates

---

## Context

IVCO pre-development phase produces high-value research artifacts (DNA, Allen Framework analysis, methodology comparisons) that deserve structured capture. Today's "Allen Framework vs Buffett Owner Earnings 1986" paper was handcrafted without a standard workflow. This design establishes a repeatable process.

## Design Decisions (Allen's Choices)

| # | Question | Decision |
|---|----------|----------|
| 1 | Trigger | Auto-detect: Jane proposes when insight found, Allen approves |
| 2 | Audience | Dual-version: internal (wikilink+index) + external (self-contained) |
| 3 | Knowledge architecture | Belongs in `research/{topic}/papers/` |
| 4 | Agent division | Parallel competition: Jane + Codex write independently, Allen picks best, loser reviews |
| 5 | Quality standard | Triangulation required: minimum 3 independent sources cross-verified |
| 6 | Implementation form | Agent DNA definitions (not a new skill), unified SOP reference file |

## Post-Review Corrections (Codex Review, Allen Approved)

| # | Original | Correction |
|---|----------|------------|
| 1 | AI-assisted analysis = independent source type | AI = **Tier 3** synthesis tool. Does NOT count toward ≥3 minimum. ≥3 must be Tier 1 (primary) + Tier 2 (secondary) |
| 2 | Single 6-phase workflow for all research | **Lite Mode** (default): DETECT→TRIANGULATE→PUBLISH→APPROVE. **Full Mode** (Allen 指定): all 6 phases with COMPETE |
| 3 | Jane + Codex symmetric parallel competitors | Codex = **External Challenger** (intentionally asymmetric). Jane = deep Allen Framework. Codex = fresh outside perspective |

## 6-Phase Workflow

### Phase 1: DETECT

- **Who**: Jane (automatic detection during work)
- **Trigger conditions** (any one):
  - Cross-system insight (e.g., DNA review reveals methodology innovation)
  - External literature x internal framework produces meaningful comparison
  - Major system work completed (>=3 files / new DNA / >=10% impact)
  - Allen explicit instruction
- **Output**: Research Proposal (topic + why + estimated sources)
- **Gate**: Allen approves

### Phase 2: TRIANGULATE

- **Who**: Jane (source identification)
- **Source types**:
  - A. Primary reading (original literature / official documents / financial reports)
  - B. AI-assisted analysis (NotebookLM / Codex / other LLMs)
  - C. Internal implementation (Allen calculations / DNA / case studies)
  - D. External reference (academic papers / industry reports / book chapters)
- **Rule**: Must cover at least 3 of 4 types (A/B/C/D)
- **Gate**: Sources confirmed >= 3

### Phase 3: COMPETE

- **Who**: Jane + Codex (parallel, independent)
- **Jane version**: Deep Allen Framework integration, wikilinks, DNA references
- **Codex version**: External perspective, fresh AI paradigm viewpoint
- **Shared constraints**: Same material package, same outline, same word count range
- **Gate**: Both drafts complete

### Phase 4: SELECT + REVIEW

- **Who**: Allen (selection) + losing agent (review)
- **Allen**: Picks best version as base
- **Losing agent**: Devil's Advocate Review of winning version
  - Argument gaps?
  - Source accuracy?
  - Over-extended conclusions?
- **Output**: Review Report + suggested changes
- **Gate**: Review complete

### Phase 5: PUBLISH (Dual-Version Output)

- **Who**: Chi (engineering output)
- **Internal version**:
  - Location: `research/{topic}/papers/{slug}.md`
  - Format: Obsidian frontmatter + wikilink + contributed-to
  - Update: `research/{topic}/index.md` Knowledge Sources table
- **External version**:
  - Location: `allen-ivco/docs/papers/{slug}-public.md`
  - Format: Self-contained, no wikilinks, full citations, abstract field
  - Ready for: ivco.io / blog / X publication
- **Gate**: Both versions ready

### Phase 6: APPROVE

- **Who**: Allen (final review)
- **Decision**: Publish / Revise / Archive (no publish)
- **Post-approval**: Update SCRATCHPAD + knowledge system indexes

## File Structure

```
research/{topic}/
├── index.md                          # Update Knowledge Sources table
├── action-guide.md                   # Update if affected
└── papers/                           # New directory
    └── {slug}.md                     # Internal version

allen-ivco/docs/papers/               # New directory
└── {slug}-public.md                  # External version
```

## Internal Version Frontmatter Template

```yaml
---
id: paper-{slug}
type: research-paper
status: draft | review | published
created: YYYY-MM-DD
last-updated: YYYY-MM-DD
version: 1.0.0
topic: "{research topic name}"
description: "One-line summary"
tags: [tag1, tag2]
source-documents:
  - "Source 1 full citation"
  - "Source 2 full citation"
  - "Source 3 full citation"
triangulation:
  source-a: "Primary reading — {description}"
  source-b: "AI-assisted — {description}"
  source-c: "Internal implementation — {description}"
contributed-to:
  - "[[research/{topic}/action-guide]]"
analysts:
  jane-version: "{Jane version angle}"
  codex-version: "{Codex version angle}"
  selected: "jane | codex"
  reviewer: "jane | codex"
---
```

## External Version Differences

- No `contributed-to`, no wikilinks
- `source-documents` uses full external citation format (author, year, title, URL)
- Add `abstract:` field (3-5 line summary)
- Add `## About IVCO` intro section at end

## Quality Checklist (Phase 4 Review)

```
[ ] Triangulation — at least 3 independent sources cross-verified
[ ] Source attribution — every argument traceable to specific source
[ ] No over-extension — conclusions do not exceed evidence support
[ ] Internal-external consistency — both versions share identical core arguments
[ ] Allen Framework alignment — no contradiction with DNA / CLAUDE.md
[ ] Actionability — clear implications for IVCO development or investment decisions
```

## Agent DNA Updates Required

### jane.md
- Add: Research Detection Protocol (trigger conditions + proposal format)
- Add: Phase role definitions (DETECT, TRIANGULATE, COMPETE, SELECT+REVIEW)
- Add: Quality Gate checklist reference

### codex.md
- Add: Research Paper Protocol (parallel competitor role)
- Add: Constraints (read-only sandbox, no internal knowledge access, plain text output)

### chi.md
- Add: Dual-Version Publishing Protocol (internal/external conversion + index updates)

### references/research-workflow.md (NEW)
- Complete 6-phase SOP with flow diagram
- Input/output/gate conditions per phase
- Full quality checklist
- File templates (internal + external)
- Case study: Buffett 1986 paper as worked example

## Implementation Deliverables

| # | Deliverable | Type |
|---|-------------|------|
| 1 | `references/research-workflow.md` | New file — unified SOP |
| 2 | `jane.md` update | Edit — Research Detection Protocol |
| 3 | `codex.md` update | Edit — Research Paper Protocol |
| 4 | `chi.md` update | Edit — Dual-Version Publishing Protocol |
| 5 | `research/investing/papers/` | New directory |
| 6 | `docs/papers/` | New directory |
| 7 | Move today's Buffett paper | Migrate from `note/` to `research/investing/papers/` |
| 8 | Create external version of Buffett paper | First case study output |
