---
title: Reference
domain_tag: [operations, hr]
doc_type: sop
---

> Human resources document for Musti Musik covering employment, contracts, or performance.

![image7.jpg](Reference_images/image7.jpg)
**REFERENCE**

# Explanation of Method That We Use
## PILIHAN METODE MACHINE LEARNING UNTUK DETEKSI/KLASIFIKASI CHORD
### CONVOLUTIONAL NEURAL NETWORK (CNN)
CNN adalah jenis jaringan saraf tiruan yang sangat efektif untuk memproses data dengan struktur grid, seperti gambar atau, dalam kasus kita, spektrogram audio. CNN terdiri dari beberapa lapisan yang memproses dan mengekstrak fitur dari input secara bertahap.
CNN sangat efektif untuk klasifikasi audio, termasuk deteksi chord. Metode ini bisa mengolah spectrogram atau mel-spectrogram dari audio sebagai input.
Mengapa CNN menjadi pilihan terbaik?
Kemampuan ekstraksi fitur otomatis: CNN bisa belajar fitur-fitur penting dari spektrogram audio tanpa perlu ekstraksi fitur manual.
Invariansi translasi: CNN bisa mendeteksi pola terlepas dari posisinya dalam spektrogram.
Skalabilitas: Mudah untuk menyesuaikan arsitektur CNN dengan kompleksitas tugas.
Apa saja komponen utama yang kita butuhkan untuk menggunakan metode CNN ini?
Convolutional Layer
Analogi: Ini seperti telinga ahli musik yang mendengarkan berbagai aspek suara.
Fungsi: Layer ini menggunakan filter (kernel) untuk mendeteksi pola-pola tertentu dalam input.
Contoh: Dalam spektrogram chord, layer ini bisa mendeteksi pola frekuensi rendah, menengah, atau tinggi yang khas untuk chord mayor atau minor.
Pooling Layer
Analogi: Ini seperti otak ahli musik yang memfokuskan pada informasi paling penting.
Fungsi: Layer ini mengurangi dimensi data dengan mempertahankan informasi paling penting.
Contoh: Setelah mendeteksi pola-pola penting, pooling layer akan menyaring dan menyimpan informasi paling relevan, seperti pola harmonik yang khas untuk chord mayor atau minor.
Fully Connected Layer
Analogi: Ini seperti proses pengambilan keputusan akhir oleh ahli musik.
Fungsi: Layer ini menggunakan informasi dari layer sebelumnya untuk membuat klasifikasi akhir.
Contoh: Berdasarkan pola-pola yang terdeteksi, layer ini akan memutuskan apakah chord tersebut mayor atau minor.
WORKFLOW
Persiapkan dataset audio chord mayor dan minor.
Konversi file audio menjadi spektrogram atau mel-spektrogram.
Bagi dataset menjadi data training, validasi, dan testing.
Rancang arsitektur CNN sederhana (misalnya dengan beberapa layer konvolusi, pooling, dan fully connected).
Latih model menggunakan data training dan validasi.
Evaluasi performa model menggunakan data testing.
CODE REFERENCE
