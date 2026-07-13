---
title: Google Ads SOP
domain_tag: [marketing, ads]
doc_type: sop
owner: marketing_head
status: Approve
confidentiality: Internal
source: gdrive
review_frequency: annually
---

> SOP Google Ads: setup Google Tag Manager untuk tracking konversi, kesalahan umum keyword match type (Broad Match), fundamental (Ad Rank, struktur akun, funnel ToFu/MoFu/BoFu), dan setup Search Campaign.

## Setting Google Tag Manager untuk Tracking Konversi

ini digunakan untuk melakukan tracking konversi, misalnya klik tombol di website agar bisa mengukur efektivitas iklan yang dijalankan

Beberapa hal yang perlu disiapkan :

### Membuat Akun & Container di GTM
Buat Akun
       Pertama buat akun GTM, lalu buat container untuk website Musti Musik
Siapkan Container
       Selanjutnya pada container tersebut nanti akan diletakkan tag-tag, seperti Google Ads, trigger, dll

### Menambahkan Snippet GTM ke Website
Siapkan Snippet
       Setelah container dibuat, perlu menyisipkan dua snippet kode ke website: satu di bagian <head> dan satu di bagian <body> agar GTM bisa aktif di semua halaman.
Install plugin di wordpress
         Sebelum kode dipasang di web, jangan lupa untuk install pluginnya terlebih dahulu
Taruk kode di website
       Setelah itu, kode tidak perlu di edit edit lagi, cukup copy dan paste kode GTM tersebut ke website Musti Musik

### Menyiapkan Konversi di Akun Google Ads
Set up conversion action
       Di Google Ads, buatlah conversion action yang ingin dilacak. dalam kasus studi website Musti Musik yaitu klik tombol "Daftar Sekarang"

Catatan : Dalam setup konversi, akan ada Conversion ID dan Conversion Label. dua data ini penting. dan nantinya akan digunakan di GTM agar konversi tersebut bisa dikaitkan dengan tindakan spesifik

### Membuat Tag Konversi di GTM
Membuat tag
       Di GTM, buatlah tag baru dengan tipe "Google Ads Conversion Tracking". Isikan Conversion ID & Conversion Label yang sudah didapatkan dari Google Ads. Kemudian Pilih trigger yang menentukan kapan tag tersebut harus dijalankan (misalnya saat tombol diklik). Trigger bisa berupa custom event atau pemicu dari data layer.

### Testing & Debugging
Testing
       Setelah setup, gunakan mode Preview / Debug di GTM untuk menguji apakah tag sudah berfungsi dengan benar. Dan cek apakah ketika aksi (klik tombol, submit form) terjadi, tag konversi dikirim dan tercatat. Jika tidak, perlu dicek variabel, trigger, ataupun data layer-nya.

## Kesalahan Umum: Keyword Match Type (Broad Match)

Ketika membuka akun Google Ads, akan ada bagian "Search Keywords". ini adalah daftar kata kunci yang bisa di targetkan. Nah, di sinilah banyak orang melakukan kesalahan. Mereka menggunakan Broad Match, yaitu jenis pencocokan kata kunci paling luas di Google Ads.

### 3 Jenis Match Type di Google Ads

**Broad Match (paling luas)**
Google akan menampilkan iklan untuk banyak pencarian yang menurut algoritma relevan, meskipun sebenarnya tidak terlalu cocok.

**Phrase Match (lebih terarah)**
Kata kunci diapit tanda kutip "...". Google hanya menampilkan iklan kalau pencarian orang masih mengandung frasa tersebut.

**Exact Match (paling spesifik)**
Ditulis dalam tanda kurung siku [ ... ]. Hanya muncul kalau pencarian pengguna benar-benar sama dengan kata kunci.

### Alasan Broad Match Bisa Berbahaya

Dulu, ketika menargetkan kata kunci seperti "guitar lessons near me", iklan hanya muncul kalau orang mengetik hal itu persis. Sekarang, Google pakai sistem "intent" (niat pencarian) Jadi kalau seseorang mencari "piano sheet music", Google bisa menganggap "oh, orang ini mungkin mau belajar piano" lalu menampilkan iklan "piano lessons".

Masalahnya Kalau orang itu hanya ingin mencari lembaran not balok, bukan les piano, maka kita tetap bayar untuk klik yang tidak relevan, dan biaya iklan terbuang.

## Fundamental Google Ads

Tiap platform ads penting untuk manage traffic. Google Ads mencakup Network & YouTube untuk awareness. Karakteristik audiens berbeda per platform — funnel/gameplan bisa dikombinasikan (mis. orang yang sudah lihat YouTube ditarget lagi di GDN dengan sequence video 1→2→3→convert). Targeting lokasi via IP kurang akurat — pakai granularity provinsi. Sebelum jalan Google Ads, tentukan Goals & Metric dulu. Demand Gen Campaign bisa tayang di ~80% inventory Google (Google & YouTube adalah situs paling banyak dikunjungi per 2025).

### Ad Rank & Key Concept
Ad Rank menentukan performa iklan, dipengaruhi 3 faktor:
1. Bid kita vs bid kompetitor.
2. Kualitas Ad/Landing Page & user intent.
3. Ad Rank Threshold (angka minimum agar iklan muncul) & Ad Assets Impact (variasi iklan).

### Landing Page — Kesalahan Umum
Hindari: LP isinya cuma gambar, tidak ada identitas bisnis (who/contact), homepage blank, tidak ada disclaimer (produk herbal/skincare), overclaim, tidak ada navigasi, script aneh, banyak link mati. Google menilai keseluruhan website, bukan cuma halaman iklan — selalu baca Ads Policy. Google Ads Transparency Center bisa untuk lihat iklan kompetitor (tapi tidak bisa lihat LP-nya). Iklan yang disapprove tidak otomatis men-suspend akun.

### Struktur Akun Google Ads
- 1 Gmail = 1 Advertiser (tapi 1 Gmail bisa punya banyak akun Google Ads).
- 1 akun untuk 1 identitas bisnis & 1 domain — jangan 1 domain dipakai 2 akun.
- Masalah akun umum: Payment (kalau suspend, appeal, bisa pakai Gopay), Verifikasi, Suspend.

### Setup Tag & Tracking
Google Ads Conversion, Google Tag Manager, Google Analytics, link YouTube Channel semua perlu di-setup. Remarketing juga bisa menjangkau orang yang akses domain link Meta.

### Struktur Akun (Level)
Level 1 Akun → Level 2 Campaign → Level 3 Ad Group → Level 4 Ads.

### Funnel Google Ads
- **ToFu:** Video, Demand Gen (Video).
- **MoFu:** Search Campaign, Demand Gen (Image).
- **BoFu:** Search Campaign, Shopping Campaign.
- Pemula: mulai dari bawah funnel (BoFu) dulu.
- Campaign lain: Display, Performance Max (PMax — leads bagus tapi kualitas cenderung rendah).

### Setup Search Campaign
1. New Campaign → pilih objective → campaign type Search → masukkan website → pilih bidding.
2. Bidding: kalau budget cukup pilih Maximize Conversion; kalau budget mepet pilih Clicks dengan bid maximum diset manual.
3. Budget awal: mulai dari Rp50rb-100rb.
4. Target lokal: pilih "include people in or regularly in your included locations".
5. Jangan iklan dini hari (~23.00-05.00) — atur jadwal tayang.
6. Buying keywords: pakai Keyword Planner atau logika kata kunci yang biasa dicari konsumen saat sudah ada intensi beli.
7. Display Path: sesuaikan dengan keywords. Isi headline, description, dll — usahakan Ad Strength full bar (pakai semua extension).
8. Call Out Extension: cod, gratis ongkir, harga terjangkau, dll (makin banyak extension, makin besar "real estate" iklan).
9. Location Extension: link Google Business Profile ke akun Google Ads.
10. Setelah Search Campaign jalan, buat Demand Gen dengan data interest dari Search Campaign (catatan: definisi "interest" di Google beda dari Meta — insight Meta belum tentu berlaku).
11. CPAS butuh agensi luar negeri untuk auto purchase.

### Scaling Google Ads
- Naikkan budget bertahap, jangan langsung banyak campaign sekaligus.
- Ad Rank tinggi → CPC lebih rendah.
- Ikuti budget recommendation dari Google Ads (mulai dari rekomendasi paling bawah) selama CPA masih masuk.
- Monitor tiap 3 hari.
- Negative-kan keyword brand di campaign lain yang lebih general untuk hindari ad cannibalism — pastikan target audience antar campaign tidak bentrok.
- Industri F&B secara umum performa lebih baik di Google dibanding Meta.
- Google lebih cocok untuk tujuan jangka panjang. Benchmark CTR Search: ~5%.
