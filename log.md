# Musti Musik Brain — Ingest Log

Append-only. Never rewrite existing entries.

## 2026-07-19 (product/ full cleanup pass)
- **Deleted (6 files, certificate-merge data missed in original June purge):** `product/events/masterclass-{agustus,desember,juli,november}.md`, `product/events/untitled-spreadsheet.md`, `product/paid-class/special-class-maret-2026.md`
- **Renamed (14 files, removed `copy-of-`/`untitled-` artifacts):** 12 Hormozi book-launch reference scripts in `product/books/` renamed to `book-launch-*-reference.md` pattern; `product/paid-class/copy-of-project-plan.md` → `bootcamp-project-plan.md`; `product/academy/copy-of-testimonial-and-feedback-musti-musik.md` → `testimonial-and-feedback-transcript.md`
- **Metadata migrated (130 files):** added `owner` (role per subfolder: academy_head/books_head/events_head/music_school_head/paid_class_head), `status: Unknown`, `confidentiality: Internal`, `source` (`ai` for the 9 docs I authored this month, `gdrive` for the rest), `review_frequency` (evergreen for reference/strategy/transcript, annually for sop, quarterly if pricing keywords detected) — all per Migration Defaults in schema.md. `status` intentionally left `Unknown`/not `Approve` — accuracy verification needs a human, per the schema's own tiering.
- **Structural fixes:** removed 3 files' `•⁠` bullet-artifact characters (`worklist-musti-musik.md`, `competitor-analysis.md`, `customer-success-1.md`); converted 22 files from H1-only chapter dividers to real `##` chunk boundaries (list in commit) — these previously had zero valid chunk boundaries per Chunking Convention
- **Flagged, not auto-fixed:** 64 files still have standalone bold lines that may be pseudo-headings (`**Some Title**` used as a heading instead of `##`/`###`) — not bulk-converted because some bold lines are legitimate emphasis (full sentences, signature-line underscores), not headings; converting blindly risked corrupting content. Needs individual review — good candidate for the department Claude Code review sessions (see the "review/[departemen]" branch workflow already in place).
- Not touched: `product/*/archive/` (51 files, already excluded from ETL embedding, out of scope for this pass) and body-content prose cleanup (escaped chars — none found; wall-of-text-to-list conversion — not attempted at this scale, left for department review sessions)

## 2026-07-19 (cleanup)
- Removed `operations/hr/performance-marketing.md` — misfiled duplicate (31k words, mixed Newsletter/Meta Ads/YouTube/TikTok content) missed by the marketing team's metadata PR because it lived in operations/hr, out of that PR's scope. Content already fully superseded by `marketing/ads/newsletter-sop.md`, `meta-ads-sop.md`, `youtube-analytics-sop.md`, `marketplace-ads-tiktok-shopee.md`. Its twin at `marketing/ads/performance-marketing.md` was already removed by the team's own PR.

## 2026-07-19
- Expanded `schema.md` metadata design (decided w/ Dave + AI engineer Faris before Foundation Phase kickoff):
  - Added `doc_type: reference` (external knowledge, not internal SOP) + explicit decision tree for sop/strategy/transcript/rundown/reference classification
  - Added guidance: split mixed-doc_type files (e.g. Employee Handbook) into separate files by content boundary rather than force one label
  - Split `owner` (manual, accountability) from `Access` (not a frontmatter field — computed at query time from domain_tag + a Postgres role→scope table, not yet built)
  - Added `status` (Approve/Draft/Archive/Unknown), `confidentiality` (Internal/External), `source` (gdrive/manual/ai/whatsapp/external), `effective_date` (conditional), `review_frequency` (optional), `superseded_by` (optional)
  - `last_reviewed` added as ETL-computed (git commit date), not manual frontmatter
  - `status: Archive` now has the same ETL skip effect as the `archive/` folder — see RESOLVER.md
  - No backfill executed yet on the 464 existing files — migration defaults documented in schema.md, actual backfill is Foundation Phase / Faris's work

## 2026-06-18
- Marketing/tech SOP intake (7 source files → 7 new docs)
- marketing/ads/meta-ads-sop.md — Meta/FB ads SOP (campaign structure, audiences, pixel, Orthodox Matrix, scaling, bidding, ad scripting)
- marketing/ads/marketplace-ads-tiktok-shopee.md — TikTok Ads + Shopee Ads/CPAS
- marketing/ads/youtube-analytics-sop.md — YouTube analytics & reporting SOP (thumbnails, retention, baseline)
- marketing/ads/newsletter-sop.md — newsletter & email marketing SOP (Mailketing tutorial, metrics)
- marketing/organic/ai-content-creation-module.md — AI content training (LLM basics, prompting, image/video/voice tooling, OpenClaw, 7-day roadmap)
- operations/tech/n8n-setup-guide.md — n8n setup/workflow guide (filed to tech per RESOLVER #14, not marketing)
- marketing/sales/sales-halo-ai-agent-spec.md — HALO AI CS/sales agent spec + full KB (Sekolah Musik, Akademi, Masterclass, PO Buku, Free Class) with live pricing
- Borderline calls: AI Module → organic (content creation) over tech; Newsletter/YouTube → ads (Performance Marketing team SOPs) alongside existing performance-marketing.md / email-marketing-template.md

## 2026-06-12
- Initial import from Google Drive (618 Excel + docx files audited)
- Converted all docx → md, Excel SOPs → md, data files filtered to DB
- Applied gbrain MECE restructure per Engineering Brief v1.1
- Removed ~190 individual PDR files and response files from brain → DB hr_performance_reviews / hr_recruitment ingest
- Rerouted misfiled SOPs to correct domain folders (295 files rerouted)
- Generated: RESOLVER.md, schema.md, index.md, log.md, per-directory READMEs
- Final file count: 591 markdown files across all domains (see index.md)

## 2026-06-17
- Product division SOP intake (13 source files → 10 new docs; 3 `- Copy` files were byte-identical duplicates, skipped)
- product/books/sop-book-making.md — book production SOP (curriculum → AI gen → layout → visual/QR → QC)
- product/books/book-launch-gantt-chart.md — book launch timeline (launch 26 Jun 2026, harga Rp89.999)
- product/events/bootcamp-gantt-chart.md — bootcamp ops timeline (Oct 2025)
- product/events/freeclass-gantt-chart.md — free class ops timeline template
- product/events/masterclass-gantt-chart.md — masterclass ops timeline (Mar 2026)
- product/events/offline-concert-gantt-chart.md — offline student concert, 5-phase timeline (28 Feb 2026)
- product/events/online-concert-gantt-chart.md — online concert timeline (30 Mar 2026)
- marketing/organic/sop-midi-editing.md — MIDI/backing-track sync SOP for private-student video content
- product/academy/flow-customer-success-academy-online.md — academy member CS flow + 8 WA templates (per-domain filing, RESOLVER rule 5 over 11)
- product/music-school/flow-customer-success-sekolah-musti-musik.md — music-school student CS flow + templates + pricing

## 2026-06-17 (data purge)
- Audited all 620 files; found ~156 mislabeled as doc_type:sop that are actually data records (slipped through the 2026-06-12 DB filter). Removed from repo — canonical home is DB/Drive/CRM/accounting. Recoverable via git history.
- Categories removed: recording/video-link logs (~47), student homework/Q&A/answer keys (~45), member/registrant/lead/attendance rosters (~14), finance/order/settlement ledgers (~11), certificate merge tables (~9), dashboards/metric reports (~7), CVs + recruitment responses (~11 → DB hr_recruitment), trackers/survey data (~8), single-fact snippets (~3)
- Kept (process docs in table form): all *-gantt-chart, worklist, rundown, project-plan; archive/** templates
- File count: 620 → 464 markdown files
- NOT deleted, flagged for human review: operations/finance/finance.md (actually an HR job description — recategorize to operations/hr/), operations/finance/untitled-document.md (images only), product/events/untitled-spreadsheet.md, borderline-keeps (donasi-masterclass, spt-pajak, competitor-analysis, road-map)
