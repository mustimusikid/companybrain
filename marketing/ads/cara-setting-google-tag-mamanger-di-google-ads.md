---
title: Cara Setting Google Tag Mamanger Di Google Ads
domain_tag: [marketing, ads]
doc_type: sop
---

> Marketing strategy, ad script, or content SOP for Musti Musik.

**Cara Setting Google Tag Mananger Di Google Ads**

ini digunakan untuk melakukan tracking konversi, misalnya klik tombol di website agar bisa mengukur efektivitas iklan yang dijalankan

Beberapa hal yang perlu disiapkan :
**Membuat Akun & Container di GTM**
Buat Akun
       Pertama buat akun GTM, lalu buat container untuk website Musti Musik
Siapkan Container
       Selanjutnya pada container tersebut nanti akan diletakkan tag-tag, seperti Google Ads, trigger, dll

**Menambahkan Snippet GTM ke Website**
Siapkan Snippet
       Setelah container dibuat, perlu menyisipkan dua snippet kode ke website: satu di bagian <head> dan satu di bagian <body> agar GTM bisa aktif di semua halaman.
Install plugin di wordpress
         Sebelum kode dipasang di web, jangan lupa untuk install pluginnya terlebih dahulu
Taruk kode di website
       Setelah itu, kode tidak perlu di edit edit lagi, cukup copy dan paste kode GTM tersebut ke website Musti Musik

**Menyiapkan Konversi di Akun Google Ads**
Set up conversion action
       Di Google Ads, buatlah conversion action yang ingin dilacak. dalam kasus studi website Musti Musik yaitu klik tombol “Daftar Sekarang”

Catatan : Dalam setup konversi, akan ada Conversion ID dan Conversion Label. dua data ini penting. dan nantinya akan digunakan di GTM agar konversi tersebut bisa dikaitkan dengan tindakan spesifik

**Membuat Tag Konversi di GTM**
Membuat tag
       Di GTM, buatlah tag baru dengan tipe “Google Ads Conversion Tracking”. Isikan Conversion ID & Conversion Label yang sudah didapatkan dari Google Ads. Kemudian Pilih trigger yang menentukan kapan tag tersebut harus dijalankan (misalnya saat tombol diklik). Trigger bisa berupa custom event atau pemicu dari data layer.

**Testing & Debugging**
Testing
       Setelah setup, gunakan mode Preview / Debug di GTM untuk menguji apakah tag sudah berfungsi dengan benar. Dan cek apakah ketika aksi (klik tombol, submit form) terjadi, tag konversi dikirim dan tercatat. Jika tidak, perlu dicek variabel, trigger, ataupun data layer-nya.
