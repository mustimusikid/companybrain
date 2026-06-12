---
title: Copy Of Deep Learning 1
domain_tag: [operations, hr]
doc_type: sop
---

> Human resources document for Musti Musik covering employment, contracts, or performance.

Deep Learning
![image13.jpg](Copy of Deep Learning_images/image13.jpg)
**Deep Learning**

# Resource

# Course 1
## Summary
**Deep Learning** adalah **subbagian dari Machine Learning** yang berfokus pada algoritma berbasis **neural networks.**
**Deep Learning** menggunakan **artificial neural networks** dengan banyak lapisan yang terhubung (deep). Model deep learning bisa sangat kompleks dengan **jaringan saraf berlapis-lapis** (deep neural networks), termasuk **Convolutional Neural Networks (CNNs)** untuk data gambar atau **Recurrent Neural Networks (RNNs)** untuk data sekuensial seperti teks.
Based on this analogy:
![image15.png](Copy of Deep Learning_images/image15.png)
Single Neuron Entity of Neural Network
Size adalah Input yang akan di pertimbangkan untuk Neural Network.
Circle adalah Proses Neural Network, atau proses Deep Learning, in this case menggunakan Function ReLU (Rectified Linear Unit).
Final Price adalah Output yang di hasilkan setelah melewati proses Deep Learning.
## Neural Network yang lebih besar terbentuk dari stacking atau Gabungan dari banyak Single Neuron
Salah satu metode pendekatan Deep Learning adalah Supervised Learning
Dalam **supervised learning**, model deep learning dilatih menggunakan data yang **dilabeli**. Ini berarti setiap contoh data yang digunakan untuk pelatihan memiliki **input (fitur)** dan **output yang diketahui (label)**. Tujuannya adalah agar model dapat mempelajari hubungan antara input dan output, sehingga dapat memprediksi output yang benar untuk data baru yang tidak dilabeli.
Didalam pendekatan Supervised Learning terdapat beberapa arsitektur model untuk menerapkannya, yaitu:
**Convolutional Neural Networks (CNN)** untuk pengenalan gambar,
**Recurrent Neural Networks (RNN)** atau **Transformer** untuk pemrosesan bahasa alami (NLP),
**Feed-forward neural networks** atau **Standard Neural Network** untuk regresi dan klasifikasi.
Didalam pendekatan Supervised Learning juga terdapat 2 jenis data, yaitu:
Structured Data adalah jenis data yang **terorganisir** dengan baik dalam format yang **terdefinisi** dengan jelas, seperti tabel dalam database atau spreadsheet. Structured data disusun dalam bentuk yang dapat dengan mudah diidentifikasi, diakses, dan diproses oleh algoritma machine learning.
Unstructured Data adalah data yang **tidak terorganisir** secara rapi dalam format tabel yang terstruktur, dan tidak mudah dipetakan ke kolom dan baris. Data ini biasanya berupa **data tidak terstruktur** seperti teks, gambar, audio, dan video.
## Binary Classification
**Binary classification** adalah jenis tugas **klasifikasi** di mana model dilatih untuk **memprediksi salah satu dari dua kelas**. Dalam binary classification, output dari model biasanya dibatasi pada dua kategori, yang seringkali dilambangkan sebagai:
**Kelas 0** atau **Kelas 1**
**Negatif** atau **Positif**
**False** atau **True**
**Tidak** atau **Ya**
**Contoh Binary Classification**
**Deteksi Spam: **Mengklasifikasikan apakah sebuah email adalah spam (1) atau bukan spam (0).
**Deteksi Penyakit:** Memprediksi apakah seseorang memiliki penyakit (1) atau tidak (0) berdasarkan data medis.
**Analisis Kredit:** Memprediksi apakah seseorang akan membayar pinjaman (1) atau tidak akan membayar (0) berdasarkan profil keuangan.
Salah satu metode Binary Classification yang sangat umum digunakan adalah Logistic Regression. Logistic regression bekerja dengan memodelkan hubungan antara fitur-fitur input dan kelas output menggunakan fungsi sigmoid, yang membatasi output menjadi rentang antara 0 dan 1. Output ini kemudian diinterpretasikan sebagai probabilitas.
**Cost function** dalam logistic regression digunakan untuk mengukur seberapa baik model memprediksi output (kelas 0 atau 1) dibandingkan dengan label sebenarnya. Tujuan utama dari cost function adalah memberikan sebuah nilai yang bisa kita minimalkan untuk membuat model lebih akurat. Dalam logistic regression, model menghasilkan probabilitas bahwa contoh data termasuk dalam kelas 1. Cost function membantu menghitung error berdasarkan seberapa jauh probabilitas prediksi dari nilai sebenarnya (0 atau 1).
**Gradient Descent** adalah salah satu algoritma optimisasi yang paling umum digunakan dalam machine learning, termasuk dalam logistic regression. Gradient descent digunakan untuk meminimalkan cost function, yaitu fungsi yang mengukur kesalahan model (seperti dalam logistic regression).
Bayangkan cost function sebagai permukaan atau lembah yang kita ingin turun sampai mencapai titik terendah (minimum). Gradient descent membantu kita menemukan titik terendah ini dengan bergerak sedikit demi sedikit menuju arah di mana cost function paling cepat menurun.
**Derivatives (Turunan)**
Turunan atau derivatif adalah konsep dalam kalkulus yang digunakan untuk mengukur seberapa cepat sebuah fungsi berubah. Dalam konteks machine learning, turunan memberi tahu kita bagaimana perubahan kecil dalam input (misalnya, bobot 𝑤 w) akan mempengaruhi output (misalnya, cost function 𝐽 ( 𝑤 ) J(w)).
**Computation Graph (Graf Perhitungan)**
**Computation Graph** adalah **diagram** yang menggambarkan langkah-langkah komputasi yang diperlukan untuk menghitung fungsi yang kompleks. Ini adalah alat visual yang digunakan untuk **melacak bagaimana fungsi dibangun** dari operasi-operasi sederhana, seperti penjumlahan, perkalian, dan aplikasi fungsi non-linear (misalnya, sigmoid atau ReLU).
Dalam konteks **deep learning**, computation graph sangat berguna untuk **backpropagation**, yaitu algoritma yang digunakan untuk menghitung gradien (turunan) secara efisien melalui jaringan saraf.
**Vectorization**
Vectorization adalah teknik di mana kita mengonversi perhitungan atau operasi matematika yang biasanya dilakukan dalam **loop** menjadi operasi pada **vektor atau matriks**. Ini adalah salah satu kunci untuk membuat algoritma machine learning dan deep learning berjalan **lebih cepat** dan **lebih efisien**, terutama ketika bekerja dengan data yang besar.
**for loop vs Vectorization using NumPy library** Baik menggunakan **loop manual** (for loop) atau menggunakan **NumPy**, hasil akhir dari perhitungan akan **sama** dalam hal **nilai numerik**. Ini karena keduanya melakukan operasi matematika yang sama, tetapi perbedaannya terletak pada efisiensi dan kecepatan
![image9.png](Copy of Deep Learning_images/image9.png)
using for loop
![image2.png](Copy of Deep Learning_images/image2.png)
using vectorization with NumPy untuk menghindari penggunaan for loop
**Broadcasting in Pyhton**
**Broadcasting** di Python (khususnya dalam **NumPy**) adalah fitur yang sangat berguna yang memungkinkan **operasi aritmatika** dilakukan pada **array dengan ukuran yang berbeda** tanpa perlu menulis kode secara eksplisit untuk menangani perbedaan ukuran tersebut. Broadcasting secara otomatis memperluas dimensi array yang lebih kecil agar sesuai dengan array yang lebih besar sehingga operasi dapat dilakukan dengan **efisien** dan **tanpa error**
**Aturan pada Broadcasting**
Untuk memahami **broadcasting**, kita perlu memahami aturan dasarnya, yaitu bagaimana NumPy menangani array dengan ukuran yang berbeda. Ada dua aturan penting dalam broadcasting:
**Jika dua array memiliki jumlah dimensi yang berbeda**, maka NumPy akan **menambahkan dimensi baru di depan array yang lebih kecil** sampai kedua array memiliki jumlah dimensi yang sama.
**Jika ukuran array di sepanjang dimensi tertentu berbeda**:
Jika salah satu dari dua array memiliki ukuran **1** di suatu dimensi, NumPy akan memperluas array tersebut di sepanjang dimensi itu sehingga ukurannya sama dengan array lainnya.
Jika ukuran array di sepanjang dimensi tertentu **tidak sama** dan **bukan 1**, maka NumPy akan memberikan error karena tidak dapat melakukan broadcasting.
Contoh penambahan Array biasa
![image1.png](Copy of Deep Learning_images/image1.png)
dimensi array sama, broadcasting tidak diperlukan
![image4.png](Copy of Deep Learning_images/image4.png)
disini skalar di perluas menjadi ukuran yang sama dengan a sehingga operasi penambahan bisa dilakukan.
## Single Layer Neural Network
Dalam **single layer neural network**, ada hanya **satu lapisan neuron** yang terhubung langsung dari **lapisan input** ke **lapisan output** tanpa lapisan tersembunyi (hidden layer). Contoh dalam NumPy:
![image3.png](Copy of Deep Learning_images/image3.png)
Dalam contoh di atas:
**X** adalah input (fitur-fitur), yaitu jumlah kata dan URL.
**W** adalah bobot yang akan dioptimalkan selama pelatihan.
**b** adalah bias.
**Fungsi sigmoid** digunakan untuk menghitung probabilitas.
**Hidden Layer**
**Hidden layer** (lapisan tersembunyi) adalah **lapisan neuron** dalam neural network **tiruan** (**artificial neural network**) yang berada **di antara lapisan input** (input layer) dan **lapisan output** (output layer). Lapisan tersembunyi ini disebut **"tersembunyi"** karena neuron-neuronnya **tidak terlihat langsung** oleh data input maupun oleh output akhir; mereka hanya berfungsi sebagai **intermediate layer** (lapisan perantara) yang mengolah informasi dari input sebelum menghasilkan output.
Hidden layer berperan penting dalam neural network, terutama dalam **deep learning**, karena mereka memungkinkan model untuk **mempelajari pola non-linear** dan **kompleks** dalam data.
Contoh pada NumPy:
![image11.png](Copy of Deep Learning_images/image11.png)
![image10.png](Copy of Deep Learning_images/image10.png)

Penjelasan:
**W_hidden**: Bobot untuk 3 neuron di hidden layer yang menerima 2 input.
**b_hidden**: Bias untuk masing-masing neuron di hidden layer.
**relu()**: Fungsi aktivasi ReLU diterapkan pada hasil dari hidden layer.
**W_output** dan **b_output**: Bobot dan bias dari hidden layer ke lapisan output.
**sigmoid()**: Fungsi aktivasi di lapisan output yang menghasilkan probabilitas prediksi.
## Hubungan Activation Function, Non-Linear Activation dan Derivatives of Activation Function
**Activation function**, **derivatives (turunan)**, dan **non-linear activation function** sangat berhubungan erat dan **tidak bisa dipisahkan** dalam konteks neural networks dan **deep learning**. Mereka bekerja **bersama-sama** untuk memungkinkan **pembelajaran** yang efektif di dalam neural network.
**Fungsi aktivasi** digunakan di setiap neuron dalam neural network untuk mentransformasikan input dari lapisan sebelumnya.
**Fungsi turunan** dari aktivasi digunakan dalam **backpropagation** untuk menghitung **gradien** yang diperlukan untuk memperbarui bobot. Tanpa turunan fungsi ini, jaringan tidak bisa belajar.
**Fungsi aktivasi non-linear** diperlukan untuk memungkinkan jaringan saraf belajar **pola-pola yang kompleks dan non-linear**. Jika hanya fungsi linear yang digunakan, jaringan saraf akan sangat terbatas dalam kemampuannya.
Bagaimana Penerapannya dalam Deep Learning
**Activation function** diterapkan pada setiap lapisan, terutama pada **lapisan tersembunyi**. Lapisan-lapisan ini akan memproses dan mentransformasikan input melalui fungsi aktivasi non-linear untuk menghasilkan representasi fitur yang lebih abstrak dan bermanfaat.
**Turunan fungsi** dari aktivasi digunakan selama **backpropagation** untuk menghitung bagaimana bobot di setiap lapisan harus diperbarui, sehingga jaringan dapat belajar dari kesalahan.
**Non-linear activation function** (seperti **ReLU**, **tanh**, atau **sigmoid**) memungkinkan **deep learning** bekerja pada masalah yang sangat kompleks, seperti pengenalan gambar, pemrosesan bahasa alami, atau prediksi suara, yang tidak bisa dilakukan oleh model linear.
## Proses Training Deep Learning
**Forward propagation** dan **backpropagation** adalah dua langkah inti dalam proses pelatihan jaringan saraf. Forward propagation digunakan untuk menghitung prediksi, sementara backpropagation digunakan untuk memperbaiki prediksi dengan memperbarui bobot berdasarkan error.
**Random initialization** memastikan bahwa bobot jaringan tidak semuanya dimulai dari nol, memungkinkan pembelajaran yang lebih efektif.
**Parameter** (bobot dan bias) dioptimalkan selama pelatihan, sementara **hyperparameter** seperti **learning rate** dan **jumlah lapisan** harus ditentukan sebelum pelatihan.
**Matrix dimensions** yang tepat sangat penting untuk memastikan bahwa operasi matematis berjalan lancar di setiap lapisan.
Proses pelatihan berulang dalam beberapa **epoch** hingga model dapat membuat prediksi yang akurat berdasarkan data yang diberikan.
# Course 2
## Summary
### Train, Test and Dev Sets
Dalam Machine learning dan Deep learning terdapat 3 pelatihan penting untuk modeling
Train Set
**Train set** adalah bagian dari dataset yang digunakan untuk **melatih model**. Model belajar **pola-pola** dari data ini dengan **menyesuaikan parameter** seperti bobot dan bias di setiap iterasi (melalui **forward propagation** dan **backpropagation**).
Biasanya, **70%-80%** dari keseluruhan data dialokasikan sebagai train set.
Dev Set
**Dev set** atau **validation set** adalah bagian dari dataset yang digunakan untuk **mengevaluasi model selama pelatihan** dan melakukan **tuning hyperparameter**.
Biasanya, **10%-20%** dari data dialokasikan untuk dev set.
Test Set
**Test set** adalah bagian dari dataset yang digunakan **hanya setelah pelatihan selesai** untuk mengevaluasi **seberapa baik model dapat menggeneralisasi** pada data yang belum pernah dilihat sebelumnya. Test set digunakan **sekali** di akhir pelatihan untuk memberikan **indikasi kinerja akhir** model.
**Biasanya, 10%-20%** dari dataset dialokasikan untuk test set.
### Bias/Variance
Bias (Bias Model)
**Bias** mengacu pada **seberapa baik model bisa belajar pola dari data**. Bias tinggi berarti model membuat **asumsi yang kuat dan sederhana** tentang data, sehingga tidak cukup fleksibel untuk menangkap **pola-pola yang kompleks** dalam data.
**Ciri-Ciri** Model dengan **Bias Tinggi**:
Kinerja yang buruk pada **train set** dan **dev set**.
Model gagal **belajar pola dari data** dengan baik, sehingga prediksi model tidak akurat baik di data pelatihan maupun data baru.
Variance (Varians Model)
**Variance** mengacu pada **seberapa banyak prediksi model berubah** ketika diberikan **dataset yang berbeda**. Variance tinggi berarti model **terlalu sensitif** terhadap **perubahan kecil** dalam data, sehingga model cenderung **overfitting** terhadap data pelatihan.
**Ciri-Ciri** Model dengan **Variance Tinggi**:
Kinerja yang sangat baik pada **train set** tetapi buruk pada **dev set** atau **test set**.
Model terlalu menyesuaikan diri dengan data pelatihan dan tidak bisa **menggeneralisasi** ke data baru dengan baik.
Regularization
**Regularization** adalah teknik yang digunakan untuk **mengurangi overfitting** dengan membatasi **kompleksitas model**. Regularization membantu menjaga keseimbangan antara **bias dan variance** dengan menambahkan **penalti** pada model untuk parameter yang terlalu besar atau kompleks.
regularization biasanya dilakukan dengan menambahkan **penalti** pada **bobot** yang terlalu besar dalam model, sehingga mencegah model untuk menjadi terlalu kompleks dan overfitting terhadap data pelatihan.
**Regularization** adalah teknik yang digunakan untuk **mengurangi overfitting**, yaitu ketika model menjadi terlalu kompleks dan terlalu cocok dengan data pelatihan, sehingga gagal menggeneralisasi ke data baru.
**L2 regularization** adalah salah satu teknik yang umum digunakan, di mana bobot besar diberikan penalti dalam fungsi loss, sehingga model cenderung menjaga bobotnya tetap kecil dan sederhana. **Dropout regularization** adalah teknik lain di mana, selama pelatihan, beberapa neuron dipilih secara acak untuk dihilangkan sementara waktu. Ini mencegah model terlalu bergantung pada neuron tertentu, membuat model lebih robust dan mengurangi kemungkinan overfitting. Regularization secara keseluruhan membantu menjaga model tetap sederhana dan bisa menggeneralisasi lebih baik.
Normalizing Input dan Normalizing Activations **Normalizing input** adalah langkah penting untuk memastikan bahwa semua fitur input memiliki **skala yang seragam**, sehingga mempermudah pelatihan model. Normalisasi input dilakukan dengan mengubah fitur input agar memiliki rata-rata 0 dan standar deviasi 1. Hal ini membantu mempercepat proses pelatihan, karena model tidak perlu menangani input yang berada pada skala yang sangat berbeda. **Normalizing activations** pada jaringan saraf juga penting, terutama di jaringan yang lebih dalam. **Batch normalization**, sebagai contoh, memastikan bahwa output dari setiap lapisan tersembunyi tetap berada dalam skala yang tepat, sehingga menjaga pelatihan tetap stabil. Normalisasi ini penting untuk mencegah masalah **vanishing** atau **exploding gradients**, yang sering terjadi ketika jaringan memiliki banyak lapisan.
Vanishing/Exploding Gradients dan Weight Initialization Dalam jaringan yang sangat dalam, masalah **vanishing** dan **exploding gradients** dapat terjadi selama proses pelatihan. **Vanishing gradients** terjadi ketika gradien menjadi sangat kecil, sehingga bobot tidak diperbarui dengan cukup cepat, membuat pelatihan berhenti atau berjalan sangat lambat. Sebaliknya, **exploding gradients** terjadi ketika gradien menjadi sangat besar, menyebabkan pembaruan bobot yang berlebihan dan pelatihan menjadi tidak stabil. Salah satu cara untuk mengatasi masalah ini adalah melalui **weight initialization** yang tepat. Metode seperti **He initialization** atau **Xavier initialization** digunakan untuk memastikan bahwa bobot diinisialisasi dengan skala yang tepat, sehingga gradien tetap stabil dan pelatihan dapat berlangsung dengan baik.
Learning rate decay adalah teknik di mana learning rate secara bertahap dikurangi selama pelatihan. Pada awal pelatihan, learning rate yang lebih besar membantu model untuk belajar lebih cepat. Namun, ketika model semakin dekat ke solusi optimal, learning rate dikurangi agar pembaruan bobot menjadi lebih halus dan tidak melompat terlalu jauh dari solusi yang tepat. Tuning process juga melibatkan pemilihan hyperparameter lainnya, seperti jumlah lapisan tersembunyi, jumlah neuron, dan regularization strength. Dengan melakukan tuning secara tepat, kita dapat menemukan konfigurasi model yang optimal untuk data yang digunakan, memastikan bahwa model dapat bekerja dengan baik tanpa underfitting atau overfitting.
