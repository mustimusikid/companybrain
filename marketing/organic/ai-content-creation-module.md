---
title: AI Content Creation Module
domain_tag: [marketing, organic]
doc_type: sop
---

> Modul pelatihan AI untuk produksi konten: cara kerja ChatGPT/LLM, fitur ChatGPT, struktur & teknik prompt, level AI (generative → multi-agent), tooling gambar/video/voice (Nano Banana, Veo, Kling, ElevenLabs, HeyGen, Higgsfield), OpenClaw, dan roadmap 7 hari mastery konten AI.

## Cara Kerja ChatGPT / LLM
- LLM = mesin yang dilatih dari miliaran teks untuk memahami & menghasilkan bahasa manusia. Tidak "berpikir" — memprediksi token demi token. Belajar dari data → pahami pola ("kalau kata X biasanya diikuti Y") → prediksi kata selanjutnya → simpan pola sebagai parameter.
- **Komponen:** Parameters (aturan kecil penentu kata berikutnya); Tokens (potongan teks, 1.000 token ≈ 750 kata Indonesia); Token Embeddings (token → angka bermakna); Context Window (batas token per percakapan; GPT-3.5 ~4rb, GPT-4 8rb/32rb/128rb; cek di artificialanalysis.ai). Lewat batas → teks awal "tergeser keluar".

## Fitur ChatGPT
1. **Memory** — settings → personalization → memory (ada batas; bisa add/delete).
2. **Temporary Chat** — tidak masuk history/memory; untuk testing prompt.
3. **Custom Instructions** — settings → personalization; diprioritaskan di atas memory (1 persona, ada batas).
4. **Projects** — folder dengan instruksi & prompt spesifik.
5. **Tasks** — minta lakukan sesuatu di masa depan (mis. ide konten setiap pagi).
6. **CustomGPT** (berbayar) — my GPTs → Create & Configure; upload info, bisa dijual/share link.

## Struktur Prompt: Role → Context → Action → Output Format → Data
1. **Role** — AI berperan sebagai siapa.
2. **Context** — latar/info penting sebelum tugas.
3. **Action** — perintah spesifik.
4. **Output Format** — bullet points / tabel / list.
5. **Data** — contoh/referensi agar akurat.

### Teknik Prompt
1. Klarifikasi sebelum menjawab ("berikan saya beberapa pertanyaan dulu").
2. Cara jawab pertanyaan klarifikasi: tahu pasti → sekaligus; tidak → satu per satu.
3. Verifikasi ("sebelum melanjutkan, jelaskan X").
4. Continue or Regenerate (benar → lanjut; salah → edit prompt).
5. Reasoning ("lakukan step by step + alasan ringkas").
6. Delegasi diskusi ("pimpin diskusi, beri pertanyaan/pernyataan lanjutan").

## Level AI
1. Generative AI (input→output, stateless, no memory, human-initiated). 2. AI Workflow. 3. AI Agent. 4. Multi-Agent System.

## Tools Mastery
- Text→image: Nano Banana, Midjourney. Text→video: Sora, Veo3, Fliki. Image→image: Gemini. Image→video: Gemini, Kling. Video→video: Runway, Luma, Kling. Text→sound: Suno, ElevenLabs.

### Image/Video Gen Prompt (7 gold rules)
Aspect ratio; Shot type (extreme long → extreme closeup); Camera & lens (type + angle); Character control (emotion/direction/body pose); Light control; Composition; Color control (sessions.edu/color-calculator). Basic prompt: Style, Subject, Action, Environment.

### Higgsfield / Kling / Cinema Studio
- Higgsfield: Create Video (veo/kling) → pakai reference video/image; kling pakai motion control (hindari gerakan banyak); scene/orientation/background control. Langkah: buat reference/gambar dulu → buat video → upload reference + prompt (SHOT, SUBJECT, SCENE, VISUAL DETAILS, ACTION & CAMERA MOTION, CINEMATOGRAPHY, STYLE, AUDIO) → enhance on/off → pilih model.
- **Relight video:** reference chaining; transform gambar (mis. golden hour). Penting: "preserve original face structure, identity, expression, hairstyle and pose exactly, do not modify the face". Nano Banana Pro (16:9, 1k, 2x batch) → edit Kling, ganti lighting agar wajah konsisten (Kling 3.0 omni edit).
- **Cinema Studio:** generate gambar dulu (prompt via ChatGPT, gambar = reference starting scene, prompt = action) → multishot manual → edit.

### Talking Head & Podcast (HeyGen)
- Talking head: avatars → create avatars → upload golden sample (2 menit, gestur bagus). Formula: Face (eyebrow up/down 2×1, eyes open/close 3×1), Body move 5%, Hand (L, hold, 2, L, R, hold), no lick/side eye/head move. Create video → avatar → portrait → hapus text → upload audio → submit → download → edit di CapCut.
- Baby podcast: ChatGPT menolak (violation) → pakai Flora Fauna AI (model flux, upload image, prompt "a baby in podcast studio") → masukkan ke HeyGen + script.
- Music video VEO3: garis besar + karakter (seed character), scene + lighting + lirik rap.

## OpenClaw
- AI dengan akses kontrol komputer (hati-hati). Install cloud (lebih aman, API boros) atau lokal (risiko tinggi, via Ollama — glm-5, kimi-k2.5).
- Cloud via Hostinger: Docker manager → docker compose deploy → ketik openclaw → deploy. Gateway token = password. Telegram bot token (via BotFather). API key Google (Google AI Studio, Gemini). OpenRouter free models. Bisa connect OpenAI (butuh API berbayar).
- **Interface:** Health, Main session, Overview, Channel (telegram/whatsapp), Instances, Usage, Cron Job (habit tanpa prompt tiap kali), Persistent memory, Tools, Skills, Nodes, Logs.
- **Cron jobs:** nama, deskripsi, siapa jalanin, kapan/cron, prompt (bisa set sendiri).
- **Skills:** cek di Clawhub (banyak scam — cek security/virus). Pakai: download zip → workspace/skills; atau npx skills (Marketing skills for AI Agents di GitHub) → install global/project → symlink → prompt.
- **Multiple agent:** dashboard → agents → set up orchestrator (docs.openclaw) → siapkan prompt orchestrator; pilih skill per agent.

## Catatan Roadmap 7 Hari (referensi)
Day 1-2 AI images + JSON method (Nano Banana Pro; JSON dari Pinterest reference untuk color grading agar tidak abu-abu/AI-look). Day 3 AI voices human (ElevenLabs voice design/clone, MiniMax ~$5/120 menit — hindari voice pre-made). Day 4-5 video gen (Veo 3.1 narrative+audio, Kling motion realistis, Seedance 2 reference; 5-10 detik reliabel, 3-10 percobaan/clip). Day 6 scripts & messaging (Claude/Kimi K2, sound natural, spesifik audiens). Day 7 pipeline lengkap (script → Nano Banana JSON → Veo/Kling/Seedance → voiceover ElevenLabs/MiniMax → Topaz upscale → assemble di CapCut, cut cepat 3 detik pertama).
