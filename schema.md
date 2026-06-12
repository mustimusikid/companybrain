# Musti Musik Brain — Schema

## Frontmatter Template

---
title: Document Title
domain_tag: [primary_domain, subdomain]
doc_type: sop
---

> One-line summary of what this document covers.

## Allowed doc_type values
- `sop` — standard operating procedure, process guide, handbook
- `strategy` — company strategy, OKRs, direction documents
- `transcript` — meeting transcripts, interview notes
- `rundown` — event rundowns, concert schedules, cue cards

## Fields NOT in frontmatter (ETL-computed)
- `repo_path` — computed from actual file path
- `source_tier` — derived: inbox/ → inbox | archive/ → archive | else → db_tracked
- `owner` — derived as domain_tag[0]
- `sha` — written by ETL from git

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
