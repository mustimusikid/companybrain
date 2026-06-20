# Repo Hygiene Notes — 2026-06-20
Dibuat saat `chore/repo-hygiene`. Yang **sudah** dibereskan di PR ini + yang **perlu keputusan owner** (Dave/Tian) sebelum dihapus, karena ini repo bersama & sebagian mungkin konten unik.

## ✅ Sudah dibereskan di PR ini
- Hapus 4 file `.DS_Store` dari tracking + tambah ke `.gitignore` (+ `.obsidian/workspace.json`)
- Rename `contract-appreciation-&-offering-musti-musik.docx.md` → `contract-appreciation-and-offering-musti-musik.md` (buang `.docx` & `&`)

## 🟡 Perlu keputusan: 34 file `copy-of-*` (artifact 'Copy of' dari Drive)
Mayoritas yatim (ga ada original) — kemungkinan konten unik dengan nama jelek. Saran: rename buang prefix `copy-of-`, atau hapus kalau emang duplikat. 2 di bawah punya original TAPI isinya beda (cek versi mana yang benar):
```
- operations/hr/copy-of-contract-musti-musik.md
- operations/hr/copy-of-deep-learning-1.md
- operations/hr/copy-of-deep-learning.md
- operations/hr/copy-of-employee-management-1.md
- operations/hr/copy-of-employee-management.md
- operations/hr/copy-of-google-form-1.md
- operations/hr/copy-of-google-form.md
- operations/hr/copy-of-mm-hr-27-august,-2309.md
- operations/hr/copy-of-mm-hr-29-july,-2316.md
- operations/hr/copy-of-musti-musik-human-resources.md
- operations/hr/copy-of-peraturan-perusahaan-musti-musik.md
- operations/hr/copy-of-project-management-1.md
- operations/hr/copy-of-project-management.md
- operations/hr/copy-of-youtube-1.md
- operations/hr/copy-of-youtube.md
- product/academy/copy-of-testimonial-and-feedback-musti-musik.md
- product/books/copy-of-1-affiliate-explainer-vsl-script.md
- product/books/copy-of-[new]-$100m-money-models-book-launch-run-of-show-blackbook.md
- product/books/copy-of-copy-of-copy-of-copy-of-scripts-200-book-recap-vsl.md
- product/books/copy-of-master-scripts.md
- product/books/copy-of-scripts-$100m-200-book-bundle-thank-you-vsl-script.md
- product/books/copy-of-scripts-$100m-scale-advisory-script.md
- product/books/copy-of-scripts-800-book-offer-vsl.md
- product/books/copy-of-scripts-pre-event-registration-vsl.md
- product/books/copy-of-scripts-recap-vsl.md
- product/books/copy-of-scripts-vip-no-thank-you.md
- product/books/copy-of-scripts-vip-thank-you.md
- product/books/copy-of-scripts-vip-vsl.md
- product/music-school/archive/copy-of-360-review-self-assessment-file-make-a-copy.md
- product/music-school/archive/copy-of-job-offer-scripts.md
- product/music-school/archive/copy-of-reference-check.md
- product/music-school/archive/copy-of-spark-offer-letter.md
- product/music-school/archive/copy-of-spark-teacher-contract.odt.md
- product/paid-class/copy-of-project-plan.md
```

## 🟡 Perlu retitle: 2 file `untitled-*` (ADA isinya, judulnya 'Untitled')
```
- marketing/sales/untitled-spreadsheet.md
- operations/finance/untitled-document.md
- product/events/untitled-spreadsheet.md
```

## 🔴 PRIVACY — pindah ke DB (`hr_performance_reviews`/kontrak), jangan di repo (semua orang bisa baca)
Per brief 13 Juni: file per-orang (review/kontrak bernama) = DATA, bukan repo.
```
- operations/hr/regfan-utama-fathan-performance-marketing-intern.md
- operations/hr/ricardo-lucky-fernando-contract-appreciation-&-offering-musti-musik.docx.md
- product/music-school/archive/annual-performance-review-teachers-09.20.22.md
- product/music-school/archive/teacher-review-report-nathan-jones.md
```

## 🟡 Nama file langgar konvensi (koma/karakter aneh) — perlu rename
```
- marketing/ads/hook,-meat,-cta-ads-2025.md
- operations/finance/sop-finance,-accounting,-tax.md
- operations/hr/contract-appreciation-&-offering-musti-musik.md
- operations/hr/copy-of-mm-hr-27-august,-2309.md
- operations/hr/copy-of-mm-hr-29-july,-2316.md
- operations/hr/recruitment-&-offboarding-1.md
- operations/hr/recruitment-&-offboarding.md
- operations/hr/ricardo-lucky-fernando-contract-appreciation-&-offering-musti-musik.docx.md
- product/academy/topik-bedah-&-kuliah-piano.md
```
