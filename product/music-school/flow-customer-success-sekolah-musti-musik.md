---
title: Flow Customer Success Sekolah Musti Musik
domain_tag: [product, music-school]
doc_type: sop
---

> Alur Customer Success murid Sekolah Musti Musik — onboarding murid baru, reminder sesi, reminder pembayaran tiap pertemuan ke-4, hingga info paket & harga, beserta template pesan.

## Flow: Convert (New Student)

1. DM Welcoming + Invite Group (pesan 1)
2. Registrasi Form (pesan 2)
3. Kirim PDF TnC (pesan 3)

## Flow: Student (Berjalan)

1. Reminder setiap H-1 sesi (pesan 4)
2. Tiap pertemuan ke-4: Reminder pembayaran untuk lanjut sesi berikutnya (pesan 5 dan pesan 6 kondisional)
3. Pengiriman info paket dan harga (pesan 7 atau 8)
4. Tracking Resubs di sheets private
5. Jika tidak lanjut: Update data member stop di sheets private
6. NPS/FGD 1 bulan 1x

## Template Pesan

| # | Keterangan | Isi Pesan |
| --- | --- | --- |
| 1 | PC | 🎶 Selamat Datang di Musti Musik! Halo kak [Nama Siswa]! Silahkan bergabung ke group besar Sekolah Musik [LINK] (segera join, link expired dalam beberapa jam). |
| 2 | PC | Untuk melengkapi pendaftaran, mohon isi form registrasi: [Link Form]. Jika ada kendala, hubungi kami. |
| 3 | PC | Terms & Condition (TnC).pdf — di-download dan dikirim. |
| 4 | PC | Reminder H-1 sesi: hari/tanggal, waktu, lokasi/link. Mohon hadir tepat waktu & siapkan alat musik. Jika berhalangan, konfirmasi maks. 24 jam sebelumnya. |
| 5 | PC | Hari ini pertemuan ke-4 (sesi terakhir paket saat ini). Apakah kakak lanjut 1 bulan lagi, atau langsung 3 bulan? |
| 6 | PC (kondisional) | Konfirmasi ingin tetap melanjutkan program Academic/Hobby/Little Worshipper untuk Private/GroupClass seperti sebelumnya, atau berminat program lain. |
| 7 | PC (jika sudah pilih program) | Biaya [Program] sebesar RpXXXXXX, bayar via [Info pembayaran]. Kirim bukti transfer ke nomor ini. |
| 8 | PC | 3 program: 1. Academic (sertifikasi LCM/ABRSM/Rockschool/Trinity) 2. Hobby (main sesuai keinginan) 3. Little Worshipper (anak-anak, lagu worship). |

## Daftar Harga Program

| Program | Harga |
| --- | --- |
| Academic | Rp1.500.000/bulan (private); Rp1.600.000 buddies 2 (Rp800.000/murid); Rp1.700.000 buddies 3 (Rp567.000/murid) |
| Hobby | Rp1.500.000/bulan (private); Rp1.600.000 buddies 2 (Rp800.000/murid); Rp1.700.000 buddies 3 (Rp567.000/murid) |
| Little Worshipper | Rp500.000/anak/bulan |
