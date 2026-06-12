# Musti Musik Brain — Resolver

Walk this decision tree before filing any document. Read this file first.

1. Is it a concert/event rundown, cue card, or event schedule? → **product/events/**, doc_type: rundown
2. Is it a meeting transcript? → file under the domain it concerns, doc_type: transcript. Exception: individual agency meeting notes → DB (agency_meeting_minutes), not repo
3. Is it about HOW TO RUN a freeclass, masterclass, bootcamp, or concert? (operational SOP, checklist, host process, registration flow) → **product/events/**
4. Is it about WHAT IS IN a class? (curriculum, module content, lesson plan, study guide, course bundle) → **product/paid-class/**. Rule: ops team uses it → events/ | teacher uses it → paid-class/
5. Is it about online academy content, modules, or member onboarding? → **product/academy/**
6. Is it about the physical music school? (teachers, students, schedules, TnC, teacher contracts, school SOPs) → **product/music-school/**
7. Is it reference material from "Build A Music School" external course? → **product/music-school/archive/**. ETL does NOT embed archive/ — human reference only.
8. Is it about books (buku jazz/worship) — production, launch, SOP? → **product/books/**
9. Is it an ads strategy, script TEMPLATE, or performance marketing SOP? → **marketing/ads/**. Individual winning scripts as data → DB marketing_ad_scripts table.
10. Is it about organic content creation, video editing, or scripting? → **marketing/organic/**
11. Is it a sales playbook, outreach script, CS flow, or lead handling guide? → **marketing/sales/**
12. Is it about employee contracts, handbook, job description TEMPLATES, company regulations, org chart, or hiring PROCESS? → **operations/hr/**. ⚠ Per-person PDR files → DB hr_performance_reviews, NOT the repo.
13. Is it a financial SOP, COA guide, or cost allocation process? → **operations/finance/**
14. Is it about tech systems, n8n workflows, or automation SOPs? → **operations/tech/**
15. Is it about B2B partnerships or reseller process? → **operations/partnership/**
16. Is it about external agency vendors or quotation process templates? → **operations/agency/**. Individual meeting notes → DB agency_meeting_minutes.
17. Is it a company-wide strategy doc (OKRs, annual plan, direction)? → **operations/**, doc_type: strategy
18. Nothing fits? → **inbox/**. Flag for re-filing.

## Disambiguation
- Sales script + product-specific → marketing/sales/ (sales is primary)
- Finance SOP touching HR → operations/finance/ with domain_tag: [operations, finance, hr]
- Event SOP touching marketing → product/events/ (product is primary)

## ETL Skip Rules
- inbox/** → skip embedding, source_tier = inbox
- **/archive/** → skip embedding, source_tier = archive
- Files missing frontmatter → skip, log error
