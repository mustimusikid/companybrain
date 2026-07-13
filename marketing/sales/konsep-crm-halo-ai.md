---
title: Konsep CRM — Requirement Meeting Halo AI (29 Mei 2026)
domain_tag: [marketing, sales]
doc_type: reference
owner: marketing_head
status: Archive
confidentiality: Internal
source: gdrive
review_frequency: evergreen
superseded_by: sales-halo-ai-agent-spec.md
---

> Dokumen persiapan meeting requirement CRM dengan vendor Halo AI (29 Mei 2026). Diarsipkan — meeting sudah terjadi, hasil aktualnya ada di sales-halo-ai-agent-spec.md.

**KONSEP CRM**
Dokumen Kebutuhan & Persiapan Meeting
Halo AI — CRM Feature Discussion

## 1. Apa Itu CRM?
CRM (Customer Relationship Management) adalah sistem untuk mengelola semua interaksi dengan calon pelanggan (leads) dan pelanggan aktif — mulai dari pertama kali mereka masuk, sampai mereka closing dan seterusnya.

Intinya: satu tempat terpusat untuk mengetahui siapa leads-mu, dari mana datangnya, sudah di tahap mana, dan apa yang perlu dilakukan selanjutnya.

**Manfaat Utama CRM**
Semua data leads tersimpan di satu tempat, tidak tersebar di WhatsApp, DM, email, dan spreadsheet
Tim sales tahu persis leads mana yang perlu diprioritaskan hari ini
Follow-up tidak ada yang terlewat karena sistem yang mengingatkan atau melakukannya otomatis
Bisa mengukur dari channel mana leads paling banyak datang dan paling banyak closing
Kinerja tim sales bisa dimonitor dan dioptimalkan berdasarkan data

## 2. Alur Kerja CRM
Dalam bisnis yang menggunakan CRM dengan baik, alurnya berjalan seperti berikut:

| Tahap | Aktivitas | Siapa yang Terlibat |
| --- | --- | --- |
| 1. Lead Masuk | Leads dari berbagai channel tercatat otomatis ke sistem | Sistem (otomatis) |
| 2. Deteksi & Klasifikasi | Sistem mendeteksi source dan memberi kategori (Cold/Warm/Hot) | Sistem (AI) |
| 3. Follow-up Awal | Warm & Hot leads mendapat follow-up otomatis atau manual | Sistem + Sales |
| 4. Nurturing | Cold leads dimasukkan ke drip campaign jangka panjang | Sistem (otomatis) |
| 5. Konversi | Hot leads ditangani langsung oleh sales untuk closing | Sales |
| 6. Retensi | Pelanggan aktif dikelola untuk repeat order dan referral | CS + Marketing |

## 3. Kebutuhan CRM yang Diinginkan
## 3.1 Auto-Detect Kategori Leads
Sistem harus mampu mengklasifikasikan leads secara otomatis ke dalam tiga kategori berdasarkan sinyal perilaku yang terdeteksi:

| Kategori | Sinyal yang Dibaca | Tindakan Otomatis |
| --- | --- | --- |
| Openchat | Pertama kali chat |  |
| Reply | Reply 1x | Masuk drip campaign mingguan |
| ☀ Warm | Reply >1x | Follow-up dalam 24 jam |
| 🔥 Hot | Tanya harga, minta penawaran, sebut 'kapan bisa mulai', tanya schedule | Follow-up dalam 24 jam |

**Sinyal yang perlu dibaca sistem:**
Kata kunci dalam pesan (harga, kapan, mau beli, berapa, bisa mulai)
Frekuensi interaksi (berapa kali membuka email, mengunjungi halaman)
Waktu respons dari leads
Jenis halaman yang dikunjungi (halaman harga = sinyal lebih kuat)
Riwayat interaksi sebelumnya

**Pertanyaan untuk Halo AI:**
Apakah kriteria kategori bisa dikustomisasi sesuai bisnis kami?
Seberapa cepat sistem memperbarui kategori setelah ada sinyal baru?
Apakah ada lead scoring (nilai 0-100) yang bisa dilihat per leads?

## 3.2 Auto-Detect Source Leads
Setiap leads harus otomatis teridentifikasi dari channel mana mereka berasal, tanpa input manual dari tim.

| Source | Cara Deteksi | Informasi yang Dibutuhkan |
| --- | --- | --- |
| WA | Custom message |  |
| IG | Custom message |  |
| ADS | Custom message |  |
| THREADS | Custom message |  |
| FB | Custom message |  |
| TIKTOK | Custom message |  |
| YT | Custom message |  |
| Referral | Custom message |  |

**Pertanyaan untuk Halo AI:**
Channel apa saja yang sudah didukung untuk integrasi otomatis?
Bagaimana cara setup integrasi WhatsApp Business ke CRM?
Apakah bisa membedakan leads dari Instagram Feed vs Instagram Story?

## 3.3 Auto Follow-up
Leads dengan kategori Warm dan Hot harus mendapatkan follow-up otomatis dengan pesan dan timing yang berbeda sesuai kategorinya.

| Kategori | Timing Follow-up | Channel | Jenis Pesan |
| --- | --- | --- | --- |
| Hot | Dalam 24 jam setelah masuk kategori Hot | WhatsApp (prioritas) | Personal, langsung ke penawaran |
| Hot | Jika tidak direspons dalam 24 jam | WhatsApp | Follow-up ke-2, lebih urgensi |
| Warm | D+1 setelah terklasifikasi | WhatsApp | Edukasi produk, manfaat |
| Warm | D+3 | WhatsApp | Social proof, testimoni |
| Warm | D+7 | WhatsApp | Penawaran spesial atau promo |
| Cold | Minggu ke-2 | WhatsApp | Konten edukatif |
| Cold | Minggu ke-4 | WhatsApp | Penawaran ringan / newsletter |

**Pertanyaan untuk Halo AI:**
Apakah template pesan bisa dikustomisasi sendiri?
Bisa set delay/timing follow-up secara fleksibel?
Auto follow-up bisa berhenti otomatis jika leads sudah membalas?
Apakah ada fitur A/B testing untuk template follow-up?

## 4. Fitur Tambahan yang Ingin Dieksplorasi
## 4.1 Alert Eskalasi Manual
Leads Hot yang belum direspons oleh sales dalam waktu tertentu harus memicu notifikasi otomatis ke tim.
Notifikasi via WhatsApp, email, atau in-app ke sales person yang ditunjuk
Bisa set threshold waktu (misal: Hot leads belum direspons > 2 jam = alert)
Eskalasi ke supervisor jika masih belum direspons setelah X jam berikutnya

**Pertanyaan untuk Halo AI:**
Alert bisa dikirim ke nomor WhatsApp personal tim sales?
Bisa assign leads ke sales person tertentu secara otomatis berdasarkan aturan?

## 4.2 Laporan Konversi & ROI per Source
Perlu visibilitas penuh tentang efektivitas setiap channel lead generation.
Berapa leads masuk per channel per periode

Revenue yang dihasilkan per source
Cost per lead jika terintegrasi dengan data iklan

**Pertanyaan untuk Halo AI:**
Dashboard laporan bisa difilter per channel dan per periode?
Data bisa diekspor ke spreadsheet (CSV/Excel)?
Ada laporan funnel drop-off (di tahap mana paling banyak yang tidak lanjut)?

## 4.3 Re-engagement Cold Leads
Leads yang sudah lama tidak aktif bisa diaktifkan kembali saat ada momen yang tepat.
Trigger otomatis saat ada promo baru atau konten relevan
Segment leads berdasarkan berapa lama tidak aktif
Kampanye re-engagement yang berbeda untuk leads 30 hari, 60 hari, 90 hari+

## 4.4 Histori Interaksi Lengkap per Leads
Setiap leads harus memiliki timeline interaksi yang lengkap dan bisa dilihat dalam satu halaman.
Semua percakapan (WhatsApp, email, DM) terekam dan bisa dibaca ulang
Catatan dari sales person bisa ditambahkan manual
Perubahan kategori tercatat dengan timestamp
Riwayat follow-up yang sudah dikirim

## 5. Pertanyaan Kunci untuk Meeting
Gunakan checklist berikut selama meeting dengan Halo AI untuk memastikan semua kebutuhan terjawab.

| No | Pertanyaan | Prioritas |
| --- | --- | --- |
| 1 | Kriteria auto-detect kategori leads (Cold/Warm/Hot) — apakah bisa dikustomisasi? | Tinggi |
| 2 | Channel yang didukung untuk integrasi otomatis (WhatsApp, IG, email, form)? | Tinggi |
| 3 | Auto follow-up tersedia via channel apa — WhatsApp, email, atau keduanya? | Tinggi |
| 4 | Berapa lama delay follow-up setelah leads masuk kategori bisa diatur? | Tinggi |
| 5 | Template pesan bisa dikustomisasi sendiri tanpa bantuan teknis? | Tinggi |
| 6 | Alert eskalasi ke sales jika hot leads belum direspons — tersedia? | Tinggi |
| 7 | Dashboard laporan konversi per channel dan per kategori — bisa diekspor? | Sedang |
| 8 | Lead scoring (nilai numerik) tersedia selain kategori teks? | Sedang |
| 9 | Histori percakapan lengkap per leads bisa dilihat dalam satu halaman? | Sedang |
| 10 | Berapa batas jumlah leads, user, dan kontak dalam paket yang tersedia? | Sedang |
| 11 | Apakah ada masa trial sebelum berlangganan penuh? | Rendah |
| 12 | Dukungan onboarding dan training untuk tim — tersedia? | Rendah |

# 6. Informasi Bisnis untuk Disampaikan
Sampaikan informasi berikut kepada Halo AI agar mereka bisa merekomendasikan setup yang paling sesuai:

_No structured data — see original file_

*Dokumen ini disiapkan sebagai bahan persiapan meeting dengan Halo AI*
Versi 1.0  —  29 Mei 2026
