---
title: Tech Documentation
domain_tag: [operations, tech]
doc_type: sop
---

> Technical documentation or automation workflow for Musti Musik systems.

Workflow Automate Resi

Dashboard Pengajaran

Dump
Tentu! Mari kita bedah isi "otak" dari sistem **Content Winning - Lose** yang sudah kita buat.
Sistem ini tidak menggunakan logika IF/ELSE kaku (seperti "Kalau A harus B"), melainkan menggunakan konsep **Weighted Scoring (Penilaian Berbobot)**. Ini mirip seperti sistem penilaian ujian di kampus, di mana nilai akhir adalah gabungan dari nilai UTS, UAS, dan Tugas, dengan persentase kepentingannya masing-masing.
Berikut adalah tahapan logikanya dari awal sampai akhir:
### 1. Filter Awal (Pintu Gerbang)
Sebelum dinilai, setiap baris iklan harus melewati dua syarat ini:
**Hanya yang Active:** Jika statusnya sudah di-*pause* atau *deleted*, iklannya langsung diabaikan.
**Aturan 3 Hari (Learning Phase):** Sistem akan mengecek umur iklan dari kolom Starts. Jika iklan baru berjalan 3 hari atau kurang, sistem tidak akan menilainya dan langsung memberikan cap **⏳ LEARNING**. Tujuannya agar kita tidak keburu "membunuh" iklan yang algoritmanya masih mencari audiens (fase *learning* Meta).
### 2. Penentuan Target KPI (Dinamis)
Karena setiap *campaign* punya harga konversi yang berbeda, sistem akan mendeteksi iklan ini milik siapa (berdasarkan nama file) lalu memasang target **Cost Per Result (CPR)** yang sesuai:
Free Class: Target CPR maksimal Rp 1.500
Masterclass: Target CPR maksimal Rp 50.000
Bootcamp: Target CPR maksimal Rp 120.000
### 3. Pemberian Nilai (Scoring) per Metrik
Jika iklan sudah lewat 3 hari, sistem akan memberikan "Nilai Rapor" (skala 0 - 100) untuk 3 metrik utama. Di sinilah toleransi (kasus mepet) mulai bekerja:
**A. Nilai CPR (Cost Per Result)**
**Dapat nilai 100:** Jika CPR sesuai target atau lebih murah.
**Dapat nilai 60 (Mepet):** Jika CPR agak mahal, batas toleransinya maksimal 30% di atas target (Misal: Target Rp 50rb, tapi realisasinya Rp 60rb).
**Dapat nilai 0:** Jika CPR sangat mahal atau sama sekali belum ada konversi (0 Result).
**B. Nilai CTR (Click-Through Rate)**
**Dapat nilai 100:** Jika CTR $\geq$ 1.0%.
**Dapat nilai 50 (Mepet):** Jika CTR di antara 0.7% sampai 0.99%.
**Dapat nilai 0:** Jika CTR di bawah 0.7%.
**C. Nilai OCLP (Outbound Click Landing Page)**
**Dapat nilai 100:** Jika OCLP $\geq$ 70%.
**Dapat nilai 50 (Mepet):** Jika OCLP di antara 50% sampai 69%.
**Dapat nilai 0:** Jika OCLP di bawah 50%.
### 4. Perhitungan Bobot (Total Skor Akhir)
Setelah ketiga nilai rapor di atas didapatkan, sistem akan mengalikannya dengan bobot prioritas. Di dalam kode yang kita buat, prioritasnya disetting seperti ini:
**CPR adalah Raja (Bobot 50%)**
**CTR adalah Menteri (Bobot 30%)**
**OCLP adalah Prajurit (Bobot 20%)**
**Rumus Skor Akhir:**
(Nilai CPR x 0.50) + (Nilai CTR x 0.30) + (Nilai OCLP x 0.20)
### 5. Pengambilan Keputusan (Stempel Akhir)
Skor akhir (maksimal 100) ini yang akan menentukan nasib iklan:
**🏆 WINNING (Skor 80 - 100):**
Iklan ini performanya sangat bagus secara keseluruhan.
**👀 MONITORING (Skor 50 - 79):**
Ini adalah area abu-abu. Iklan ini punya "penyelamat". Misalnya, CTR-nya jelek banget (nilai 0), tapi entah kenapa CPR-nya sangat murah (nilai 100). Skor totalnya 50. Karena CPR-nya masuk target, mesin tidak akan membunuh iklannya, tapi menyuruhmu untuk mengawasinya.
**❌ KILL (Skor 0 - 49):**
Iklan ini performanya buruk di banyak sisi. Misalnya, CPR mahal (nilai 0) dan CTR jelek (nilai 0). Iklan ini wajib dimatikan karena membakar uang.
**Logika Khusus untuk "Branding"**
Kalau nama filenya "Branding", sistem akan membuang logika CPR/OCLP karena objektifnya bukan konversi, melainkan jangkauan.
Sistem hanya akan menilai **CPM (Bobot 60%)** dan **CTR (Bobot 40%)**. Jika CPM di bawah Rp 1.500 dan CTR di atas 1%, dia langsung jadi WINNING.
Dengan arsitektur ini, kamu punya ruang untuk mengubah kebijakan sewaktu-waktu. Kalau dirasa aturan sekarang terlalu kejam, kamu tinggal menaikkan angka toleransinya di dalam kode tanpa perlu mengubah sisa strukturnya!

—

Pertanyaan yang sangat kritis dan *on-point*! Jawabannya: **TIDAK, evaluasi konten tidak mutlak hanya menggunakan CTR, OCLP, dan CPR.** Namun, ketiga metrik tersebut sering dijadikan **"Holy Trinity" (Tiga Pilar Utama)** dalam mengevaluasi *Creative/Content* karena ketiganya mewakili perjalanan pengguna (*user journey*) dari melihat iklan sampai terjadi konversi.
Mari kita bedah alasan di balik layar (secara logika *media buying*), mengapa 3 metrik itu dipilih, dan apa peran metrik lain yang ada di dalam JSON Anda.
### 1. Mengapa CTR, OCLP, dan CPR Jadi Prioritas?
Ketika kita menilai **Konten/Kreatif** (video/gambar-nya bagus atau tidak), kita harus melihat respon audiens terhadap visual tersebut:
**CTR (Daya Tarik / The Hook):** Mengukur apakah gambar/video Anda berhasil membuat orang *berhenti scroll* dan mengklik. Kalau CTR rendah, berarti visual atau *copywriting*-nya membosankan/tidak relevan.
**OCLP (Kualitas Klik / The Intent):** Mengukur berapa persen orang yang klik *link* dan **benar-benar menunggu *****landing page***** terbuka penuh**. Banyak orang tidak sengaja klik (Fat Finger) atau langsung *close* karena *loading* lama. OCLP > 70% membuktikan bahwa klik yang didapat CTR adalah klik niat, bukan klik nyasar.
**CPR (Hasil Akhir / The Value):** Pada akhirnya, sebagus apapun CTR dan OCLP, kalau audiens tidak beli (konversi mahal), iklannya gagal. CPR memastikan kita mendapat hasil dengan biaya masuk akal.
### 2. Metrik "Harta Karun" Lain di JSON Anda
JSON yang Anda ekstrak menyimpan banyak metrik yang bisa membuat sistem *scoring* Anda jauh lebih tajam. Berikut adalah metrik penting lainnya dan kapan mereka digunakan:
#### A. Results & Amount Spent (Signifikansi Statistik)
**Logika:** Sebuah iklan dengan CPR Rp 10.000 (sangat murah) tapi baru menghasilkan **1 Result** dan baru *spend* Rp 10.000, **belum tentu Winning**. Itu bisa jadi kebetulan (*luck*). Tapi iklan dengan CPR Rp 20.000 yang sudah menghasilkan **50 Results** adalah pemenang sejati.
**Penggunaan:** Sering dijadikan **Syarat Minimal (Threshold)**. Misalnya: *"Iklan baru boleh dinilai WINNING kalau minimal sudah cetak 3 Results atau sudah menghabiskan budget minimal Rp 50.000."*
#### B. Purchase ROAS (Raja E-Commerce)
**Logika:** CPR menghitung *Cost per Result* secara rata. Padahal, ada 1 *Purchase* yang beli paket Rp 50.000, ada 1 *Purchase* yang langsung borong Rp 1.000.000. ROAS (Return on Ad Spend) menangkap nilai ini.
**Penggunaan:** Kadang CPR sedikit mahal (dapat skor jelek), tapi ROAS-nya sangat tinggi (mendatangkan pembeli "Sultan"). ROAS sering dipakai untuk membobol aturan CPR.
#### C. 3-second video plays rate... (Kekuatan Detik Pertama)
**Logika:** Metrik ini sangat spesifik untuk format **Video Ads**. Ini menghitung berapa persen orang yang bertahan menonton 3 detik pertama video Anda dibandingkan total tayangan (*Impressions*).
**Penggunaan:** Kalau 3-second video plays tinggi tapi CTR rendah, artinya *Hook* video Anda di awal sangat memukau, tapi penawarannya (ajakan kliknya) tidak menarik. Ini sinyal untuk tim *Video Editor* merevisi isi videonya, bukan awalnya.
#### D. Checkouts initiated / Adds to cart (Sinyal Mid-Funnel)
**Logika:** Bagaimana kalau sebuah iklan baru jalan 2 hari, belum ada *Results* (Purchase) sama sekali, tapi ternyata yang masukin ke keranjang (*Add to Cart*) sudah banyak?
**Penggunaan:** Metrik ini dipakai sebagai **Indikator Harapan**. Iklan ini jangan buru-buru di-KILL, tapi masuk MONITORING, karena audiensnya sudah punya niat beli tapi mungkin ada masalah di harga ongkir atau halaman *checkout*.
#### E. CPM & Reach (Faktor Eksternal)
**Logika:** CPM (Biaya per 1.000 tayangan) sangat dipengaruhi oleh kompetisi pasar dan lelang audiens (*bidding*), bukan sepenuhnya salah konten.
**Penggunaan:** Kalau CPM tiba-tiba melonjak 3x lipat dibanding biasanya, CPR pasti ikut mahal. Ini jadi bahan analisis apakah target audiensnya sudah jenuh (Audience Fatigue).
### Kesimpulan
Sistem evaluasi **CTR + OCLP + CPR** yang sudah Anda buat adalah fondasi yang **sangat solid dan *****best practice*** untuk mulai mengotomatisasi evaluasi konten. Itu adalah langkah awal yang tepat agar sistem tidak terlalu *over-engineered* dan bingung sendiri.
Apakah ke depannya Anda tertarik untuk memasukkan variabel Results (Signifikansi Statistik) atau ROAS ke dalam formula pembobotan di n8n agar keputusan WIN/KILL-nya lebih akurat lagi?
