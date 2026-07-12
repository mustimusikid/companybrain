# Musti Musik Brain — Schema

## Frontmatter Template

---
title: Document Title
domain_tag: [primary_domain, subdomain]
doc_type: sop
owner: marketing_head            # role, not a person's name — see Owner section
status: Unknown
confidentiality: Internal
source: manual
effective_date: YYYY-MM-DD       # ISO 8601 date format, required for this field whenever it's set
review_frequency: monthly
superseded_by: other-file.md     # optional — only set on archived/outdated docs
---

> One-line summary of what this document covers.

## Allowed doc_type values
- `sop` — standard operating procedure, repeatable process, handbook chapter
- `strategy` — direction-setting: goals, OKRs, vision/mission, why we're prioritizing X
- `transcript` — raw/lightly-cleaned record of a meeting or interview, dialogue-like
- `rundown` — timed sequence for ONE specific occurrence of an event
- `reference` — knowledge sourced from OUTSIDE Musti Musik (course, book, benchmark), not our own process/decision

### Decision tree (check in order, first match wins)
1. Is this a record of what people actually said, in order, not deliberately structured? → **transcript**
2. Does it have specific dates/times tied to ONE occurrence — not a template reused with new dates each time? → **rundown**
   (Test: if you strip the dates, does it still read as "the way we always do X"? If yes, it's `sop`, not `rundown` — most of our recurring event gantt charts are `sop` for this reason, since teams copy the same file and just change dates each month.)
3. Is this about deciding what to do / why (direction, priorities, positioning), not the steps to execute it? → **strategy**
4. Is this the repeatable process the team actually follows — regardless of where the knowledge originally came from? → **sop**
   (Where it came from is a separate question, captured by the `source` field, not `doc_type`. Example: Meta Ads SOP originated from external training (`source: external`) but is now literally how the team runs ads — that makes it `doc_type: sop`, not `reference`.)
5. Otherwise (external material we keep as background knowledge, not yet adopted as our own operating process) → **reference**

### One document, multiple doc_types
Don't force a mixed document into one label. Split it into separate files along its natural content boundaries (usually the existing `##` chapters), and give each file its own doc_type + metadata. Example — `Employee Handbook`:
- Vision/Mission/History chapters → `strategy` (also a candidate for `confidentiality: External` — safe to share with candidates/public)
- Culture Code chapter → `strategy`
- HR Policy (attendance, leave, termination) → `sop`, `confidentiality: Internal`
- Compensation Philosophy + pay grade tables → `sop`, `confidentiality: Internal` (most sensitive section — this is exactly why splitting matters, since one file can't hold two different confidentiality levels)

If a chunk still resists clean classification after splitting as far as reasonably possible, just pick whichever type covers >50% of the content. Don't over-optimize for purity.

## Owner vs Access — two different concerns, don't conflate
- **`owner`** (frontmatter field): **a role, not a person's name** — e.g. `marketing_head`, `academy_head`, `finance_head`. Sales SOPs are owned by `marketing_head` (there's no separate Sales Head), etc. Using a role instead of a name means owner stays correct through staff turnover — nobody needs to bulk-edit files just because someone changed jobs or left. Owner values should be drawn from the **same canonical role list** used for Access below — one source of truth for roles, not two lists that can drift apart.
  - Since owner is now role-based, it's largely **auto-suggestible**: the role that heads a document's `domain_tag` (via the same role→scope table used for Access) is usually the right owner — the system can pre-fill it, and a human only needs to override for edge cases (e.g. a sub-domain with its own lead distinct from the parent division head).
- **Access** (NOT a frontmatter field): who is *allowed* to see this document. Computed at query time from `domain_tag` cross-referenced against the same role→scope permission table living in Postgres (e.g. `hr_roles`: `ads_intern → [marketing, ads]`, `marketing_head → [marketing]`), tied to actual HR role data. Never written per-file — one small permission table governs all 464+ docs, so a role change or reorg doesn't require re-tagging every file. (Not yet built — this is a Foundation Phase design decision for implementation in the next phase.)

## Status values
- `Approve` — reviewed and confirmed accurate
- `Draft` — work in progress, not yet vetted
- `Archive` — superseded/no longer valid (see `superseded_by` below); has the same ETL effect as physically living in an `archive/` folder — skipped from embedding
- `Unknown` — default for legacy bulk-imported docs that haven't been individually reviewed yet (this is the honest default for most of the June 12 migration — don't guess a status, label it `Unknown`)

## Effective Date
- **Required** when the document covers pricing, HR policy, or a dated campaign — content that can go stale in a way that actively misleads (e.g. an agent quoting an old price).
- **Optional/blank** for evergreen process SOPs where "effective since" doesn't carry real meaning.

## Confidentiality
- `Internal` — default; not for external eyes
- `External` — safe to share outside the company (recruiting material, public-facing "about us" content, etc.)

## Source (closed enum — don't use free text)
- `gdrive` — migrated from the original Google Drive during the June 12 bulk import
- `manual` — written directly into the vault (Obsidian/GitHub) as an original document
- `ai` — synthesized by an AI assistant from other raw material (spreadsheet, meeting notes, PDF)
- `whatsapp` — promoted from the WhatsApp listener's `captured_notes` buffer
- `external` — sourced from an external course, book, or training (pairs naturally with `doc_type: reference`)

## Review Frequency (required)
Fixed enum — how often this document needs re-verification:
`daily`, `weekly`, `monthly`, `quarterly`, `biannually`, `annually`, `evergreen`

Pairs with `last_reviewed` (below) to compute staleness (`now - last_reviewed > review_frequency` → flag for review). `evergreen` means content that essentially never goes stale (e.g. Vision/Mission, external `reference` material) and is exempt from the staleness check.

Suggested defaults by content type:
- Pricing, active campaigns, discount codes → `weekly` or `monthly`
- HR policy, compensation → `quarterly` or `biannually`
- Process SOPs (event playbooks, production flows) → `annually`
- Vision/Mission/Culture, `reference` docs → `evergreen`

## Supersedes / Superseded_by
- Set `superseded_by: <filename>` on the **old** document when a newer version replaces it (e.g. pricing changes: old file gets `status: Archive` + `superseded_by: harga-akademi-2027.md`). This gives anyone (human or agent) who lands on stale content — because it's still semantically similar and could surface in search — a clear pointer to current truth. Only set when applicable; most documents never need this field.

## Fields NOT in frontmatter (ETL-computed)
- `repo_path` — computed from actual file path
- `source_tier` — derived: inbox/ → inbox | archive/ → archive | `status: Archive` → archive | else → db_tracked
- `sha` — written by ETL from git
- `last_reviewed` — the git commit date this file was last modified. This is an automatic proxy, not a guarantee of human verification — a doc can go untouched for years and still be correct, or get a typo fix that bumps the date without anyone actually re-checking the substance. Start with this free auto-computed value; only add a manual override field later if it proves insufficient in practice.

## Migration Defaults (for existing 464 files, backfill pass)
- `owner`: auto-suggest from the role that heads the doc's `domain_tag` (via the role→scope table); human confirms or overrides for sub-domain edge cases
- `status`: `Unknown`
- `confidentiality`: `Internal` (safe default until reviewed)
- `source`: `gdrive` for anything from the June 12 import; `ai` for docs added afterward in AI-assisted batches
- `review_frequency`: default `quarterly` if the doc_type-based suggestion above doesn't obviously apply; adjust per-doc during backfill where it matters (pricing/campaign docs especially)
- `last_reviewed`: no manual work needed — computed automatically from git

## Who Edits What: Manual vs AI-Assisted vs Fully Automated
Three tiers, not two — most fields aren't "type it from scratch" for a human, they're "confirm what the system already suggested":

**Strictly human (AI can't do this, don't try):**
- The actual document content/process knowledge itself
- Final `status: Approve` stamp — someone has to vouch it's correct
- HR role assignments (a separate system action, not a per-doc edit)

**AI-assisted, human confirms (the system suggests, human clicks agree/override):**
- `title`, `domain_tag`, `doc_type` — suggested via the decision tree above
- `owner` — suggested from domain_tag → role table lookup
- `effective_date` — extracted from the text when a date is explicitly mentioned
- `superseded_by` — suggested via similarity search against existing docs
- `confidentiality` — suggested from content patterns, but `External` specifically always needs an explicit human confirm given the leak risk
- `review_frequency` — suggested from the doc_type defaults above

**Fully automated, no review needed:**
- `repo_path`, `source_tier`, `sha`, `last_reviewed` — ETL-computed
- `source` — inferable from which ingestion pipeline the content came through (e.g. `whatsapp` if promoted from a WA capture, `ai` if AI-drafted)
- Access — computed at query time, never touches individual files

## Page Format

### Flat Format (use for SOPs)
frontmatter → > summary line → ## sections → content

### Two-Layer Format (use for strategy, rundowns, transcripts)
frontmatter → > summary → compiled truth sections → ---
→ ## Changelog (append-only, reverse chronological)

## Chunking Convention
- `##` heading = chunk boundary for ETL ingest into knowledge_chunks
- `###` sub-headings stay within their parent `##` chunk
- Minimum chunk: ~50 words (merge short sections with next)
- Maximum chunk: ~500 words (split long sections at paragraph boundary)
- Keep `##` sections focused: one process or concept per section

## Table Rules
- Use markdown tables for structured data
- Max 200 characters per cell (truncate with "...")
- Remove entirely empty columns

## Image References
- Store images in `<filestem>_images/` sibling folder
- Reference: `![description](filestem_images/image1.png)`
- Alt text required — used as OCR context fallback

## Agent → Brain Scope
| Agent            | domain_tag filter              | Use case                     |
| ---------------- | ------------------------------ | ---------------------------- |
| Hermes (general) | all domains                    | General queries              |
| CFO Agent        | [operations, finance]          | Financial questions          |
| Marketing Agent  | [marketing]                    | Ads, content, sales          |
| Product Agent    | [product]                      | Product & customer questions |
| CS Agent         | [marketing, sales] + [product] | Customer-facing queries      |

## ETL Notes
- to_tsvector config: use 'simple' (not 'indonesian' — no built-in PostgreSQL config)
- HNSW index on knowledge_chunks.embedding
- Upsert key for knowledge_documents: repo_path (computed from actual file path)
- `captured_notes` (granular WhatsApp captures, DB-only — never the repo) is a staging
  buffer on the listener's Postgres, deduped on raw_message_id. It stores NO embeddings;
  a scheduled sync feeds each new capture into gBrain via `gbrain capture` (which embeds
  with the brain's own model + wires the graph). Agents then see captures through gBrain
  under the same domain_tag scope as curated docs. The buffer never writes the repo; the
  only chat→repo path is human-gated promotion (see RESOLVER rule for WhatsApp captures).
