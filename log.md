# Musti Musik Brain — Ingest Log

Append-only. Never rewrite existing entries.

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
