---
title: Meta Ads SOP
domain_tag: [marketing, ads]
doc_type: sop
owner: marketing_head
status: Approve
confidentiality: Internal
source: gdrive
review_frequency: annually
---

> SOP Performance Marketing untuk Meta (Facebook/Instagram) Ads: setup Business Manager, struktur campaign/adset/ads, audience (saved/custom/lookalike), pixel, Orthodox Matrix (OCLP, LP Convert), scaling, rules, manual bidding, dan SOP scripting ads.

## How To Set Up A Facebook Ads Campaign

1. **Membuat Business Manager & Akun Iklan:** Hindari menjalankan iklan dari akun pribadi. Business Manager memberi kendali atas peran tim, akses aset, dan pembayaran — penting untuk skalabilitas.
2. **Membuat Campaign & memilih objective sesuai funnel:** Awareness ("Reach"/"Brand Awareness"), Consideration, atau Conversion ("Conversions"/"Leads"). Sesuaikan objective dengan hasil agar AI Meta bekerja efektif.
3. **Ad Set — Audiens, Anggaran, Jadwal, Penempatan:** Pakai Advantage+ Audience bila belum tahu target; manual bila punya data (lokasi, usia, gender, interest, behavior, demografi). Budget Lifetime/Daily memengaruhi reach (≈$5/hari ≈ 53rb–150rb orang; $2/hari ≈ 21rb–62rb). Atur Schedule (start/end). Placement: Automatic vs Manual.
4. **Membuat Ads:** Pilih Identity (Page + IG), Ad Setup (Create Ad: Single Image/Video, Carousel, Collection), Ad Creative (Add Media), Primary Text dengan hook di awal. A/B test beberapa kreatif/teks dalam 1 ad set.
5. **Tracking performa:** Pakai Ads Manager; fokus CTR, CPC, CPA. Evaluasi setelah min. 1 minggu; perhatikan fase learning.

## Tips Tracking Ad Clicks

- Sebagian besar klik di ponsel.
- Klik tinggi tanpa penjualan = masalah di landing page.
- CTR = (Click / Reach) × 100.
- Dua kolom CTR di Ads Manager: **CTR (All)** = semua klik (like, share, links); **CTR (Links)** = klik tautan.

## Poin Penting untuk Advertiser Pemula

1. Mulai dari tujuan jelas sesuai tahap funnel.
2. A/B testing berkala.
3. Optimasi berbasis data dari Ads Manager.
4. Gunakan Advantage+ jika masih baru.
5. Jangan terlalu cepat menilai hasil (beri ≥1 minggu).

## Basic Meta Ads

- **Objective Musti Musik:** Leads & Sales. Sales untuk bootcamp & akademi (sudah punya audiens, tujuan conversion); Leads untuk free class (landing page minta nama/email/no telp).
- **3 Algoritma Meta:** based on Interest, based on Behavior, based on Kesamaan (lookalike dari pelanggan & followers).
- **Facebook Pixel:** Settings → Event Setup Tools → masukkan link website yang di-track → lakukan tracking.
- **Dashboard:** Ads Reporting (filter waktu, pilih metrics), Audiences, Campaign (A/B Testing, Breakdown placement/usia/gender).

### Audiences

- **Saved Audience:** first-party Meta — set berdasarkan interest/demografi (Location, Age, Detailed Targeting seperti Jazz/Piano/Music Education; Narrow dengan Engaged Shopper untuk Purchase). Untuk objective Purchase JANGAN centang "Reach more people likely to respond" agar tetap targeted.
- **Custom Audience:** target orang yang sudah kenal produk. Source: Website (+Events tracking), App, Customer list, dll. Atur Audience Retention (mis. 180 hari). Penamaan: `MM_Purchase_180D`.
- **Lookalike Audience:** target orang yang belum kenal produk tapi perilakunya mirip custom audience (mis. Purchase). Atur kemiripan 1%–3% (1% paling mirip).

## Advance Meta Ads — Struktur

- **Campaign (induk):** pilih objective, Advantage Budgeting, A/B testing, Advantage+ catalog ads, kategori khusus (kredit/kerja/politik/housing) wajib dipilih bila relevan agar tidak banned.
- **Ad Set (kontrol):** setup pixel + event relevan, tanggal, audience, lokasi, umur, gender, interest, Placement (Advantage+ vs Manual).
- **Ad:** konten iklan.

### Setting Campaign → Adset → Ads (praktik MM)

- Campaign: Create → objective LEADS (freeclass) / SALES (bootcamp & akademi) → Manual sales campaign → nama mis. `BOOTCAMP / NOV / PROS / AON / CONVERSION / PURCHASE`. Budgeting di Ad Set dulu, baru Advantage budgeting setelah ada ads winning.
- Adset: nama mis. `LAL / Sales / Indo / 21-55 / Nama Creative`; Conversion=Website; Performance Goal=Maximize conversions; Datasets=Musti Musik; Conversion Event=Purchase. Budget contoh: 4jt / 8 adset / 10 hari = Rp50.000/hari/adset. Audience: switch to original → custom/lookalike; age, gender, interest.
- Ads: nama mis. `Ad / Dark Post / Video / Creative Name`; Identity Page "Musti Musik" + IG "mustimusik.id"; Creative source Manual Upload; Video ad; Primary Text + Headline; CTA "Book Now"; Destination Website (mis. mustimusik.id/bootcampads/); Tracking Musti Musik Datasets → Publish.

## Rumus Metrik Dasar

- **Reach:** jumlah unik orang yang melihat iklan (ditargetkan Meta). **Impression:** total tayangan iklan, termasuk yang melihat >1×.
- **Result:** jumlah tindakan sesuai tujuan campaign (klik, konversi, purchase). **Amount Spent:** total biaya campaign.
- **CPR (Cost Per Result)** = Amount Spent / Results.
- **CPC (Cost Per Click)** = Amount Spent / Link Click.
- **CTR (Link Click-Through Rate)** = (Link Click / Impression) × 100%.
- **CPM (Cost Per Mille)** = (Amount Spent / Impression) × 1000.
- **CR Purchase to LC** = (Purchase / Link Click) × 100%.
- **Purchase ROAS** = Revenue / Amount Spent.

## Orthodox Matrix

- **CTR – Link Click:** relevansi konten vs audiens. Standar 1%.
- **OCLP (Outbound Click Landing Page):** % klik yang benar masuk LP = Landing page views / Link clicks. Standar 70%.
- **LP CONVERT:** mengukur LP/offer/pricing/copy = (pixel result, mis. Website leads) / Landing page views. Standar 25% (di bawah 25% bisa tetap profitable).
- Setup custom metric: Columns → Customize → Create Custom Metric → rumus → format Percentage → Save kolom "ORTHODOX MATRIX".

## Scale Up & Scale Out

- Scale hanya bila campaign winning (perform baik dalam 7 hari).
- **Scale Up:** naikkan budget bertahap ≤20–30%/24 jam (mis. Rp500rb→Rp600rb). Pantau CTR, Frequency (<3).
- **Scale Out:** ad set baru dengan targeting/kreatif berbeda (lookalike/custom baru). Pantau Impression vs Clicks, Engagement Rate.
- Metrics keseluruhan: CTR >1%, Frequency <3, Conversion Rate, Impression & Reach.

## Rule (CBO)

- Buat rule: matikan campaign pukul 23.00/24.00 WIB, nyalakan lagi 05.00 WIB (audiens Indonesia tidur, hemat budget). Hanya untuk CBO; jangan untuk ABO.
- More → Create a new rule → centang campaign → Action "Turn off campaign", Time range "Today", Schedule Custom semua hari 05.00–23.30 → Create.
- **Rule anti-boncos:** tujuannya campaign auto-off kalau spend tinggi tanpa hasil. Bisa set 1-3 rule per campaign. Cara: klik campaign → Create new rule → Custom rule → beri nama (mis. "Spent 30rb No Pur Off") → Apply to campaign → Condition: Spent greater than Rp30.000 AND Purchase smaller than 1 → Time range "Today" → Create. Bertingkat, contoh rule ke-2: "Spent 50rb No Pur Off" (Turn off campaign, Spent > Rp50.000, Purchase < 2, Today). Bisa dilanjutkan rule ke-3 sampai ke-5 dengan threshold makin tinggi.

## Manual Bidding

- Default: Highest Volume Bidding.
- **Bid Cap** (hanya CBO): batas maksimum bid (mis. KPI Rp25.000/result; Meta cari convert di bawahnya). Syarat: daily budget min Rp200.000 dan sudah tahu CPR (mis. average Rp15.000 < Rp25.000). Aktifkan Advantage campaign budget → Campaign Bid Strategy "Bid Cap" → Adset Bid control Rp25.000.
- **Cost Per Result (CPR):** atur biaya per hasil rata-rata manual; budget harian jangan terlalu rendah. Setting sama seperti Bid Cap.

## SOP Scripting Ads

- **Istilah:** Call Out/Hook (Goal Hook, Pain Point Hook, Avatar Hook); Creative Targeting; Winning Script; Benchmarking.
- **Alur:** Riset & Persiapan (avatar, benchmarking via Meta Ads Library, kumpulkan pain point) → Penyusunan Skrip (Hook → Pain Point → Trust Building → CTA) → Kreativitas Visual (Reels: hook 3 detik; Carousel) → Dokumentasi skrip (Google Doc/PPT: jenis iklan, tanggal, CTR) → Uji & Evaluasi.
- **Implementasi:** brief H-7 (inspirasi, format, target), upload ke database; monitor CTR; perbarui Winning Script.
