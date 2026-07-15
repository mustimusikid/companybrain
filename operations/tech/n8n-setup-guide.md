---
title: n8n Setup & Workflow Guide
domain_tag: [operations, tech]
doc_type: sop
owner: tech_head
status: Unknown
confidentiality: Internal
source: gdrive
review_frequency: annually
---

> Panduan setup n8n (cloud/self-hosted/Railway), konsep canvas/node/workflow, kredensial Google & OpenAI, HTTP request/API, dan case study automasi riset video viral (Apify + Google Sheets).

## Setup n8n: Cloud vs Self Hosted (n8n.io)
1. **Cloud** — pakai fitur bawaan, tinggal daftar di n8n.
2. **Self hosted** — tarik kode & fitur n8n, hosting di server lain.
3. **Self hosted local** — di laptop sendiri (laptop tidak boleh shutdown).

**Setup Cloud:** buka n8n.io → Get started, isi data → ingat account name.

## Konsep Dasar
- **Canvas:** latar editor; tombol fit/zoom/tidy, run workflow, tambah node (+), sticky note, "Add first step".
- **Node:** langkah dalam workflow — (a) mengambil, (b) memproses, atau (c) mengirim data.
- **Workflow:** alur kerja otomatis dari beberapa node berurutan (analogi resep masakan). Contoh: Trigger email masuk → cek kata "invoice" → simpan lampiran ke Drive + notif WhatsApp. Manfaat: hemat waktu, kurangi error, banyak use case.
- **Top bar:** Nama Workflow, Tag, Save.

### Kategori Node
AI; In an app; Data transformation; Flow (cek kondisi); Core (teknis/coding); Human in the loop (tunggu feedback); Add another trigger (eksekusi workflow lain / balas berdasarkan isi chat).

### Actions di Node
Eksekusi/play, delete (tong sampah), deactivate (loncat ke flow berikutnya), open (pengaturan), rename, copy, duplicate.

### Export/Import
Export: tombol tiga titik → download (file .json). Import: workflow baru → import workflow → from file → pilih .json → open.

## Setup via Railway (self-host murah)
- Railway: aktifkan website/app, support template n8n, free trial, fee ~$5/bulan (railway.com). Sign in → Continue with GitHub.
- New → Deploy a template → "n8n with worker" → tunggu (all green) → Deploy → project dibuat.
- Pilih primary → klik link → buat akun n8n via link → isi data → started → "send me a free license key" → masukkan kode dari email ke activation key → activate.
- Batas free $5; cek project usage hard limit $5 (bila habis akan mati; berbayar ~$1-2/bulan).
- **GitHub** dipakai sebagai "gdrive khusus code" agar bisa masuk ke Railway (setup: email, username, password, verify).

## Kredensial OpenAI di n8n
- openai.com → login API platform (continue with Google) → dapat API key.
- Start building → isi nama company, non technical → API key name "N8N Key Integration" → copy key (bayar min. $5) → simpan (key hanya tampil sekali).
- n8n → credentials → OpenAI → paste API key → masukkan Organization ID (OpenAI → general) → Save → create workflow → OpenAI node bisa prompt.

## Kredensial Google di n8n
1. console.cloud.google.com → new project (kuota 25 gratis) → nama "N8N integration" → create → select project.
2. APIs & Services → Enable APIs → cari Google Sheets API → Enable.
3. Credentials → OAuth consent screen → Get started → app N8N, email, audience External, contact info → finish.
4. Branding → Add domain → railway.app (atau n8n.cloud jika n8n cloud).
5. Clients → Create client → Web application → Authorized redirect URLs (dari n8n: credentials → Google Sheet → OAuth redirect, copy) → Create → simpan Client ID & Client Secret → masukkan ke n8n.
6. Sign in with Google → continue. Jika diblok: enable Drive API; OAuth consent screen → Audience → Add user (email kamu). Sukses = "connection successful" + akun connected; cek daftar dokumen muncul di node Google Sheet.

## HTTP Request & API
- **API** = "pelayan di restoran" (Application Programming Interface) — cara layanan dipakai program lain.
- **Komponen request:** URL (scheme https, host, port :443, path/endpoint, query parameters); Method (GET=terima, POST=kirim, DELETE, PUT, PATCH); Header (info universal: location, language, device type; mis. `accept: application/json`); Body (hanya untuk POST, berisi data).

## Case Study: Riset Video Viral Otomatis
- **Creator Sheet:** 2 kolom (nama & username creator).
- **Reference Videos Sheet:** ID, Creator, IG reels URL, caption, hashtag, durasi, play count, likes, comment, video URL, thumbnail URL.
- **Prerequisites:** Spreadsheet, Google Sheets API, OpenAI, Railway, GitHub, Apify.
- **Apify** (apify.com, ~$5): ambil data dari berbagai website. Get started → continue with GitHub. Token: Settings → API integration → copy.
- **Workflow:** Create workflow → trigger manual → Google Sheets node "get rows in sheet" → pilih file template & sheet "creators" → run. Tampilan data: Schema/Table/JSON (key=code/id, value=isi).
- **Loop:** node loop (set jumlah; tambahkan "add" di Done untuk aksi setelah selesai; balikkan panah ke loop untuk ulang).
- **HTTP Request:** Apify → Instagram scraper → API endpoints → n8n HTTP request: method GET, URL & token dari Apify, query parameter (token, dataset path tanpa query), Body (cek view API reference, send JSON: `{{$json.username}}`, onlyPostsNewerThan, resultsLimit).
