---
title: LLM Prompting & n8n Basics
domain_tag: [operations, tech]
doc_type: reference
owner: tech_head
status: Draft
confidentiality: Internal
source: gdrive
review_frequency: evergreen
---

> Catatan dasar cara kerja Large Language Model, teknik prompting (Role/Context/Action/Output Format/Data), dan pengenalan UI n8n (Canvas, Node, Workflow). Sebelumnya tercampur di file marketing/ads/performance-marketing.md — dipindah karena tidak berhubungan dengan ads.

## Fitur ChatGPT

**Apa yang bisa dilakukan ChatGPT:** tulis/edit teks, buat gambar & ide konten, koding & bantuan programming, analisis data & visualisasi, simulasi percakapan/roleplay. ChatGPT tidak "berpikir" tapi memprediksi respons berdasarkan data yang sudah dilatih.

- **Memory:** Settings → Personalization → Memory (bisa on/off, ada batasnya). Lihat/kelola via "Manage Memories" — bisa delete/tambah manual (mis. "tolong ingat hal ini"). Fungsi: mengingat konteks untuk pertanyaan serupa di masa depan.
- **Temporary Chat:** chat yang tidak masuk riwayat/history/memory — bagus untuk testing apakah prompt sudah bagus.
- **Custom Instructions:** Settings → Personalization → Custom Instruction. Simpan preferensi (nickname, dll), diprioritaskan di atas memory. Hanya 1 persona, ada batas panjang instruksi.
- **Projects:** buat folder di sidebar kiri untuk lebih terorganisir — bisa tambah instruksi & prompt spesifik per folder.
- **Tasks:** minta ChatGPT lakukan sesuatu di masa depan tanpa perlu ngetik ulang (mis. reminder ulang tahun + ide konten tiap pagi).
- **CustomGPT** (khusus paket berbayar): buat GPT custom via "My GPTs" — tab Create (upload info yang ingin di-referensi AI) dan tab Configure. Bisa dibagikan via link atau dijual.

## Apa Itu Large Language Model?
**Large Language Model (LLM)** adalah sebuah **mesin pintar yang dilatih untuk memahami dan menghasilkan bahasa manusia**.
Atau
**“otak buatan”** RAKSASA yang dilatih dari miliaran teks, supaya bisa memahami dan menghasilkan bahasa manusia dengan cara yang sangat natural.

Disebut *large* karena model ini:
Dilatih dari **data teks dalam jumlah sangat besar** (internet, buku, artikel, percakapan, dll)
Memiliki **parameter dalam jumlah ratusan miliar**, yaitu "aturan tersembunyi" yang dipelajarinya
Model ini bisa:
Menjawab pertanyaan
Menulis artikel
Bikin puisi, skrip, email, kode, dan banyak lagi

### Analogi
Bayangkan ada seseorang (sebut saja AI) yang:
Sudah **membaca ratusan juta buku, blog, email, tweet**
Belajar dari semua itu, lalu **bisa menebak kata selanjutnya dalam sebuah kalimat**
Jadi saat kamu nanya: *"Gimana cara mulai bisnis F&B?"*, dia bisa jawab karena dia **sudah melihat ribuan pertanyaan serupa** dan tahu pola jawaban terbaik.

### Bagaimana Cara Kerjanya?
### Belajar dari Data
Dia belajar dari teks-teks yang sudah ada (misalnya dari Wikipedia, Reddit, buku, dll)
### Pahami Pola Bahasa
Dia pelajari: “Kalau ada kata X, biasanya diikuti kata Y”
### Prediksi Kata Selanjutnya
Saat kamu mengetik sesuatu, dia **memprediksi token demi token** untuk melanjutkan kalimat kamu sebaik mungkin.
### KOMPONEN 1: PARAMETERS
Parameter = aturan-aturan kecil yang dipakai AI untuk belajar sebuah pola baru
Di LLM, parameter digunakan untuk **menentukan kata apa yang paling cocok muncul setelah kata sebelumnya**, berdasarkan jutaan contoh dari internet, buku, artikel, dan percakapan.

### KOMPONEN 2:  TOKENS
Token = potongan kecil dari teks
Satu kata bisa jadi 1 token atau 2 token kalau panjang/tidak umum
LLM dihitung dan dibatasi berdasarkan token
Kalau kita tulis teks panjang banget, model akan berhenti ketika tokennya penuh

### KOMPONEN 3: TOKENS EMBEDDINGS
Token embeddings = cara mengubah tiap token jadi angka2 yang bermakna supaya bisa diproses oleh model

### KOMPONEN 4: CONTEXT WINDOWS
Batas seberapa banyak token yang bisa diingat dan diproses oleh model dalam 1 kali percakapan atau input
### Seberapa Besar Context Window?
Model seperti **GPT-3.5**: ~4.000 token
**GPT-4**: Bisa sampai 8.000, 32.000, bahkan 128.000 token tergantung versi
1.000 token ≈ sekitar 750 kata bahasa Indonesia
Kalau kamu nulis terlalu panjang dan melewati batas token, maka:
### Teks paling awal akan “tergeser keluar”
Model akan mulai lupa bagian awal karena sudah di luar jangkauan window
 → untuk cek seberapa besar context window masing2 model

LLM “belajar” dengan cara **membaca miliaran kata** dari internet — seperti buku, artikel, website, percakapan, dll.
Tapi dia **nggak belajar makna secara manusiawi**, melainkan dia belajar:
“Kalau ada kata A, biasanya diikuti kata B.”
Misalnya:
Lihat sering ada “makan nasi goreng”
Maka dia belajar bahwa “nasi goreng” sering muncul setelah “makan”
### 2. Belajar Menebak Kata Selanjutnya
Latihannya itu kayak main tebak-tebakan:
**Input:** “Saya suka makan…”
**Tugas LLM:** Tebak kata selanjutnya → “bakso” (misalnya)
Kalau tebakannya salah, dia dikasih tahu, dan dia **perbaiki cara berpikirnya sedikit**. Ini dilakukan **jutaan kali**, sampai dia jadi pintar menebak kata demi kata.
### 3. Semua Pola Disimpan Jadi Angka (Parameter)
Selama belajar, LLM menyimpan hasil belajarnya dalam bentuk angka-angka khusus yang disebut **parameter** — semacam "aturan tersembunyi" tentang bahasa.
Semakin banyak dia belajar, **semakin banyak parameternya**, dan **semakin pintar** dia dalam memahami konteks dan menjawab pertanyaan.
### Singkatnya:
LLM belajar dengan **membaca banyak teks**,
lalu **berlatih menebak kata selanjutnya**,
dan **menyimpan pola-pola itu dalam bentuk angka
**supaya bisa menjawab atau menulis seperti manusia.
Prompt Engineering
### STRUKTUR PROMPT YANG BAIK
Role > Context > Action > Output Format > Data
## 1. Role – "Lo mau dia jadi siapa?"
Kamu perlu kasih tahu AI-nya dia berperan sebagai siapa.
🔍 **Kenapa penting?
**Karena AI bisa menyesuaikan gaya dan sudut pandang sesuai peran.
📌 Contoh:
*“Kamu adalah seorang content creator.”
*Kalau kamu tulis seperti itu, AI akan menjawab dengan sudut pandang seorang content creator, bukan dosen atau programmer.

## 2. Context – "Apa hal yang dia perlu tahu dulu?"
Kamu perlu kasih **latar belakang atau info penting** sebelum kasih tugas ke AI.
🔍 **Kenapa penting?
**Tanpa konteks, jawabannya bisa ngawur atau terlalu umum.
📌 Contoh:
*“Kamu bikin konten tentang AI.”
*Ini kasih gambaran topik besar yang akan dibahas.

## 3. Action – "Lo mau dia ngelakuin apa?"
Perintah spesifik tentang **apa yang harus dilakukan oleh AI**.
🔍 **Kenapa penting?
**Tanpa action yang jelas, AI bisa bingung harus ngapain.
📌 Contoh:
*“Cari 5 ide konten tentang penerapan AI dalam bikin konten.”*

## 4. Output Format – "Lo mau jawabannya kayak gimana bentuknya?"
Tentukan bentuk jawaban: apakah **bullet points**, **tabel**, atau **list**.
🔍 **Kenapa penting?
**Supaya hasilnya **rapi, mudah dibaca, dan langsung bisa dipakai**.
📌 Contoh:
*“Bullet points / table / list”*

## 5. Data – "Lo punya contoh buat dia belajar nggak?"
Kalau ada **contoh atau referensi**, kasih ke AI supaya hasilnya lebih akurat.
🔍 **Kenapa penting?
**Contoh bikin AI ngerti gaya dan isi yang kamu harapkan.
📌 Contoh:
*“Contoh konten AI yang sudah pernah aku buat adalah berikut ini: Ide 1, Ide 2.”*

### TECHNIQUES

### TEKNIK 1: KLARIFIKASI SEBELUM MENJAWAB
Berikan saya beberapa pertanyaan terlebih dahulu sebelum kamu menjawab → powerful to use when you don’t know what kind of context you need to give to them

### TEKNIK 2: CARA JAWAB PERTANYAAN KLARIFIKASI
If u know the answer secara pasti → jawab secara sekaligus
But if u don’t → jawab satu2

### TEKNIK 3: TEKNIK VERIFIKASI
Sebelum kamu melanjutkan, tolong jelaskan x kita

### TEKNIK 4: CONTINUE OR REGENERATE
If AI understands: Oke ini sudah benar lanjutkan ke nomor 2
If AI don’t understands: Regenerate ulang → klik edit di prompt kita sampe dia ngerti

### TEKNIK 5: REASONING
Kalau kamu udah ngedit promptnya tp masih salah → edit prompt: tolong lakukan secara step by step dan alasan ringkas dari setiap langkahnya

### DELEGATE THE CONVOS TO CHATGPT
Edit promptnya: tolong sekaligus pimpin diskusi ini dan berikan pertanyaan dan pernyataan lanjutan setiap jawaban akhir kamu
GENERATIVE AI
This is still parts of AI Module, however it is more into Generative AI
Fundamentals
LEVEL 1 GENERATIVE AI
LEVEL 2 AI WORKFLOW
LEVEL 3 AI AGENT
LEVEL 4 MULTI AGENT SYSTEM

### GENERATIVE AI
Fokus: from input to generate output
Characteristics:
Stateless interaction
No memory between sessions
Human initiated tasks only
Example: gpt, gemini, etc
When to use?
Mau hasilnya cepet
TOOLS MASTERY (that we need to know)
Text to image: nano banana, mid journey
Text to vid: sora ai, veo3, fliki ai
Image to image: gemini
Image to vid: gemini, klingeye
Vid to vid: runway, luma labs, kling, one
Text to sound: suno, 11 labs

Heygen AI
The tools
![image333.png](PERFORMANCE MARKETING _images/image333.png)
Cara Pilih Tools
Cek token: tokenizer web
Claude → brainstorm
GPT → cepet
Image → open AI 1.5
Nano banana pro
Cek berdasarkan
Commercial → flux
Prompting AI Generative

IMAGE VIDEO GEN BASIC PROMPT
Style: realistis, kartun, pixar, disney
Subject: kucing, orang, dll
Action: duduk, dll
Environment: tepi sungai

IMAGE VIDEO GEN PRO PROMPT GUIDE (7 gold rule)
Aspect ratio
![image331.png](PERFORMANCE MARKETING _images/image331.png)
Shot type
Use as much as you can
Extreme long shot
Very long shot
Mid shot
Medium long shot
Long shot
Medium closeup
Closeup
Extreme closeup
Camera & lens (kit + angle)
![image330.png](PERFORMANCE MARKETING _images/image330.png)
Camera type: cctv? Gopro? Etc
![image329.png](PERFORMANCE MARKETING _images/image329.png)
Character control
Emotion control
![image364.png](PERFORMANCE MARKETING _images/image364.png)
Direction control
![image363.png](PERFORMANCE MARKETING _images/image363.png)
Body Pose
Light control
![image362.png](PERFORMANCE MARKETING _images/image362.png)
Composition
![image358.png](PERFORMANCE MARKETING _images/image358.png)
Color control
![image357.png](PERFORMANCE MARKETING _images/image357.png)
![image356.png](PERFORMANCE MARKETING _images/image356.png)

Tools AI: dreamina
Clipper
Tools: opusclip
Bisa trial 1 minggu 15 dollar 250 ribu
Ambil yt link/zoom link
Sistemnya credit (makin panjang videonya makin banyak creditnya)
Cara: ambil klip yg viewsnya tinggi di timestamp tertentu
1 menit = 1 kredit

THE PROMPT
Kalau buat ads video bisa pakai VEO

Useful prompts:
Prompt : Village square scene, a wise middle-aged Lurah (male, in brown batik shirt and black peci) stands before a crowd, his face serious, holding a microphone say : Lurah (urgent): “Benderanya… hilang?!”
### The prompt:
A pair of hands enters the scene, reaching for the central figure. They carefully **lift the figurine from its circular base** and **tilt it slightly**, as if to inspect it more closely. Meanwhile, the digital representation of the figure on the computer screen—a gray-scale 3D model—remains perfectly still. The illustration on the packaging box to the right also stays fixed, its outline and colors unchanging. The rest of the background, including the desk, keyboard, and shelves, remains completely still and unaffected by the movement.

IMAGE AND VIDEO CREATION
 → gambar
Kling AI → video production (harga lebih terjangkau)
Runway → video production
Midjourney
Flux
Higgsfield Ultimate Vid

Klik Create Video
→ bisa veo bisa kling
→ better pakai reference video atau image
→ pakai kling better pakai motion control tapi ga disarankan untuk yang pergerakannya banyak
→ scene control: choose the background shot from (dari gambar atau dari video reference kita)
→ orientation: karakter orientation match video atau gambar
→ background reference betterclean
→ bisa pake motion di library juga

Langkah
Create reference nya dulu (atau create gambar dulu)
Baru dibikin video
Upload reference terus masukin promptnya
Required:
SHOT
SUBJECT
SCENE
VISUAL DETAILS
ACTION AND CAMERA MOTION
CINEMATOGRAPHY
STYLE
AUDIO
Enhance bisa di on kan atau di off kan
Tentukan modelnya

Kalau text ke video jarang yang bagus

### RELIGHT VIDEO
Pakai reference chaining (reference diupload as prompt)
Pakai higgsfield image, transform dulu gambarnya (pengen misal pencahayaannya jadi golden hour)
Penting! Kasih notes IMPORTANT: preserve original face structure, identity, expression, hairstyle and pose exactly, do not modify the face.
Upload gambar reference → nano banana pro → rasio 16:9 → resolusi 1k → 2x batch → copy paste prompt → generate → download
Ke video → edit kling → upload video shornya → masukin elemen imagenya
Change the lighting of @.video1 to lighting of @.image1 make the face stay consistent like in the @.video1
Kling 3.0 omni edit

### HIGGSFIELD CINEMA STUDIO
Masuk ke video → cinema studio video → masukin screenshotan gambar → pilih multishot manual
(intinya generate gambarnya dulu baru bikin videonya, promptnya bisa pake bantuan chatgpt, gambar tuh as a reference starting scenenya, promptnya act as an action prompt)
Trs ntar tinggal diedit2 aja bagian yg perfect sama yg engga

### MEMBUAT TALKING HEAD MENGGUNAKAN HEYGEN
Cukup masukin script/audio
Langganan/paid
Masukin dulu video
Masuk ke avatars > create avatars > get started > still > next step > upload footage
Video yang diupload adalah Golden sample (konten talking head aja, ngomong asal 2 menit selama 2 menit gerakan tangannya bagus. Formulanya
Face: eyebrow updown 2x1 (2 detik 1 kali), eyes open and close 3x1
Body gesture: body move 5% compensation
Hand: L, hold, 2, L, R, hold
No lick, no side eye, no head move (20%))
Setelah avatar nya jadi, klik create video, klik avatar video, klik portrait, pilih avatarnya
Hapus textnya
Upload audio yg kita mau
Klik submit > pilih nama > on atau off watermark > done > download > capcut > tetep editing kek video biasa ujung2nya

### MEMBUAT BABY PODCAST HEYGEN
(well, not really important, but perhaps we can use if we want to create podcasts)
Can’t use chatgpt karena ada violationnya (mem-babykan adult) → bisa pake flora fauna ai, caranya:
Ganti model jadi flux
Upload image
Prompt: a baby in podcast studio (dienhance pake ai buat promptnya)
Download and masukin ke pictures hygiene, terus masukin scriptnya

### MEMBUAT MUSIC VIDEO VEO3
Garis besar + karakter
Scene a music video an Indonesian beauty woman (seed caracter 457580) floating like astronaut with oversize  silver jacket. The background is space craft with indonesian flag on screen. The lighting is ambience red and blue light soft.
Singing in rap up beat: “kata2”
Tab 65
TOOLS AND PRICING

HEYGEN
Pricing
Free
1 video per bulan
Video hingga 3 menit
Ekspor video 720p
Akses uji coba fitur premium
Creator 29 USD/bln
Video unlimited
Video 30 menit
Bisa 175+ bahasa
Hapus watermark
Pro 99 USD/bln
Penggunaan premium 10x lebih banyak
Pemrosesan video lebih cepat
Sunting & koreksi naskah terjemahan
Ekspor 4k
Higgsfield
Basic 9USD/bln (billed for 12 months)
150 credits/bln = 75 nano banana pro generations, 25 kling 3.0 videos
2 video, 2 image, 1 karakter
Pro 23USD/bln billed 12 months
600 cred = 300 nano banana pro gen, 100 kling 3 vid
3 video, 4 image, 2 karakter
Ultimate 39USD/bln
1200 cred/bln = 600 nano banana pro gen, 200 kling 3 vid
Creator 199USD/bln
6000 cred/bln = 3000 nano banana pro gen, 1000 kling 3 vid
Kling AI
🆓 1. Free Plan

±66 credits (harian / bulanan tergantung versi)

video pendek (±5–10 detik)

resolusi rendah (360–720p)

ada watermark

👉 cukup buat testing aja

🟡 2. Standard Plan

💰 ± $7 – $10 / bulan

±660 credits / bulan

tanpa watermark

resolusi sampai 720p

full akses model dasar

📊 Output kira-kira:

±30–60 video pendek / bulan

👉 cocok buat beginner / content ringan

🟢 3. Pro Plan

💰 ± $25 – $30 / bulan

±3000 credits / bulan

resolusi 1080p

cinematic mode

kontrol kamera lebih advanced

📊 Output:

±60–100 video HD (5 detik)

👉 ini yang paling “worth it” buat creator

🔵 4. Premier Plan

💰 ± $60 – $80 / bulan

±8000 credits

lebih banyak output

prioritas render

👉 cocok buat:

content creator harian

small agency

🔴 5. Ultra Plan

💰 ± $120+ / bulan

±26,000 credits

produksi besar (ratusan video)

👉 untuk:

agency

production team
Veo3
🟡 1. Subscription (paling umum)
Google AI Pro — ± $19.99/bulan

Fitur:

akses Veo 3 / 3.1 (versi terbatas)

±1000 credits

Flow video editor

Gemini AI

📊 Estimasi:

10 detik video ≈ 125 credits

👉 cocok untuk:

creator ringan

eksperimen

🔴 Google AI Ultra — ± $249.99/bulan

Fitur:

akses penuh Veo 3 & Veo 3.1

±12,500+ credits

30TB storage

semua AI Google

👉 cocok untuk:

agency

production heavy

📌 Insight:

Pro = limited access

Ultra = full power

🧠 2. API Pricing (pay-as-you-go)

Kalau pakai via developer:

💸 Harga per detik:

Fast model: ± $0.15/sec

Standard: ± $0.40/sec

Contoh biaya:

5 detik → $0.75 – $2

10 detik → $1.5 – $4

📌 Versi lama bahkan sempat:

$0.75/sec (lebih mahal)

🟢 3. Credit system (dalam subscription)

Walaupun kamu subscribe:

👉 tetap pakai credits

1 video = makan credits

makin:

panjang

HD / 4K

pakai audio

👉 makin mahal

⚠️ Limitasi penting Veo 3
❗ 1. Durasi pendek

rata-rata:

5–10 detik per generate

➡️ video panjang = stitching

❗ 2. Tidak benar-benar “free”

tidak ada free plan penuh

harus lewat subscription

❗ 3. Akses belum fully terbuka

kadang:

waitlist

region limit

fitur beda tiap platform

OPENCLAW
### OPENCLAW

Moltbook → AI sosmed
Install ke computer, punya full akses kontrol ke komputer kita → but still we need to be careful

### INSTALLATION

Bisa install di cloud (ready to use, lebih secure) atau local deployment (full control, data privacy)

![image259.png](PERFORMANCE MARKETING _images/image259.png)

Install di cloud → berbayar, API boros
Install di lokal → higher risk, bisa install di ollama
 (instruction here)

Buat akun di ollama → bisa akses beberapa model cloud free (glm-5 for coding and reasoning, kimi-k2.5 ada promo 1 dollar/bulan)
After install klik openclawdashboard
Saranin pake di cloud instead of local krn lebih aman

Cloud → hostinger
Kalau udah punya server hostinger klik docker manager (diskon 20% hostinger:  )

Siapin API key google (ke google ai studio, ambil api keys pake gemini)
Klik docker compose klik deploy sekali klik
Ketik openclaw, klik deploy
Gateway token = pass untuk masuk
Telegram bot token (ke telegram, ke bot father, buat bot baru, namain + username, dapetin kodenya, terus copy codenya paste ke telegram bot token)
Copy api keys ke gemini api keys di hostinger, trs kita punya dashboard sendiri dan bisa connect ke telegramnya
Udah dideploy klik buka, copy token gateway trs paste
Kalo mau diubah tinggal klik kelola trs ke environment trs diubah2 aja

Kalo mau ke open AI tinggal klik ke open AI → tp kalo perlu api keys itu hrs bayar

Openrouter ai models → free > riverflow, arcee ai: trinity large preview (free) copas
Api keys > create new secret key > pilih default project > copy > trs ganti > save > deploy

### INTERFACE & FEATURES
Kalau ada update → klik update aja
Health → apakah Ai dan getaway aktif, kalau hijau oke
Main session → bisa ada session2 lain misal connect ke telegram jadi session baru
Overview → tampilan keseluruhan (url, getaway token, password, agent, bahasa, snapshot)
Channel → gmn caranya connect ke channel (telegram, whatsapp)
Instances
Usage → brp token yg udh kita habisin di sini
Kalo pake cloud paymentnya lumayan

Cron Job → habit yg bisa dijalanin sama openclaw without us prompting everytime

Persistent memory → mengingat detail who are we etc
Tools → apa yg biasa diakses si ai
Skills
Channel
Cron jobs

Skills → bisa inject bbrp tugas

Nodes → device yg connect

Logs → untuk cek errornya dimana

HOW TO CREATE CRON JOBS
Ketik nama, deskripsi, siapa yg jalanin, mau kapan jalaninnya, atau cron
Klik promptnya nnt dia bisa set sendiri

Clawhub → cek apakah skillnya free virus/malware
Download zip ke skill yg kamu pengen dari clawhub
Masukin zip ke folder workspace di openclaw di skill

### SKILLS
Cek di clawhub skillsnya ada apa aja
Skill banyak yang scam → cek securitynya
Cara pakai
Download zip > ke foldernya > copy > ke tempat install clawnya > workspace > paste di skills
Marketing skills for AI Agents (di github) > install pake npx skills, copy > buka ke terminal > klik spasi buat install semua > pilih install ke open claw > install di project atau global > klik ke symlink
How to use it > prompt in your claw

### MULTIPLE AGENT OPENCLAW
Dashboard > agents > set up orchestrator > bisa set via tutorial multi agent routing di docs.openclaw > copy ke terminal
Siapin prompt untuk orchestrator dulu
![image247.png](PERFORMANCE MARKETING _images/image247.png)
Kita bisa pilih skill apa yg mau kita aktifin per agent
USEFUL AI REFERENCES
How to build a full ad campaign with AI -
AI reels for brand promotion
Full Commercial from Product Images -

AI insights from X
how to master AI content in 7 days (the exact roadmap)
Miko
@Mho_23

a week from now, two versions of you exist...
one is still watching other people post AI content, wondering how they make it look so real, bookmarking tutorials they'll never finish
the other is producing professional AI videos for any product in any niche, testing 50 creative angles while competitors test 5, building an unfair advantage that compounds every single day
same starting point, different trajectory, and the split happens in the next 7 days
AI content is by far the most important skill you should be learning right now
if you run any type of business or want to run one, you already know marketing is everything. you can have the best product in the world but if your marketing isn't good then it doesn't matter. nobody will ever see it.
what AI content allows us to do for the first time is marketing at scale. before this you were limited by how much content you could produce, how many creators you could afford, how many variations you could test. now those limitations are gone.
if you master this skill you can pretty much market anything. you can test dozens of creative concepts in a day. you can stand out from the competition because you're not limited to one or two angles anymore. you can actually find what works instead of guessing and hoping.
this is something you should be learning and implementing now. do not wait on this. the window is open right now but it won't stay open forever.
here's the exact curriculum that gets you there
the foundation: why most AI content looks like slop
most AI content fails not because the tools are bad but because people don't understand what makes content look real vs what makes it look obviously AI generated
there are specific tells that give AI content away instantly. the grey washed color grade that Nano Banana outputs by default. the overly polished studio voice that sounds nothing like someone talking in a room. the robotic movements. the scripts that sound like ChatGPT wrote them because ChatGPT did write them and nobody bothered to fix it.
once you understand what these tells are, you can systematically eliminate them. that's what separates content that gets scrolled past from content that actually converts.
the tools are getting better every week. the visuals are getting solved. the voice quality is getting solved. but the one thing AI cannot solve for you is having something worth saying. the messaging, the angles, the hooks, the way you frame the problem and position your solution, that's the actual skill.
let's build it
### day 1-2: AI images and the JSON method
everything starts with generating images. before you even think about video you need to understand how to generate good images because these images become the starting frames for everything else.
the best tool for this right now is Nano Banana Pro or Nano Banana 2. this can create ultra realistic AI images from a text prompt. when i say realistic i mean images that most people genuinely cannot tell are AI generated.
but here's what most people miss: Nano Banana normally outputs images with a grey scale color grade which immediately makes them look AI generated. anyone who has seen enough AI images can spot this instantly.
the fix is using JSON prompts for color grading instead of just typing a regular text prompt.
go to Pinterest and find a reference image that has the exact aesthetic, lighting, and color grading you want. upload it to ChatGPT with thinking mode enabled. ask it to create a detailed JSON prompt that would recreate that image. it will give you a JSON output that captures all the lighting information, color grading, tones, shadows, highlights.
now when you generate your image in Nano Banana, paste that JSON as your base and add your actual prompt on top of it. the JSON handles all the realism and color grading so your images don't come out with that standard grey AI look. your text prompt handles the actual content.
this combination gives you dramatically better results than just typing a text prompt by itself.
goal: generate 20+ images using the JSON method until you can consistently produce results that don't look obviously AI
### day 3: AI voices that sound human
the voice is what makes or breaks the realism of any AI video content. you can have perfect visuals but if the voice sounds robotic people scroll past immediately. they don't even consciously register why they scrolled, they just felt something was off.
the best tool for beginners is ElevenLabs. but do not use the pre-made voices in their library. those voices sound too generic and too polished. everyone using ElevenLabs is using those same voices which means your content ends up sounding like everyone else's content.
instead use voice design or instant voice clone. with voice design you describe the type of voice you want and include instructions that make it sound like it's in the actual room with natural room tone, not like it was recorded in a perfect studio environment.
MiniMax is another solid option at $5 per month for 120 minutes. the voices feel like someone talking in a room which is more realistic than overly polished studio audio. when voices are too clean and too polished they stop sounding realistic because real people don't sound like that when they're filming casual content on their phone.
goal: create 3 custom voices that sound natural and test them with sample scripts
### day 4-5: AI video generation
there are many AI video tools on the market and it's hard to know which ones are actually good vs which ones are just hype.
there are only 3 tools you need to focus on right now:
Veo 3.1 is the complete package for narrative clips. native audio generation with synchronized sound effects and dialogue, up to 60 seconds through scene extension, 4K output. use it when you need a finished clip that sounds like something actually happened.
Kling gives you the most realistic physical motion available right now. many viral videos on social media are actually Kling generations. use it when believability matters more than audio.
Seedance 2 works completely differently than anything else. the real capabilities are in the dynamic prompts and referencing features. you can attach multiple images, videos, and audio clips as reference for a single generation. this means you can recreate the editing style and video style of literally any video on the internet.
what you need to know before using any of these:
5-10 seconds is the reliable range. longer generations degrade in quality.
budget 3-10 attempts per usable clip. same prompt yields wildly different results.
goal: generate 10+ videos across all three platforms until you understand what each one is best at
### day 6: scripts and messaging
this is where most people fail and it's the most important day of the entire roadmap.
it doesn't matter how good your AI tools are if your messaging is bad. you can have the most realistic visuals, the most natural sounding voice, perfect motion, perfect lighting, and none of it matters if what the person is saying doesn't resonate with whoever is watching.
for writing scripts use Claude or Kimi K2. these models produce copy that actually sounds like a human wrote it unlike other models that output that flat corporate AI tone everyone recognizes instantly.
the script should sound like a real person talking, not like an advertisement. read it out loud and ask yourself if you've ever heard anyone actually speak that way in real life. real people ramble. real people correct themselves mid-sentence. real people use filler words and pause at weird moments. real people don't speak in perfectly structured sentences with a hook, three supporting points, and a clean call to action.
when you're writing scripts you need to think about who exactly is watching and what is going through their head right now. not "millennials interested in fitness" but "28 year old women who have tried three different workout programs in the last year, feel overwhelmed by all the conflicting nutrition advice online, and are skeptical of anything that promises fast results because they've been burned before."
that level of specificity changes everything about how you write.
goal: write 10 scripts for different products and read each one out loud to check if it sounds natural
### day 7: the complete production pipeline
now you put everything together into a repeatable workflow that you can run over and over again.
start by writing your script using Claude or Kimi K2. then generate your AI character in the right scene using Nano Banana with the JSON color grading method. make sure the starting image is high quality because every problem in your starting image will carry through to your final video.
then generate the video clip using Veo, Kling, or Seedance depending on what you need. generate your voiceover separately using ElevenLabs or MiniMax with a custom voice.
if you want to increase quality further you can run your video through Topaz to upscale it and smooth out the frame rate.
assemble everything in CapCut. layer your video, your voiceover audio, your captions, and any background music. cut faster than you think you should, especially in the first three seconds. platform algorithms reward early retention above almost everything else.
the key is making sure each individual step is high quality before you move to the next step. garbage in garbage out.
goal: produce 5 complete videos from start to finish using the full pipeline
the path forward
7 days from now, two versions of you exist
one completed this roadmap and can produce professional AI content for any product in any niche. they can test angles faster than their competition. they can market anything.
the other is still collecting bookmarks, still planning to start, still waiting for the right time
same starting point, different trajectory
the window matters because the gap between people who know this and people who don't is widening every month. the people who build these skills now will have compound advantages that grow over time. the people who wait will face an increasingly steep climb as everyone else catches up.
the roadmap is here. the tools work.
7 days, 2-3 hours daily, and you're producing instead of watching.
if you want the complete system with every workflow, every prompt, every method you can find the best AI content system right now here:

contentsystem.ai
if you found this helpful, join here for more free value:
t.me/mikoslab
Want to publish your own Article?Upgrade to Premium
Show 7 replies
Miko
@Mho_23
building ai intersections | the proven system for AI content -
http://
contentsystem.ai

N8N
### N8N
THE INTROSSSSS

### AUTOMATION
Step By Step yang sudah ditentukan untuk memindahkan dan mengolah data secara otomatis

### EXAMPLE OF AUTOMATION
Chat di DM IG → Kirim LINK yang diminta → there are several conditions then we sent the responses based on the conditions

### AUTOMATION COMPONENTS
Trigger
Komponen yang jadi awal ‘mulainya’ suatu Automation
→ Manual
Ada action (diklik, dibuka, dll)
→ Scheduled
Every minute
Every day at 8 am
Every day at 8
→ Applications
Misal orang post file ke folder drive maka akan terjadi proses setelahnya, kirim DM ke IG, komen ke IG
Webhook
Property update
Form submission

Filtering
Atur data mana yang ingin diproses berdasarkan aturan tertentu
Misal:
Kita akan balas chat berdasarkan indikator:
Verified
100k folls
Kita follow juga
Lainnya
Respons kita beda based on that indikator

Actions
Interaksi dengan aplikasi: mau ngapain di aplikasi apa?

### WORKFLOW AUTOMATION
Trigger → Sorting, filtering, formatting, transforming, segmenting → Actions

Setiap hari jam 8 pagi → kalo ada org yg dm dengan followers 100km ke kita maka → kita update google sheet dan kirim DM ke org tersebut

### PROCESS MAPPING
Langkah awal dari setiap automation yang bagus
Makesure you done this sebelum bikin automation:;
Mengerti apa saja proses yang ingin dibikin otomatis pakai N8N
Tau aplikasi/website apa yang akan digunakan
Mengerti apa yang bisa dan tidak bisa kita lakukan di N8N
Estimasi jumlah waktu yang dibutuhkan dari setiap langkah yang ingin dibuat otomatis
Mengerti bagian mana yang tetap butuh campur tangan manusia

PROCESS MAPPING AI UNTUK REMINDER SCHEDULE
Triggernya apa? Misal setiap Jam 8 Pagi
AI cek Google Calendar
AI kirim message ke orang yang les dari 2 guru berbeda melalui Whatsapp
Waktu: make sure H-7 dari jam orang les, dan reminder H-1 dari jam orang les
Setelah semua reminder dikirim di hari itu, recap dan kirim ke whatsapp grup music school
Jika ada yang gak bisa les, recap dan kirim ke whatsapp grup music school
Notes: kalau jadwal berubah, kirim ulang remindernya

### PROCESS MAPPING CASE STUDY: GENERATE CONTENT
Cari Ide Konten
Trigger: Setiap jam 8 pagi, setiap ada update topik baru di google sheet, setiap ada video youtube dari channel xxxx
Aksi: hasil akhirnya Ide Konten

Proses
Kirim prompt di chatgpt untuk kasih 10 ide konten
Masukkan 10 ide kontennya ke gsheet

### THE TOOLS
Apa yang kamu butuhin
GPT
Gsheet

### CAN DO VS CAN’T DO
Buka N8N → cari app apa aja yang ada di N8N
WA can
Kalo can’t → cek apa app kalian ada API nya

### ESTIMASI WAKTU

### HUMAN INTOUCH
Review oleh manusia

KEBUTUHAN
Reminder WA
Networking
Reminder EXP
Tentuin tgl acara
Tanya org alasan perpanjang membership
Survey & fgd
Edit thumbnail yt
Exit interview

N8N → berlangganan atau diundang kak hamzah jadi anggota (tp not permanent)

Cara ngajar:
Share screen → bahas gmn automationnya

Cloud 20usd → 20 dollar (1000 eksekusi workflow per bulan) → ga perlu mikirin apapun → fitur AI

VPS server → kalo ad tim tech bagus ada domain (sewa server) → aplikasinya

Platform → sumopod 1 kali klik n8n jadi tinggal login → service → add service tinggal tambah n8n → otomatis dapat linknya dapat
N8n pro

Railway → cepet habis → butuh 4 cepet habis → butuh minimal 20$ kalo mau scale up

Kalo saran pake sumopod

WAHA/go wa → ga resmi

Halo api → halo ai

Wa bisnis bisa, tapi harus setup dari awal, wa bisnis harus dihapus dan diintegrasikan ke omnichannel (ga bisa diakses ke wa web)

Api → di nomor → risiko kebanned → go whatsapp pake akses wa web
Kalo cepat pake waha, kalo official halo ai
set up n8n
### SETUP N8N: CLOUD VS SELF HOSTED

Cloud
Pakai fitur yang dibawa di N8N no need cari di luar, tinggal daftar aja di N8N
Self hosted
Narik kode dan fitur N8N hosting di server lain
Self hosted locals
In your own laptop, meaning your laptop can’t shutdown

### SETUP N8N CLOUD BASED
Buka
Get started, isi semua datanya
Ingat2 ur account name

### USER INTERFACE
Overview -> workflow yg udah dibikin → ada kayak diagram flow
Ada button activenya

## Canvas
Latar belakang kotak-kotak abu-abu di tampilan Editor.
Di atasnya terdapat beberapa ikon dan satu node dengan berbagai fungsi:
Tombol untuk **menyesuaikan tampilan canvas agar pas di layar**, **zoom in atau zoom out**, dan **merapikan posisi node** di layar.
Tombol untuk **menjalankan workflow** setelah kamu menambahkan node pertama. Saat kamu klik tombol ini, n8n akan menjalankan semua node di canvas secara berurutan.
Tombol dengan ikon **tanda tambah (+)**. Tombol ini untuk **membuka panel node**.
Tombol dengan ikon **catatan**. Tombol ini berfungsi untuk **menambahkan sticky note** ke canvas (akan muncul saat kamu arahkan kursor ke ikon + di pojok kanan atas).
Kotak putus-putus dengan tulisan **“Add first step”**. Di sinilah kamu **memulai dengan menambahkan node pertamamu**.
## Node
Langkah-langkah dalam alur kerja (workflow) kamu. Setiap node bisa berfungsi untuk (a) mengambil data, (b) memproses data, atau (c) mengirim data.
## Apa itu Workflow?
**Workflow** adalah *alur kerja otomatis* yang terdiri dari beberapa langkah (disebut **node**) yang dijalankan secara berurutan untuk menyelesaikan sebuah tugas.
Bayangkan seperti **resep masakan**, di mana kamu mengikuti langkah-langkah dari bahan mentah sampai jadi makanan siap saji. Nah, di dunia otomasi, setiap langkah itu adalah node, dan rangkaian langkah itulah yang disebut **workflow**.
### Contoh Workflow di n8n:
Misalnya kamu ingin otomatisasi proses berikut:
**Trigger**: Ketika ada email masuk.
**Proses**: Cek apakah email itu mengandung kata "invoice".
**Aksi**: Kalau ya, simpan lampiran ke Google Drive dan kirim notifikasi ke WhatsApp.
Semua langkah itu digabungkan jadi satu **workflow** di dalam n8n, dan semuanya bisa berjalan otomatis tanpa kamu harus melakukannya manual.
### Manfaat Workflow:
Menghemat waktu (semua kerjaan jalan otomatis).
Mengurangi kesalahan manusia.
Bisa digunakan untuk banyak hal: bisnis, konten, customer service, sampai AI.

### TOP BAR OVERVIEW
Nama Workflow (Nama File)
Tag (menandai masuk kategori apa)
Save

### NODE
1 kotak kecil → mewakili proses/aktivitas jadi otomatis → misal: membuat file di google sheet (pilih node google sheet trs pilih actionnya apa)

### DEEP DIVE ABOUT NODES
Bisa klik tambah di tengah atau di pojok kanan atas
Kalo yg pojok kanan atas tuh untuk node baru
Kalo mau ngubungin tinggal klik tambah yg ada di node

Category Node
AI → hal2 yg bisa dilakuin AI
In an app → bisa ngelakuin sesuatu di app
Data transformation → ngubah data
Flow → mau ngecek suatu kondisi, apakah tgl nya tu tgl gajian, kalo hari ini tgl xxx maka xxx
Core → apapun yg ga bisa di node lain hrsnya bisa dilakuin di node (it is more technical coding things)
Human in the loop → mau di tengah2 proses tuh ada interaksi human → nunggu feedback manusia dll
Add another trigger → eksekusi workflow lain dari workflow ini (if u have multiple workflows) → bales sesuatu berdasarkan isi chatnya (mengandung kata A)

### ACTIONS IN A NODE
Ada 4 tombol
Tombol eksekusi (mau menjalankan node tsb) → menjalankan chatgpt misalnya → pilih model -> ketik messagenya
Klik play → buat eksekusi
Tong sampah → delete
Tombol kedua → matiin satu bagian node (Deactivate) biar bisa kek loncat ke flow selanjutnya
Open → pengaturan
Rename
Bisa copas juga
Bisa duplicate

### EXPORTING N8N WORKFLOW
Pencet tombol tiga di atas → pilih download → file tersimpan (bentuk filenya json)

### IMPORT N8N WORKFLOW
Bikin workflow baru → import work flow → klik from file → pilih .json → pilih open

### CASE STUDY SUPERHERO VIRAL VIDEO RESEARCH AUTOMATION
THE CREATOR SHEET
Buat 1 sheet 2 kolom: nama & uname creator yg mau kita ambil

THE REFERENCE VIDEOS SHEET
Konten viral dari creator yg kita pilih
Kolom ID, Creator, Ig reels url, caption, hashtag, durasi video, video play count, likes, comment, video url, thumbnail url

THE PREREQUISITES
Platform/app
Spreadsheet
Google sheet api
Open ai
Railway
Github
apify

SETUP GITHUB ACCOUNT
As gdrive khusus buat code
Klik tombol setup
Email uname pass
Verify
Perlu buat bisa masuk ke railway

SETUP n8n using RAILWAY part 1
Platform untuk mengaktifkan website/aplikasi yang scr aplikasi ga ada
Murah, udah support template n8n, ada free trial, fee 5 usd/bulan

Piliih sign in
Continue with github

SETUP n8n using Railway part 2
Pilih new
Deploy a template
Pilih n8n with worker
Wait 3-5 secs (all green) pilih deploy nnt dia bakal crseating project (tandanya ijo)
Pilih primary, klik linknya (bikin akun baru n8n lewat link ini) → isi datanya → started → send me a free license key → masukin codenya dari email ke enter activation key → activate → done, bisa pake n8n nya di sini
RAILWAY ada batasnya 5usd gratis, cek project usgae limit hard limit 5$ kalo udah nnt bakal mati gitu (kalo bayar paling 1-2$ per bulan)

MAKE A COPY OF GOOGLE SHEET TEMPLATE
Intinya bikin template kosongan google sheet biar ai nya bisa isi hasilnya di sini

SETUP APIFY ACCOUNT
 → ngambil data dari berbagai website → berbayar 5usd
Get started → continue with github

SIGN IN TO OPEN AI PLATFORM

Login ke api platform → masuk ke continue with google (nnt masuknya bakal ke akun gpt) → nnt bakal dapat api key

GET OPENAI API KEY
Bayar biaya sewa tiap kali ngeprompt 0.000sekian dollar
Start building → isi nama company → pilih non technical
Email skip aja
API key name: N8N Key Integration
Project name: bebas
Nah nnt copy api kenya, bayar minimal 5usd
Ke api key, edit, cm bisa sekali pake jd copy paste trs simpen
Buka n8n → credentials → open ai → continue → paste the api key
Masukin organization id ke n8n (pergi ke open ai → general → copy organization idnya) trs save
Create workflow → open ai → bisa ngeprompt

THE GOOGLE CREDENTIALS IN N8N
Buat project baru di google cloud console
Akses link
Cek kiri atas my project (bikin new project) punya batas kuota 25 gratis
Kasih nama N8N integration
Organisasi biarin
Klik create
Select project
Harusnya di kiri ada nama n8n integration
Masuk API and services (klik tombol tiga kiri di atas, pilih enable api and services)
Cari google sheet API
Klik, pencet enable
Pilih bagian credentials → api masih kosong → set OAuth consent screen klik get started → masukin app N8N masukin email kita masukin audience external pake contact information finish create
Klik branding, scroll ke bawah, klik add domain, klik railway.app
Kalo pake n8n cloud bisa pake n8n.cloud
Klik tombol clients, plih create clients, web application, authorized redirect urls → pergi ke n8n → pilih panah credentials pilih googl sheet pilih link oauth redirect, copy masukin, trs create → simpan client id dan client secret
Client id masukin ke n8n
Client secret masukin ke n8n
Trs klik sign in with google pilih email untuk ngerjain project → continue verified, kalo kena block:
Enable api dan services masukin gdrive api enable
Pergi ke credentials oauth consent screen audience, bagian bawah tambahin add user masukin email, trs hrsnya bisa sign in
Kalo berhasil connection successful
Logo account connected
Cek workflow google sheet coba cek bagian credentials, muncul ga daftar dokumennya, kalo muncul berarti bisa

ADD GOOGLE SHEETS INTO THE N8N WORKFLOW CANVAS
Create workflow
Ganti namanya
Bikin trigger → trigger manual (cuma akan jalan ketika kita bikin execute workflow)
Buka google sheet di n8n, pilih get rows in sheet (mau n8n bisa baca data di google sheet)
Pilih file sheet templatenya
Pilih creators (one of the sheet)
Pencet tombol orange (ga munculin data apapun krn datanya kosong)

THE DATA DISPLAY AT N8N
Schema
Table
Json
Key/code/id
Value/isi

ADD LOOP TO THE N8N WORKFLOW
Pilih tombol loop → mau loncat brp (kalo udah abc lanjut ke username next) (kalo mau satu2 masukin angka 1)
Done → kalo misal loopnya udah selesai dan km mau ngelakuin sesuatu after selesai berarti tambahin add di done
Kalo udah kelar dan mau balikin loop tinggal balikin aja panahnya ke loopnya

OVERVIEW HTTP REQUEST
Klik tombol panah abis loop > pilih HTTP request (biar bisa cari konten yg viral dll)

WHAT IS AN API?
API is the waitress at the restaurant
Application Programming Interface → cara suatu layanan bisa digunakan oleh program lain

OVERVIEW OF HTTP API REQUEST COMPONENTS
Url
Alamat unik for a resource on the web
Scheme = https
Host =
Port = :443
Path/endpoint = search (pembeda satu info dg info lainnya)
Query parameters = info tambahan

Method
Aksi apa yang kalian pengen pelayanan lakuin
Get = receive infos
Post = send infos
Delete
Put
Patch

Header → info yg kita selipkan yg sifatnya lebih universal
Cara ngasih info yang berbeda ke request
Common infos di header:
Location
Language
Device type
Example = accept: application/json (tells the server it would like responses in the json format)

Body → the datas so they could retrieve the info we need
Cuma ada kalo methodnya tuh POST
Using the form submission example, the body could contain:
first_name:”Maxim”
last_name:”Poulsen”
email:”maxim@example.com”

HOW TO GET APIFY TOKEN
Klik tombol panah abis loop > pilih HTTP request (biar bisa cari konten yg viral dll) > method: get > url dapetin dari apify
Kita ke apify > ambil token di setting (api integration yg bintang bintang) > copy

ADD HTTP REQUEST TO N8N WORKFLOW
Ke apify > instagram scrapper > cari di kanan api n points
Buka n8n > http request > centang query parameter > masukin token > masukin link data set copy cuma sampe path end points ga usah sampe query parameter > method nyesuaiin yg kita copy
Body > cek dokumentasi view api reference > copy > send json > using json
{{$json.username
Onlypostsnewerthan (data2 360 hari terakhir)
Resultslimit:
![image299.png](PERFORMANCE MARKETING _images/image299.png)
![image275.png](PERFORMANCE MARKETING _images/image275.png)
![image272.png](PERFORMANCE MARKETING _images/image272.png)
SHOPEE ADS
### SHOPEE CPAS
CPAS hanya bisa maksimal jika dasar Shopee Ads sudah kuat
CPAS = pengembangan Shopee Ads yang diintegrasikan dengan Meta

### FUNDAMENTAL SHOPEE ADS
Ada 4 pilihan utama iklan
Iklan produk
GMV Max Auto
Sistem otomatis pilih produk, bidding, dan optimasi berdasarkan behavior marketplace dan performa sebelumnya, tanpa kita harus setting terlalu banyak
GMV Max ROAS
Seller tentukan target ROAS sendiri, sistem akan bekerja untuk jaga iklan tetap efisien dengan ROAS mendekati target itu
**Then, what should we choose?**
Baru mulai dan belum punya banyak data → Auto
Data udah stabil dan ngerti performa buku → ROAS
Fokus testing banyak produk baru → Auto
Fokus optimasi efisiensi dan profit → ROAS
### THE HACK
Pakai GMV max auto min 7 - 14 hari
Kalo udah stabil, pindah ke gmv max roas based on data
Monitor ROAS, CTR, Conversion
Kasih waktu learning
Fokus pada hasil mingguan bukan harian
Iklan toko
Objective = naikin traffic ke toko
When to use this?
Mau bangun branding toko biar makin dikenal dan awareness tinggi
Punya banyak SKU
Mau naikin traffic menjelang promo
Beberapa produk punya performa sedang, tapi punya potensi besar buat cross sell
### THE HACK
Banner menarik
Nama toko mudah
Aktifkan voucher ato promo bundle
Iklan banner
Iklan live

WHAT ABOUT CPAS?
Meta akan otomatis tarik data perilaku pembeli di Shopee lalu menghubungkannya dengan Meta FB and IG
CPAS is recommended for
Produk high demand
Punya omzet minim 10 jt/bulan di Shopee (supaya data cukup untuk diolah algoritma meta)
Scale up dengan budget iklan lebih efisien and sustainable
Kalau toko baru, fokus ke organik traffic and shopee ads sampai punya data base awal

FITUR
Integrasi Ecommerce
API Integration
Dynamic Ads
Audience Sharing

THE BUDGET
Awareness 20-30% budget
Consideration 30-40% Budget
Conversion 40-50% Budget

70% Budget → winning ads
30% Budget → testing

Winning Content = ROAS tinggi + CTR bagus

CREATIVE OPTIMIZATION
Ada 2 tipe iklan
Carousel Ads
Nampilin banyak produk all at once
Setiap card bisa punya link sendiri
Cocok buat testing produk yg paling diminati
Cocok untuk konsep storytelling brand
Collection Ads
Gabungin visual utama (video atau desain etalase utama) dengan katalog produk yang muncul di bawahnya
Ga perlu keluar platform untuk liat detail produk
Memberikan pengalaman belanja lgsg di feed
WHAT TO CHOOSE?
Testing produk yg paling oke → carousel
Bangun experience dan tonjolkan catalog → Collection

SCALING
Budget Growth Window
Tambah 10-20% budget tiap 24 jam
Naikin di jam performa terbaik
Jangan pernah ubah budget 2x dalam 1 hari
Duplicate Scaling
Identifikasi campaign paling stabil
Duplicate
Biarkan budget sama dulu 2-3 hari
Hasil stabil, scale 20% per hari
