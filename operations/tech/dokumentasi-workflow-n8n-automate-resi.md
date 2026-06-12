---
title: Dokumentasi Workflow N8N Automate Resi
domain_tag: [operations, tech]
doc_type: sop
---

> Technical documentation or automation workflow for Musti Musik systems.

**DOKUMENTASI WORKFLOW n8n**
Automate Resi TikTok Shop

| Nama Workflow | My workflow |
| --- | --- |
| Versi | f1c2d082-dfbc-4fa1-b97b-8eabaf9fb507 |
| Status | Tidak Aktif (active: false) |
| Mode Eksekusi | v1 (executionOrder: v1) |
| Mode Binary | Separate |
| Platform | n8n Automation |
| Integrasi | TikTok Shop API, Google Drive, Google Sheets |
| Tanggal Dokumentasi | 19 Mei 2026 |

# 1. Ringkasan Eksekutif
Workflow ini adalah sistem otomatisasi penuh untuk proses pengiriman pesanan dari TikTok Shop. Workflow mencakup dua alur utama yang berjalan secara terjadwal setiap hari, yaitu pembaruan token OAuth TikTok dan proses cetak serta unggah label resi (shipping label) untuk pesanan yang berstatus AWAITING_SHIPMENT.

**Tujuan utama dari workflow ini adalah:**
Memastikan access token TikTok Shop selalu valid melalui proses refresh otomatis setiap hari pukul 11.00 WIB.
Mengambil daftar pesanan yang menunggu pengiriman dari TikTok Shop API setiap hari pukul 12.00 WIB.
Melakukan konfirmasi pengiriman (ship) untuk setiap paket secara otomatis menggunakan metode DROP_OFF.
Mengunduh dan mengorganisir label resi PDF ke Google Drive dengan struktur folder berdasarkan tanggal pickup dan kategori buku (Jazz / Worship / Bundle).
Menyimpan data pembeli ke Google Sheets sebagai rekap order.

# 2. Arsitektur Workflow
Workflow terdiri dari dua alur independen yang dipicu oleh dua Schedule Trigger berbeda:

## 2.1 Alur A — Refresh Token TikTok (Pukul 11.00 WIB)

| Urutan | Node | Deskripsi Singkat |
| --- | --- | --- |
| 1 | Schedule Trigger | Pemicu terjadwal pukul 11.00 setiap hari |
| 2 | Get row(s) | Ambil semua konfigurasi API dari Data Table api_config |
| 3 | Code in JavaScript | Siapkan payload refresh token (app_key, app_secret, refresh_token, grant_type) |
| 4 | HTTP Request | POST ke TikTok OAuth endpoint untuk mendapatkan token baru |
| 5 | Update row(s) | Simpan access_token & refresh_token baru ke Data Table |

## 2.2 Alur B — Cetak & Upload Resi (Pukul 12.00 WIB)
| Urutan | Node | Deskripsi Singkat |
| --- | --- | --- |
| 1 | Schedule Trigger1 | Pemicu terjadwal pukul 12.00 setiap hari |
| 2 | Code in JavaScript6 | Hitung tanggal folder pickup (hari ini / besok jika jam > 12) |
| 3 | Search Main | Cari folder utama di Google Drive berdasarkan nama tanggal |
| 4 | If | Cek: apakah folder sudah ada? |
| 4a (folder ada) | Search Jazz + Search Worship | Temukan subfolder Jazz dan Worship yang sudah ada |
| 4a — lanjut | Edit Fields1 | Simpan ID folder Jazz, Worship, dan Main yang sudah ada |
| 4b (folder baru) | Create Main Folder | Buat folder utama di Google Drive dengan nama 'Pickup DD MMM YYYY' |
| 4b — lanjut | Share folder | Set permission folder: Anyone with link can view (Reader) |
| 4b — lanjut | Create Folder Jazz | Buat subfolder Jazz di dalam folder utama |
| 4b — lanjut | Create Folder Worship | Buat subfolder Worship di dalam folder utama |
| 4b — lanjut | Edit Fields | Simpan ID folder Jazz, Worship, dan Main yang baru dibuat |
| 5 | Get row(s)1 | Ambil konfigurasi API (access_token, app_key, dll) dari Data Table |
| 6 | Code in JavaScript2 | Generate HMAC-SHA256 signature untuk search orders API |
| 7 | HTTP Request1 | POST ke TikTok API: cari pesanan AWAITING_SHIPMENT 7 hari terakhir |
| 8 | if total count > 0 | Cek: apakah ada pesanan? Jika tidak, workflow berhenti (Stop) |
| 9 | Split Out | Pecah array data.orders menjadi item individual |
| 10 | Code in JavaScript3 | Transformasi data: format waktu, kategorisasi buku, tambah cetak_date |
| 11 | Append Order List | Tambahkan data pembeli ke Google Sheets 'DATA PEMBELI BUKU' |
| 12 | Loop Over Items | Loop setiap pesanan satu per satu |
| 13 | Code in JavaScript4 | Generate signature untuk API ship paket |
| 14 | HTTP Request2 | POST ke TikTok API: konfirmasi pengiriman paket (DROP_OFF) |
| 15 | Wait | Jeda sejenak sebelum lanjut ke langkah berikutnya |
| 16 | Code in JavaScript5 | Generate signature untuk API cetak label resi |
| 17 | HTTP Request3 | GET ke TikTok API: ambil URL PDF label resi (A6, SHIPPING_LABEL) |
| 18 | Download PDF | Unduh file PDF resi dari URL yang dikembalikan API |
| 19 | Upload file | Upload PDF ke folder Google Drive sesuai kategori buku |
| 20 | Loop Over Items | Kembali ke item berikutnya atau selesai (Done) |

# 3. Detail Setiap Node
Bagian ini menjelaskan setiap node secara mendalam, termasuk konfigurasi, parameter, dan logika yang diterapkan.

## 3.1 Alur A — Refresh Token TikTok

### Schedule Trigger
| Nama Node | Schedule Trigger |
| --- | --- |
| Tipe Node | n8n-nodes-base.scheduleTrigger |
| Tujuan / Fungsi | Memicu workflow Alur A secara otomatis setiap hari pada jam yang ditentukan. |
| Waktu Pemicu | Pukul 11:00 setiap hari (triggerAtHour: 11) |
| Node ID | 3d623e0c-ee3a-491b-aabd-5d544523160a |

### Get row(s)
| Nama Node | Get row(s) |
| --- | --- |
| Tipe Node | n8n-nodes-base.dataTable |
| Tujuan / Fungsi | Mengambil semua baris dari Data Table bernama 'api_config' yang menyimpan kredensial TikTok API. |
| Data Table ID | 5VZX0uSi5yHlgspW |
| Nama Tabel | api_config |
| Filter | Tidak ada filter — mengambil semua baris |
| Output | Semua kolom: app_key, app_secret, auth_code, grant_type, access_token, refresh_token, shop_cipher |
| Node ID | 4f38d7ff-5f6f-4c28-9e3b-56d88cf1a9ea |

### Code in JavaScript
| Nama Node | Code in JavaScript |
| --- | --- |
| Tipe Node | n8n-nodes-base.code |
| Tujuan / Fungsi | Memformat data dari Data Table menjadi payload yang sesuai dengan format TikTok OAuth untuk proses refresh token. |
| Mode Eksekusi | runOnceForAllItems |
| Node ID | 5875e418-e2a9-4adc-abb0-0af3b3449807 |

**Logika Kode:**
Input  : item.json.app_key, app_secret, refresh_token, id
Output : { payload: { client_key, client_secret, grant_type, refresh_token }, original_row_id }
Logika : Map setiap baris tabel menjadi objek payload + simpan original_row_id untuk referensi update.

### HTTP Request
| Nama Node | HTTP Request |
| --- | --- |
| Tipe Node | n8n-nodes-base.httpRequest |
| Tujuan / Fungsi | Mengirim permintaan ke TikTok OAuth endpoint untuk memperbarui access token menggunakan refresh token. |
| Method | GET (default) |
| URL | https://auth.tiktok-shops.com/api/v2/token/refresh |
| Query Params | app_key, app_secret, refresh_token, grant_type=refresh_token |
| Output | data.access_token, data.refresh_token (token baru) |
| Node ID | 46f98e75-7390-4c16-b41f-e0de8a2eeefc |

### Update row(s)
| Nama Node | Update row(s) |
| --- | --- |
| Tipe Node | n8n-nodes-base.dataTable |
| Tujuan / Fungsi | Menyimpan token baru yang diterima dari TikTok API kembali ke Data Table api_config untuk digunakan pada workflow berikutnya. |
| Data Table ID | 5VZX0uSi5yHlgspW |
| Operasi | Update |
| Kondisi Filter | Mencocokkan baris berdasarkan original_row_id dari node 'Code in JavaScript' |
| Kolom yang Diperbarui | access_token = $json.data.access_token |
|  | refresh_token = $json.data.refresh_token |
| Node ID | 14040f6e-f651-4c44-9110-58d6fcef2410 |

## 3.2 Alur B — Cetak & Upload Resi

### Schedule Trigger1
| Nama Node | Schedule Trigger1 |
| --- | --- |
| Tipe Node | n8n-nodes-base.scheduleTrigger |
| Tujuan / Fungsi | Memicu workflow Alur B secara otomatis setiap hari pada jam yang ditentukan. |
| Waktu Pemicu | Pukul 12:00 setiap hari (triggerAtHour: 12) |
| Node ID | b36fed85-295f-497e-b9a1-dd4de577730a |

### Code in JavaScript6
| Nama Node | Code in JavaScript6 |
| --- | --- |
| Tipe Node | n8n-nodes-base.code |
| Tujuan / Fungsi | Menghitung nama folder Google Drive untuk hari pengiriman (pickup). Jika dijalankan sebelum pukul 12.00 WIB, maka folder diberi nama hari ini; jika setelah pukul 12.00, maka folder diberi nama hari... |
| Mode | runOnceForAllItems |
| Zona Waktu | Asia/Jakarta (WIB) |
| Node ID | af77b81c-1196-47ab-ade1-813591822dd1 |

**Logika Kode:**
Input  : Waktu sistem saat ini
Validasi: if (hour > 12) -> set pickupDate = hari besok
Output :
  main_folder_name : 'Pickup DD MMMM YYYY' (contoh: 'Pickup 19 May 2026')
  jazz_folder      : 'Jazz'
  worship_folder   : 'Worship'
  drop_date        : 'YYYY-MM-DD' (format untuk API)
  current_time     : timestamp saat eksekusi

### Search Main
| Nama Node | Search Main |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Mencari folder utama di Google Drive berdasarkan nama tanggal yang dihitung oleh Code in JavaScript6. Selalu mengeluarkan output meskipun folder tidak ditemukan (alwaysOutputData: true). |
| Operasi | fileFolder — search |
| Query | name = '{main_folder_name}' AND mimeType = folder AND trashed = false |
| Parent Folder | ID: 1fNlks8xJGvMFHs3P8142-nn81GAVWBDL (folder induk di Google Drive) |
| Return All | true |
| Kredensial | Google Drive OAuth2 API |
| Node ID | c94a4a90-b4b7-49ec-9b1f-5d25afe3fc35 |

### If
| Nama Node | If |
| --- | --- |
| Tipe Node | n8n-nodes-base.if |
| Tujuan / Fungsi | Pemeriksaan kondisi: apakah folder utama sudah ada? Jika $json.id tidak kosong, folder sudah ada (jalur true). Jika kosong, folder belum ada dan 0perlu dibuat (jalur false). |
| Kondisi | $json.id is not empty |
| True Branch | Menuju Search Jazz (cari subfolder yang sudah ada) |
| False Branch | Menuju Create Main Folder (buat folder baru) |
| Node ID | 1df1322e-ade9-498b-bde9-bb65e27e3aa6 |

**Jalur True — Folder Sudah Ada:**

### Search Jazz
| Nama Node | Search Jazz |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Mencari subfolder bernama 'Jazz' di dalam folder utama yang sudah ditemukan. |
| Query | 'Jazz' |
| Parent Folder | ID dari Search Main |
| Kredensial | Google Drive OAuth2 API |
| Node ID | 137cb82a-f6af-4f19-bbe0-01ee580344a0 |

### Search Worship
| Nama Node | Search Worship |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Mencari subfolder bernama 'Worship' di dalam folder utama yang sudah ditemukan. |
| Query | 'Worship' |
| Parent Folder | ID dari Search Main |
| Kredensial | Google Drive OAuth2 API |
| Node ID | 98daea34-6e2f-40ad-99e2-89b1dafac409 |

### Edit Fields1
| Nama Node | Edit Fields1 |
| --- | --- |
| Tipe Node | n8n-nodes-base.set |
| Tujuan / Fungsi | Menyimpan ID folder yang sudah ada (main_id, jazz_id, worship_id) ke dalam satu field agar dapat direferensikan oleh node berikutnya. |
| main_id | $node['Search Main'].json.id |
| jazz_id | $node['Search Jazz'].json.id |
| worship_id | $node['Search Worship'].json.id |
| Node ID | 27181a12-528b-4777-8f1a-e8e5eec721db |

**Jalur False — Folder Belum Ada (Buat Baru):**

### Create Main Folder
| Nama Node | Create Main Folder |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Membuat folder utama baru di Google Drive dengan nama yang dihitung oleh Code in JavaScript6. |
| Operasi | folder — create |
| Nama Folder | $node['Code in JavaScript6'].json.main_folder_name |
| Parent Folder ID | 1fNlks8xJGvMFHs3P8142-nn81GAVWBDL |
| Kredensial | Google Drive OAuth2 API |
| Node ID | a0932270-ea75-4625-b498-29a9f8f9a133 |

### Share folder
| Nama Node | Share folder |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Memberikan akses publik ke folder utama yang baru dibuat agar label resi bisa diakses siapa saja melalui link. |
| Operasi | folder — share |
| Role | reader |
| Type | anyone |
| Folder ID | ID dari Create Main Folder |
| Kredensial | Google Drive OAuth2 API |
| Node ID | cf4e50e6-284d-4b28-8e92-da1998bf1a0f |

### Create Folder Jazz
| Nama Node | Create Folder Jazz |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Membuat subfolder bernama 'Jazz' di dalam folder utama yang baru dibuat. |
| Operasi | folder — create |
| Nama Folder | Jazz |
| Parent Folder | ID dari Create Main Folder |
| Node ID | 2211d5bc-7b3f-41bc-ae29-371342330e30 |

### Create Folder Worship
| Nama Node | Create Folder Worship |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Membuat subfolder bernama 'Worship' di dalam folder utama yang baru dibuat. |
| Operasi | folder — create |
| Nama Folder | Worship |
| Parent Folder | ID dari Create Main Folder |
| Node ID | 53cc1548-d565-497a-8cd5-b0ce8416a8de |

### Edit Fields
| Nama Node | Edit Fields |
| --- | --- |
| Tipe Node | n8n-nodes-base.set |
| Tujuan / Fungsi | Menyimpan ID folder yang baru dibuat ke dalam field agar dapat digunakan oleh node Upload file. |
| main_id | $node['Create Main Folder'].json.id |
| jazz_id | $node['Create Folder Jazz'].json.id |
| worship_id | $node['Create Folder Worship'].json.id |
| Node ID | 754d2e7a-895b-4559-8c62-9b5eac98dee7 |

**Lanjutan Alur B — Pengambilan dan Pemrosesan Pesanan:**

### Get row(s)1
| Nama Node | Get row(s)1 |
| --- | --- |
| Tipe Node | n8n-nodes-base.dataTable |
| Tujuan / Fungsi | Mengambil konfigurasi API TikTok terbaru dari Data Table (termasuk access_token yang sudah diperbarui oleh Alur A). |
| Data Table ID | 5VZX0uSi5yHlgspW |
| Filter | Tidak ada — ambil semua baris |
| Node ID | 967f0e00-a630-44b0-8ed0-975895d890c7 |

### Code in JavaScript2
| Nama Node | Code in JavaScript2 |
| --- | --- |
| Tipe Node | n8n-nodes-base.code |
| Tujuan / Fungsi | Menyiapkan request pencarian pesanan ke TikTok API dengan menghasilkan HMAC-SHA256 signature sesuai spesifikasi TikTok. |
| Mode | runOnceForEachItem |
| API Endpoint | /order/202309/orders/search |
| Node ID | db7d8eaa-cede-403f-a54a-a3064726bd6b |

**Logika Kode:**
1. Ambil app_key, app_secret, shop_cipher dari Data Table
2. Set apiPath = '/order/202309/orders/search'
3. Buat timestamp (Unix epoch, detik)
4. Params: app_key, timestamp, shop_cipher, page_size=20, sort_field=create_time, sort_order=DESC
5. Body: order_status=AWAITING_SHIPMENT, create_time_ge=(now-7hari), create_time_lt=now
6. Signature: sort keys A-Z -> concat apiPath+keys+values+JSON.stringify(body)
7. Wrap: appSecret + signString + appSecret -> HMAC-SHA256 hex
Output: { api_path, query_params (dengan sign), body }

### HTTP Request1
| Nama Node | HTTP Request1 |
| --- | --- |
| Tipe Node | n8n-nodes-base.httpRequest |
| Tujuan / Fungsi | Mengirim permintaan POST ke TikTok Shop API untuk mencari pesanan dengan status AWAITING_SHIPMENT dalam 7 hari terakhir. |
| Method | POST |
| URL | https://open-api.tiktokglobalshop.com{api_path} |
| Headers | x-tts-access-token: (dari Get row(s)1), Content-Type: application/json |
| Query Params | query_params dari Code in JavaScript2 (JSON.stringify) |
| Body | JSON.stringify(body) dari Code in JavaScript2 |
| Node ID | 9ee89223-0167-425c-9987-0e1bb5e2fff1 |

### if total count > 0
| Nama Node | if total count > 0 |
| --- | --- |
| Tipe Node | n8n-nodes-base.if |
| Tujuan / Fungsi | Memeriksa apakah ada pesanan yang perlu diproses. Jika tidak ada pesanan, workflow berhenti untuk menghindari error. |
| Kondisi | $json.data.total_count > 0 |
| True Branch | Lanjut ke Split Out (ada pesanan) |
| False Branch | Menuju node Stop (tidak ada pesanan) |
| Node ID | 09e6a74f-78d4-4085-b75c-47a7487aacb0 |

### Stop
| Nama Node | Stop |
| --- | --- |
| Tipe Node | n8n-nodes-base.wait |
| Tujuan / Fungsi | Node penghenti workflow jika tidak ada pesanan baru. Workflow dihentikan dengan bersih tanpa error. |
| Tipe | Wait (digunakan sebagai titik akhir) |
| Node ID | 68836706-faa6-4ff9-87bc-88cd342e6ad4 |

### Split Out
| Nama Node | Split Out |
| --- | --- |
| Tipe Node | n8n-nodes-base.splitOut |
| Tujuan / Fungsi | Memecah array data.orders dari respons API menjadi item-item individual sehingga setiap pesanan dapat diproses satu per satu. |
| Field | data.orders |
| Node ID | 88d1cab8-f5f7-4b5b-825e-c62b80f37080 |

### Code in JavaScript3
| Nama Node | Code in JavaScript3 |
| --- | --- |
| Tipe Node | n8n-nodes-base.code |
| Tujuan / Fungsi | Melakukan transformasi dan pengayaan data untuk setiap pesanan: konversi timestamp, kategorisasi produk berdasarkan nama, dan penambahan tanggal cetak. |
| Mode | runOnceForAllItems |
| Node ID | db02f4c8-96af-4828-b88f-72bb593338e4 |

**Logika Kode:**
1. Format create_time (Unix timestamp) -> 'YYYY-MM-DD HH:MM:SS'
2. Kategorisasi buku berdasarkan nama produk (product_name, uppercase):
   - Mengandung 'JAZZ' dan 'WORSHIP' -> kategori = 'Jazz+Worship'
   - Hanya 'JAZZ'                   -> kategori = 'Jazz'
   - Hanya 'WORSHIP'                -> kategori = 'Worship'
   - Lainnya                        -> kategori = 'Lainnya'
3. Set data.qty = 1
4. Tambahkan cetak_date = tanggal hari ini (WIB, format: DD MMMM YYYY)
Output: data yang sudah diperkaya (formatted_date, custom_category, qty, cetak_date)

### Append Order List
| Nama Node | Append Order List |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleSheets |
| Tujuan / Fungsi | Menambahkan data pembeli dari setiap pesanan ke Google Sheets sebagai rekap/arsip order. |
| Operasi | append |
| Spreadsheet | DATA PEMBELI BUKU (ID: 1SSA_02lnFjvRZdfvj0RQ383AdmcAnw-Yy2mIrWcA5NY) |
| Sheet | OLSHOP (gid: 390655960) |
| Kolom yang Diisi | Nama, no pesanan, WA, Email, Alamat, Paket=Dropoff, Source=Tiktok Shop, Kurir=JnT, Qty=custom_category |
| Kredensial | Google Sheets OAuth2 API |
| Node ID | 1af6805e-da56-4e19-a239-43b1f9d57a16 |

**Lanjutan — Loop Per Pesanan:**

### Loop Over Items
| Nama Node | Loop Over Items |
| --- | --- |
| Tipe Node | n8n-nodes-base.splitInBatches |
| Tujuan / Fungsi | Memproses setiap pesanan satu per satu menggunakan pola loop. Setiap iterasi mengambil satu item (pesanan) dan meneruskannya ke node berikutnya. |
| Tipe | splitInBatches (batch size: 1 per default) |
| Output 0 | Selesai (menuju Done jika tidak ada item lagi) |
| Output 1 | Lanjut proses (menuju Code in JavaScript4 untuk item berikutnya) |
| Node ID | a3ee34d6-f580-48b3-8dab-c21e4339f91e |

### Code in JavaScript4
| Nama Node | Code in JavaScript4 |
| --- | --- |
| Tipe Node | n8n-nodes-base.code |
| Tujuan / Fungsi | Menyiapkan request konfirmasi pengiriman paket (ship) ke TikTok API. Menghasilkan HMAC-SHA256 signature untuk endpoint ship. |
| Mode | runOnceForEachItem |
| Node ID | 4af2af68-29c0-48aa-9423-5f04d5d236c0 |

**Logika Kode:**
1. Ambil packageId = $json['Package ID']
2. Ambil app_key, app_secret, shop_cipher dari Get row(s)1
3. apiPath = '/fulfillment/202309/packages/{packageId}/ship'
4. Params: app_key, timestamp, shop_cipher
5. Body: { handover_method: 'DROP_OFF' }
6. Generate signature: sort params A-Z + concat + body JSON -> HMAC-SHA256
Output: { package_id, api_path, query_params (dengan sign), body }

### HTTP Request2
| Nama Node | HTTP Request2 |
| --- | --- |
| Tipe Node | n8n-nodes-base.httpRequest |
| Tujuan / Fungsi | Mengirim permintaan konfirmasi pengiriman (ship) ke TikTok API untuk setiap paket. |
| Method | POST |
| URL | https://open-api.tiktokglobalshop.com{api_path} |
| Headers | x-tts-access-token, content-type: application/json |
| Body | { handover_method: 'DROP_OFF' } |
| Catatan | Menggunakan metode DROP_OFF — penjual mengantar ke counter JnT |
| Node ID | dd0e22ec-d680-4128-b46c-40b37c6a4cc6 |

### Wait
| Nama Node | Wait |
| --- | --- |
| Tipe Node | n8n-nodes-base.wait |
| Tujuan / Fungsi | Node jeda yang memberikan waktu tunggu setelah konfirmasi pengiriman sebelum memulai proses cetak resi. Digunakan untuk menghindari rate limit TikTok API. |
| Node ID | 5eb46405-e4e7-44fc-90a4-2f93eeb110d0 |

### Code in JavaScript5
| Nama Node | Code in JavaScript5 |
| --- | --- |
| Tipe Node | n8n-nodes-base.code |
| Tujuan / Fungsi | Menyiapkan request untuk mengunduh label resi PDF dari TikTok API. Menghasilkan HMAC-SHA256 signature untuk endpoint shipping_documents. |
| Mode | runOnceForEachItem |
| Node ID | 2c1f2e7d-9c67-45b5-9965-6a4a4ee18d50 |

**Logika Kode:**
1. Ambil packageId dari $node['Loop Over Items'].json['Package ID']
2. Ambil app_key, app_secret, shop_cipher dari Get row(s)1
3. apiPath = '/fulfillment/202309/packages/{packageId}/shipping_documents'
4. Params: app_key, timestamp, shop_cipher,
           document_type=SHIPPING_LABEL, document_size=A6, document_format=PDF
5. Generate signature tanpa body (GET request)
Output: { api_path, query_params (dengan sign) }

### HTTP Request3
| Nama Node | HTTP Request3 |
| --- | --- |
| Tipe Node | n8n-nodes-base.httpRequest |
| Tujuan / Fungsi | Mengambil URL PDF label resi dari TikTok API. |
| Method | GET |
| URL | https://open-api.tiktokglobalshop.com{api_path} |
| Headers | x-tts-access-token, Content-Type: application/json |
| Output | data.doc_url — URL untuk mengunduh PDF |
| Node ID | 96bfa2ec-da82-47eb-81d8-bdc368b187e9 |

### Download PDF
| Nama Node | Download PDF |
| --- | --- |
| Tipe Node | n8n-nodes-base.httpRequest |
| Tujuan / Fungsi | Mengunduh file PDF label resi dari URL yang diberikan oleh HTTP Request3. |
| URL | $json.data.doc_url |
| Response Format | file (binary) |
| Output | File PDF sebagai binary data |
| Node ID | 5f332ffa-8163-435b-8ac0-cb5841c00c87 |

### Upload file
| Nama Node | Upload file |
| --- | --- |
| Tipe Node | n8n-nodes-base.googleDrive |
| Tujuan / Fungsi | Mengunggah file PDF resi ke folder Google Drive yang sesuai berdasarkan kategori buku (Jazz / Worship / Bundle). |
| Operasi | file — upload |
| Nama File | Penamaan otomatis: {KATEGORI}_JNT_{NAMA_PEMBELI}.pdf |
|  | Contoh: JAZZ_JNT_BUDI SANTOSO.pdf |
|  | Jika Jazz+Worship -> nama prefix: BUNDLE_JNT_{nama}.pdf |
| Target Folder Jazz | jazz_id dari Edit Fields1 atau Edit Fields |
| Target Folder Worship | worship_id dari Edit Fields1 atau Edit Fields |
| Target Folder Bundle/Lainnya | main_id (folder utama) |
| Logika Penentuan Folder | Tipe Buku === 'Jazz' -> jazz_id |
|  | Tipe Buku === 'Worship' -> worship_id |
|  | Lainnya (Jazz+Worship/Bundle) -> main_id |
| Kredensial | Google Drive OAuth2 API |
| Node ID | ceea94e2-af1e-45c3-a84f-627077bc9206 |

### Done
| Nama Node | Done |
| --- | --- |
| Tipe Node | n8n-nodes-base.wait |
| Tujuan / Fungsi | Node penanda akhir loop. Workflow dinyatakan selesai ketika semua pesanan telah diproses. |
| Tipe | Wait (digunakan sebagai titik akhir) |
| Node ID | 30db6020-3323-4f78-8f96-3b1bb969580e |

# 4. Struktur Data Table api_config
Data Table api_config (ID: 5VZX0uSi5yHlgspW) merupakan sumber utama konfigurasi yang digunakan oleh kedua alur workflow. Tabel ini berisi kredensial TikTok Shop API yang diperbarui secara otomatis setiap hari oleh Alur A.

| Nama Kolom | Tipe Data | Keterangan |
| --- | --- | --- |
| app_key | string | App Key dari TikTok Shop Partner Center |
| app_secret | string | App Secret untuk signing HMAC-SHA256 |
| auth_code | string | Authorization code (initial setup) |
| grant_type | string | Jenis grant OAuth (refresh_token) |
| access_token | string | Token aktif untuk autentikasi API — diperbarui otomatis tiap hari |
| refresh_token | string | Token untuk memperbarui access_token — diperbarui otomatis tiap hari |
| shop_cipher | string | Identifikasi toko TikTok Shop yang spesifik |

# 5. Struktur Google Sheets — DATA PEMBELI BUKU
Sheet OLSHOP pada Google Sheets berfungsi sebagai database rekap order TikTok Shop. Kolom yang diisi secara otomatis oleh workflow ditandai khusus.

| Nama Kolom | Sumber Data | Keterangan |
| --- | --- | --- |
| Nama | API TikTok | recipient_address.name — nama penerima |
| no pesanan | API TikTok | order.id — nomor pesanan unik |
| WA | API TikTok | recipient_address.phone_number |
| Email | API TikTok | buyer_email |
| Alamat | API TikTok | recipient_address.full_address |
| Paket | Hardcoded | Selalu: 'Dropoff' |
| Source | Hardcoded | Selalu: 'Tiktok Shop' |
| Kurir | Hardcoded | Selalu: 'JnT' |
| Qty | Computed | custom_category dari Code in JavaScript3 (Jazz/Worship/Jazz+Worship/Lainnya) |
| Nomor Resi | Manual | Diisi manual setelah pengiriman |
| File Resi | Manual | Link Google Drive ke PDF resi |

# 6. Struktur Folder Google Drive
Semua label resi PDF disimpan dalam struktur folder yang terorganisir berdasarkan tanggal pickup dan kategori buku:

| Path Folder | Konten |
| --- | --- |
| [Root] / Pickup DD MMM YYYY / | Folder utama per hari pickup |
| [Root] / Pickup DD MMM YYYY / Jazz / | Label resi PDF untuk buku Jazz saja |
| [Root] / Pickup DD MMM YYYY / Worship / | Label resi PDF untuk buku Worship saja |
| [Root] / Pickup DD MMM YYYY / (root folder) | PDF untuk Bundle (Jazz+Worship) atau Lainnya |

**Format Nama File PDF:**
{KATEGORI}_JNT_{NAMA_PEMBELI}.pdf
Contoh untuk Jazz: JAZZ_JNT_BUDI SANTOSO.pdf
Contoh untuk Worship: WORSHIP_JNT_SITI RAHAYU.pdf
Contoh untuk Bundle: BUNDLE_JNT_AHMAD FAUZI.pdf
Karakter non-alphanumeric pada nama pembeli akan dihapus otomatis

# 7. Mekanisme Signing TikTok API (HMAC-SHA256)
Seluruh request ke TikTok Open API menggunakan mekanisme signing HMAC-SHA256. Algoritma ini diterapkan secara konsisten di tiga node kode (Code2, Code4, Code5).

**Langkah-langkah Pembuatan Signature:**
Kumpulkan semua query parameter kecuali 'access_token' dan 'sign'.
Urutkan key parameter secara alfabetis (A-Z).
Buat string: apiPath + concat(key+value) untuk setiap parameter yang sudah diurutkan.
Jika ada body request, tambahkan JSON.stringify(body) di akhir string.
Bungkus dengan app_secret: appSecret + signString + appSecret.
Hitung HMAC-SHA256 dari string final menggunakan app_secret sebagai kunci.
Tambahkan nilai hex signature sebagai parameter 'sign' pada query.

**Contoh Pseudocode:**
sortedKeys = sort(Object.keys(params).filter(k => k != 'sign' && k != 'access_token'))
signString = apiPath + sortedKeys.map(k => k+params[k]).join('') + JSON.stringify(body)
wrapped   = appSecret + signString + appSecret
signature = HMAC-SHA256(wrapped, key=appSecret).hex

# 8. Layanan Eksternal & Kredensial
| Layanan | Tipe Kredensial | Penggunaan |
| --- | --- | --- |
| TikTok Shop API | Stored in Data Table | OAuth token refresh, search orders, ship package, cetak resi |
| Google Drive | OAuth2 API | Buat folder, share folder, upload PDF resi |
| Google Sheets | OAuth2 API | Append data pembeli ke sheet OLSHOP |
| n8n Data Table | n8n Built-in | Penyimpanan konfigurasi API (api_config) |

# 9. TikTok API Endpoint yang Digunakan
| Method | Endpoint | Fungsi |
| --- | --- | --- |
| GET | https://auth.tiktok-shops.com/api/v2/token/refresh | Refresh OAuth access token |
| POST | https://open-api.tiktokglobalshop.com/order/202309/orders/search | Cari pesanan AWAITING_SHIPMENT |
| POST | https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/{id}/ship | Konfirmasi pengiriman paket |
| GET | https://open-api.tiktokglobalshop.com/fulfillment/202309/packages/{id}/shipping_documents | Ambil URL PDF label resi |
| GET | (URL dari doc_url) | Download file PDF resi |

# 10. Catatan Penting & Pertimbangan Operasional
## 10.1 Urutan Eksekusi
Alur A (refresh token, pukul 11.00) harus selesai sebelum Alur B (cetak resi, pukul 12.00) dimulai. Jeda 1 jam memberikan waktu yang cukup untuk memastikan access_token di Data Table sudah diperbarui saat Alur B berjalan.

## 10.2 Logika Tanggal Pickup
Node Code in JavaScript6 menerapkan validasi SOP: jika workflow dijalankan setelah pukul 12.00 WIB, maka tanggal pickup otomatis digeser ke hari berikutnya. Hal ini mencerminkan batas waktu drop-off di counter kurir.

## 10.3 Penanganan Folder yang Sudah Ada
Workflow tidak akan membuat folder duplikat. Jika folder untuk tanggal pickup sudah ada (misalnya workflow dijalankan ulang di hari yang sama), node Search Main akan menemukannya, If akan mengarahkan ke jalur true, dan subfolder yang sudah ada akan dicari melalui Search Jazz dan Search Worship.

## 10.4 Rate Limiting
Node Wait ditempatkan setelah HTTP Request2 (konfirmasi ship) sebagai jeda sebelum request cetak resi. Ini membantu menghindari rate limit TikTok API ketika memproses banyak pesanan dalam satu waktu.

## 10.5 Status Workflow
Workflow saat ini dalam status tidak aktif (active: false). Workflow perlu diaktifkan secara manual melalui dashboard n8n agar berjalan sesuai jadwal.

## 10.6 Kategori Buku
Sistem kategorisasi buku didasarkan pada nama produk TikTok. Kategori 'Jazz+Worship' (bundle) menggunakan prefix 'BUNDLE' pada nama file PDF dan ditempatkan di folder utama (bukan subfolder Jazz atau Worship).

# 11. Ringkasan Semua Node
| Nama Node | Tipe | Fungsi Ringkas |
| --- | --- | --- |
| Schedule Trigger | scheduleTrigger | Pemicu Alur A pukul 11:00 |
| Get row(s) | dataTable | Ambil konfigurasi API dari Data Table |
| Code in JavaScript | code | Siapkan payload refresh token |
| HTTP Request | httpRequest | Refresh token ke TikTok OAuth |
| Update row(s) | dataTable | Simpan token baru ke Data Table |
| Schedule Trigger1 | scheduleTrigger | Pemicu Alur B pukul 12:00 |
| Code in JavaScript6 | code | Hitung nama folder/tanggal pickup |
| Search Main | googleDrive | Cari folder utama di Drive |
| If | if | Folder sudah ada atau perlu dibuat? |
| Search Jazz | googleDrive | Cari subfolder Jazz |
| Search Worship | googleDrive | Cari subfolder Worship |
| Edit Fields1 | set | Simpan ID folder yang sudah ada |
| Create Main Folder | googleDrive | Buat folder utama baru |
| Share folder | googleDrive | Set permission publik (reader: anyone) |
| Create Folder Jazz | googleDrive | Buat subfolder Jazz |
| Create Folder Worship | googleDrive | Buat subfolder Worship |
| Edit Fields | set | Simpan ID folder baru |
| Get row(s)1 | dataTable | Ambil konfigurasi API terbaru |
| Code in JavaScript2 | code | Generate signature pencarian pesanan |
| HTTP Request1 | httpRequest | Cari pesanan AWAITING_SHIPMENT |
| if total count > 0 | if | Ada pesanan? Ya lanjut / Tidak berhenti |
| Stop | wait | Hentikan jika tidak ada pesanan |
| Split Out | splitOut | Pecah array pesanan jadi item individual |
| Code in JavaScript3 | code | Transformasi data + kategorisasi buku |
| Append Order List | googleSheets | Simpan data pembeli ke Google Sheets |
| Loop Over Items | splitInBatches | Loop per pesanan satu per satu |
| Code in JavaScript4 | code | Generate signature konfirmasi ship |
| HTTP Request2 | httpRequest | Konfirmasi pengiriman (DROP_OFF) |
| Wait | wait | Jeda setelah konfirmasi ship |
| Code in JavaScript5 | code | Generate signature unduh label resi |
| HTTP Request3 | httpRequest | Ambil URL PDF label resi |
| Download PDF | httpRequest | Unduh file PDF dari URL |
| Upload file | googleDrive | Upload PDF ke folder sesuai kategori |
| Done | wait | Penanda akhir loop |
