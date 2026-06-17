---
title: SOP Editing & Sinkronisasi MIDI untuk Konten Video Murid Private
domain_tag: [marketing, organic]
doc_type: sop
---

> Proses editing dan sinkronisasi aset MIDI + backing track agar selaras tempo dan dinamika natural, siap dipakai tim video untuk konten murid private.

## Tujuan

Memastikan semua aset audio (MIDI dan *backing track*) untuk konten video murid private selaras secara tempo, memiliki kualitas dinamika (*touching* & *sustain*) yang natural, serta siap digunakan tim video dalam format yang tepat.

## Software / Perangkat

- **Digital Audio Workstation (DAW):** Studio One, Cubase, Reaper, atau DAW sejenis.
- **Virtual Instrument (VSTi):** VST Piano sesuai standar tim.
- **Cloud Storage:** Google Drive.

## Tahap 1: Pengecekan & Persiapan Aset (Pre-Production)

1. **Download Aset:** Download file MIDI mentah yang disediakan tim di Google Drive.
2. **Verifikasi File Pendukung:** Pastikan folder berisi **2 file utama** — file MIDI permainan murid dan file Audio *Backing Track* (BT).
3. **Konfirmasi Masalah:** Jika salah satu file tidak ada, **segera tanyakan dan konfirmasikan** ke tim terkait sebelum mulai editing.

## Tahap 2: Impor & Penyelarasan Tempo di DAW

1. **Impor File:** Buka DAW, impor (*drag & drop*) file MIDI dan *backing track* ke *project window*.
2. **Audio Review Awal:** Dengarkan kedua file bersamaan untuk mendeteksi ketidaksesuaian awal.
3. **Setting Tempo (Matching):** Cari dan tentukan tempo (BPM) dari *backing track* terlebih dahulu. Jika tempo BT berubah, tempo MIDI akan bergeser dan tidak sinkron.
4. **Sinkronisasi MIDI (On-Tempo):** Gunakan **Time Stretch / Audio Bend / Timestretch MIDI** agar panjang dan ketukan MIDI mengikuti tempo BT yang baru. *Opsi lain:* **Quantize** (jika terlalu *off-beat* tapi tetap ingin natural) atau **Snap to Grid** untuk menggeser *notes* manual di *Piano Roll*.

## Tahap 3: Mixing, Editing Dinamika, & VST Tweaking

1. **Balans Level (Gain Staging):** Atur volume di mixer. Suara *backing track* harus **lebih pelan / lebih mundur** dibanding suara permainan piano (MIDI) agar fokus tetap pada permainan murid.
2. **Adjustment Velocity & Sustain:** Buka *Piano Roll*, hubungkan MIDI ke VST Piano:
   - **Sustain Pedal (CC #64):** Rapikan grafik *sustain* agar tidak menggantung (berisik) atau terlalu kering.
   - **Velocity / Touching:** Sesuaikan sensitivitas ketukan tiap notes agar dinamika halus dan natural (tidak seperti robot).

## Tahap 4: Ekspor & Upload (Post-Production)

1. **Review Akhir:** Dengarkan dari awal hingga akhir; pastikan tidak ada *notes* yang *miss*, bocor, atau *out of tempo*.
2. **Bounce / Export File** menjadi 2 file terpisah:
   - **File MP3:** Hasil mixing gabungan (Backing Track + Suara MIDI VST Piano yang matang).
   - **File MIDI Berubah:** Ekspor kembali file MIDI yang sudah direvisi/disinkronkan temponya.
3. **Upload Kembali:** Masukkan kedua file (MP3 + MIDI Revisi) ke folder Google Drive semula agar bisa langsung dieksekusi tim video.

## Indikator Keberhasilan (KPI Editor)

- Audio piano dan *backing track* berada di ketukan yang sama (*perfectly synced*).
- Suara piano murid menonjol namun tetap menyatu natural dengan instrumen pendukung.
- File di Google Drive terorganisir dengan penamaan jelas (Contoh: `Nama Murid_Fixed.mp3` dan `Nama Murid_Fixed.mid`).
