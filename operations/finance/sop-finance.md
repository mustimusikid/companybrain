---
title: Sop Finance
domain_tag: [operations, finance]
doc_type: sop
owner: finance_head
status: Approve
confidentiality: Internal
source: gdrive
effective_date:
review_frequency: quarterly
superseded_by:
---

> SOP finance operasional — input mutasi bank & source revenue, perhitungan Churn/ARPU/LTGP/CAC, pencatatan personal Dave, proses payroll/salary, dan pelaporan pajak (PPh21, PPh23, Pajak Omzet Bruto).

**SOP FINANCE**

## SOP 1: Bank MM dan Sumber Revenue
Mengambil mutasi rekening dari Kak Dian.
Menginput seluruh mutasi rekening MM ke dalam sheet Bank MM dengan menyesuaikan:
Tanggal
COA
Nama COA
Nomor Voucher
Debit
Credit
Balance
Memastikan seluruh saldo sesuai dan balance akhir cocok dengan rekening bank.

Untuk setiap transaksi revenue atau pendapatan:
Menginput ke sheet Source Revenue.
Menentukan:
Source
Funnel
Event
Keterangan
dan informasi pendukung lainnya.

Untuk setiap transaksi expense:
Menginput ke sheet Kredit 2026 dengan menyesuaikan:
Tanggal
COA
Nama COA
Nomor Voucher
Keterangan
Jumlah
dan data terkait lainnya.
Untuk setiap perpindahan uang pada Source Revenue:
Menginput total nominal sesuai data Excel dari Kak Dian termasuk ongkos kirim (ongkir).

	-Setelah semua selesai reporting ke Kak Dian dengan format.
Daily Report
dd/mm/yyyy
Saldo Awal: …
Kas Masuk: …
Kas Keluar: …
Saldo Akhir: …
Total Monthly Revenue: total debit di bank mm =sum(semua)

## SOP 2: Churn, LTGP, ARPU, Data Recog

### Churn
Churn private dan akademi : input semua murid yang ikut dalam bulan tersebut ke dalam sheets churn lalu bikin kolom baru diujung untuk menghitung churn atau tidak. Jadwal yang sudah ada sampai akhir ditulis jika tidak ditulis masukin date dari excel ditambah berapa bulan mereka ikut.
	-Setelah itu, lihat di sheets churn masing masing di paling kanan masukin jumlah murid, churn, murid baru dan akan dapat jumlah churn.

### ARPU
Arpu akademi lihat yang source data recog lalu ambil yang atas yang bagian akademik lifetime, 12, 9, 6, 3 bulan lalu bagi dengan total customer akademi.
	-Arpu private lihat yang source data recog lalu ambil yang bagian private class revenue dan bagi dengan total customer private.

### LTGP
Ltgp akademi kita bagi arpu akademi dengan churn akademi bulan itu lalu kali dengan 100%.
	-Ltgp private kita bagi arpu private dengan churn private bulan itu lalu kali dengan 100%.

### CAC
CAC akademi kita tambahin semua gaji lila dan anis lalu tambah advertising expense baru kita bagi total kustomer akademi.
CAC private kita tambahin semua gaji lila dan anis lalu tambah advertising expense baru kita bagi total kustomer private.
CAC keseluruhan kustomer kita tambahin semua gaji lila dan anis lalu tambah advertising expense baru kita bagi total kustomer private dan akademi.

### Data Recog
Data recog saat ini masih memasukkan seluruh sumber revenue kepada kita punya kepada source data recog.

## SOP 3: Personal Dave
Setiap transaksi expense dan income diinput ke dalam Input Transaksi dengan menyesuaikan:
Tanggal
Akun
Kategori
Sub-kategori
Catatan
Jumlah
Jika kategori belum tersedia:
Menambahkan kategori baru pada bagian “Mulai di sini yuk”.
Untuk perpindahan antar rekening:
Contoh BCA ke BRI:
BCA dicatat sebagai uang keluar
BRI dicatat sebagai uang masuk
Nominal harus sesuai.

## SOP 4: Salary
Mengambil data gaji pokok masing-masing pegawai.
Menambahkan:
reimburse
tambahan gaji
bonus
dan komponen tambahan lainnya.
Mengurangi:
keterlambatan
potongan
atau penalti lainnya.
Untuk pegawai yang masuk atau keluar di tengah bulan:
Gaji dihitung secara prorata.
Contoh:
Jika masuk tanggal 10,
maka perhitungan: 10/30 × Gaji Pokok
Setelah seluruh perhitungan selesai:
Melakukan konfirmasi kepada Kak Dian bahwa salary sudah benar dan siap dibayarkan.

## SOP 5: Pelaporan Salary dan Tax Revenue

### PPh21
Mengambil data salary dari MM-HR.
Menginput data ke subsheet Salary PPh21:
Nama
NPWP
Jumlah gaji
Membuka Coretax dan masuk ke E-Bupot.
Menginput:
NPWP
Deskripsi pembayaran:
Gaji Bulanan Pegawai Tidak Tetap
Menerbitkan E-Bupot.
Setelah E-Bupot selesai:
Membuat SPT PPh21.
Menerbitkan SPT agar pajak terlapor.

### PPh23
Untuk setiap transaksi jasa dari badan ke badan:
Membuat BPPU.
Menginput:
NPWP perusahaan terkait
Jumlah penuh transaksi
Melakukan pembayaran pajak.
Menerbitkan SPT.

### Pajak Omzet Bruto
Mengambil total debit dari Bank MM.
Menghitung pajak dengan formula: total atau =sum debit kali 0.5%
Laporkan dalam spt dan bayar lalu sudah jadi.
