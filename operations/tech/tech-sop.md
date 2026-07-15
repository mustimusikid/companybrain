---
title: Tech Sop
domain_tag: [operations, tech]
doc_type: sop
owner: tech_head
status: Unknown
confidentiality: Internal
source: gdrive
review_frequency: annually
---

> Technical documentation or automation workflow for Musti Musik systems.

PLAYBOOK TECH
![image105.png](Tech SOP_images/image105.png)
![image107.png](Tech SOP_images/image107.png)

SOP TECH

## GENERAL
**Produk ****Musti**** Musik**
Color Palette
HEX : #3a2d1b
![image109.png](Tech SOP_images/image109.png)
HEX : #a66f2e
![image98.png](Tech SOP_images/image98.png)
HEX : #f0ad4e
![image57.png](Tech SOP_images/image57.png)

## LOGIN ADMIN
### Login cPanel :
Buka (Cpanel), lalu log in.
Setelah itu, scroll ke paling bawah dan pilih Wordpress (melalui Softaculous)
![image59.png](Tech SOP_images/image59.png)
Scroll ke bawah dan pilih login as admin di-web yang diinginkan
![image72.png](Tech SOP_images/image72.png)
### Login Wordpress :
Landing Page :
Username : mustimusik
Password : mustimusik123
Member Area :
Username : admin
Password : wGRbH&5iK2

## CARA MENGGUNAKAN ELEMENTOR
Pilih page yang ingin di-edit
![image75.png](Tech SOP_images/image75.png)
Klik Edit with Elementor
![image31.png](Tech SOP_images/image31.png)
Drag and drop fitur-fitur di sebelah kiri ke website
![image33.png](Tech SOP_images/image33.png)
Hover pada divider-divider section di website untuk mendapatkan opsi Add Section
![image32.png](Tech SOP_images/image32.png)
Klik tanda tambah untuk menambah struktur
![image35.png](Tech SOP_images/image35.png)
Klik kiri pada bagian abu-abu untuk menambahkan kolom pada struktur
![image34.png](Tech SOP_images/image34.png)
Cek responsive pada dimensi berbeda dengan menggunakan Responsive Mode di bagian kiri bawah dan klik Update jika ingin menyimpan dan publish edit pada website
![image42.png](Tech SOP_images/image42.png)

## CARA MENAMBAHKAN & MENGHAPUS USER
Pada dashboard /wp-admin, klik Users dan pilih Add New User untuk menambahkan user secara manual.
![image40.png](Tech SOP_images/image40.png)
Isi kolom-kolom required dan berikan role sesuai kebutuhan.
Administrator: full access pada dashboard dan dapat mengedit
Subscriber: akun member biasa tanpa akses apapun. Untuk memberi akses pada memberarea, member tetap harus melakukan checkout product.
![image45.png](Tech SOP_images/image45.png)
Subscriber, Pro: akun member yang sudah daftar & sudah checkout product, serta memiliki akses ke modul-modul kelas.
![image44.png](Tech SOP_images/image44.png)

![image47.png](Tech SOP_images/image47.png)
Untuk menghapus akun, pilih All Users pada dashboard dan klik Delete pada akun yang ingin dihapus

### MEMBER AREA: CARA MENAMBAHKAN MODUL (COURSE)
Membuat Courses menggunakan Tutor LMS Pro
Melalui dashboard, arahkan kursor ke Tutor LMS Pro, lalu klik “Courses”.
![image24.png](Tech SOP_images/image24.png)
Klik + Add New pada pojok kiri atas
![image23.png](Tech SOP_images/image23.png)
Lalu tambahkan nama modul sesuai Modul yang akan dibuat, sebagai contoh “TEST COURSE”
![image26.png](Tech SOP_images/image26.png)
Scroll ke bawah, lalu setel course type menjadi “Paid”
![image25.png](Tech SOP_images/image25.png)
Lalu buat product terlebih dahulu untuk menentukan harga yang akan di setel pada course tersebut. Untuk membuat product, pada tab sebelah kiri arahkan ke Products > Add New.
![image28.png](Tech SOP_images/image28.png)
Samakan nama product dengan nama course yang kita buat, yaitu sebagai contoh tadi “TEST COURSE”.
![image27.png](Tech SOP_images/image27.png)
Scroll ke bawah, lalu setel pada kolom “Regular Price” sesuai dengan yang telah ditentukan, misalnya “Rp 30.000,-”. Kosongkan kolom “Sale Price”. Pada kolom “Tax Status” setel menjadi “None”. Dan pada kolom “Tax class” setel menjadi “Zero rate”.
![image30.png](Tech SOP_images/image30.png)
Scroll ke bawah dan tekan button “Publish” untuk create product.
![image29.png](Tech SOP_images/image29.png)
Lalu kembali lagi ke laman course, yaitu Tutor LMS Pro > Courses > TEST COURSE. Scroll ke bawah, lalu setel “Course Type” menjadi “Paid”. Pada kolom “Select Product” search nama product yang telah kita buat tadi, yaitu “TEST COURSE”, lalu pilih dan tampilannya akan muncul seperti ini beserta harga nya.
![image1.png](Tech SOP_images/image1.png)
Lalu scroll ke bawah untuk menambahkan pelajaran pada Course ini. Pada bagian “Course Builder”, Klik “Add New Topic”.
![image3.png](Tech SOP_images/image3.png)
Setelah mengklik “Add New Topic” akan muncul modal “Add Topic”. Lalu tambahkan BAB pada course builder tersebut, sebagai contoh “BAB 1”. Lalu tekan button “Add Topic”.
![image2.png](Tech SOP_images/image2.png)
Setelah BAB 1 terbuat, tekan button “+ Lesson” untuk menambahkan pelajaran pada BAB 1 tersebut.
![image5.png](Tech SOP_images/image5.png)
Setelah menekan button “+ Lesson”, akan muncul modal bernama “Lesson” untuk menambahkan pelajaran baru pada BAB tersebut. Kita beri contoh nama pelajaran tersebut sebagai “Pelajaran 1”.
![image4.png](Tech SOP_images/image4.png)
Scroll ke bawah untuk menambahkan link video beserta dokumen apabila pada pelajaran tersebut terdapat video & dokumen yang akan disertakan. Pilih “Youtube” untuk memasukkan link url, karena biasanya mustimusik memberikan video pembelajaran melalui YouTube. Apabila ada dokumen yang perlu disertakan pada pelajaran tersebut, tekan button “Upload Attachment”. Setelah semua selesai tekan button “Update Lesson”.
![image7.png](Tech SOP_images/image7.png)
Scroll ke bawah untuk memberikan thumbnail pada course tersebut agar terlihat bagus. Apabila thumbnail belum tersedia, kamu bisa meminta tolong kepada tim design untuk membuatkannya. Klik “Set featured image”, lalu upload thumbnail yang sesuai dengan course tersebut.
![image6.png](Tech SOP_images/image6.png)
Scroll lagi ke atas, hingga kamu menemukan button “Publish” di sebelah kanan. Tekan button “Publish” dan course telah terbuat.
![image15.png](Tech SOP_images/image15.png)

## MEMBER AREA: CARA MENGATUR KUPON
Pada arahkan ke Marketing > Coupons.
![image142.png](Tech SOP_images/image142.png)
Di pojok kiri atas klik “Add coupon”
![image141.png](Tech SOP_images/image141.png)
Masukan nama kupon sebagai judul (misalnya TESTKUPON30) dan tentukan tipe potongan.
Dibawah judul kupon terdapat button “Generate coupon code”, yang dimana jika kamu ingin generate kode kupon.
Dibawah button “Generate coupon code” merupakan deskripsi mengenai kupon, disini kita isi sebagai “Test kupon diskon sebesar 30%”.
Pada Tab “Coupon data” di bagian “General”, kamu bisa mengisikan bagian “Discount type” dengan nilai “Percentage discount” yang artinya kamu memilih potongan dalam nilai % (persentase).
Pada bagian “Coupon amount” isikan nilai “30” yang artinya kamu ingin membuat kupon ini memiliki nilai potongan diskon sebesar 30%. Jika kamu ingin menyetel potongan sebesar 50% maka isi bagian “Coupon amount” dengan nilai “50”.
Pada bagian “Coupon expiry date” kamu bisa mengisikan tanggal berapapun untuk masa berlaku kupon tersebut. Jika kamu ingin menyetel kupon tersebut agar tidak memiliki masa berlaku, maka kosongkan bagian “Coupon expiry date”.
![image142.png](Tech SOP_images/image142.png)
Pada bagian “Usage Restriction”, isikan kolom “Products” dengan produk yang ingin kamu berikan potongan harga, sebagai contoh disini saya memberikan potongan untuk product bernama “AKADEMI MUSTI MUSIK MEMBERSHIP”.
![image144.png](Tech SOP_images/image144.png)
Pada bagian “Usage Limits” di kolom “Usage limit per coupon” disini kamu bisa mengatur jumlah kupon yang bisa digunakan. Misalkan kamu ingin mengatur agar kupon TESTKUPON30 ini hanya bisa digunakan oleh 100 orang, maka set “100” pada kolom “Usage limit per coupon”. Jika kamu ingin membiarkan kupon ini unlimited/tidak memiliki batasan pemakaian, maka kosongkan kolom tersebut. Jika telah selesai semua, klik button “Publish” di bagian kanan.
![image143.png](Tech SOP_images/image143.png)

## MEMBER AREA: CARA VERIFIKASI PEMBAYARAN
Pada dashboard member area, Arahkan kursor ke WooCommerce > Orders.
![image146.png](Tech SOP_images/image146.png)
Cari user yang memiliki status payment “Cancelled” atau “Pending Payment”. Dengan catatan apabila pembayaran terdapat masalah atau kendala lain, sementara uang sudah masuk ke rekening Dave Henokh (konfirmasi dengan tim CS). Lalu klik user tersebut.
![image145.png](Tech SOP_images/image145.png)
Klik pada dropdown “status” dan ubah menjadi “Completed”. Setelah selesai, klik button “Update” di pojok kanan atas.
![image148.png](Tech SOP_images/image148.png)

## LANDING PAGE: CARA DUPLICATE PAGE
Masuk ke menu page pada dahsboard landing page,
![image75.png](Tech SOP_images/image75.png)
Pilih page yang ingin diduplikat dan klik EA Duplicator. Maka page tersebut akan terduplikat seperti yang bisa dilihat di bawah menjadi “Landing Page - Copy”. Klik “Landing Page - Copy” tersebut, lalu anda dapat memodifikasi sesuai keinginan anda.
![image149.png](Tech SOP_images/image149.png)

## LANDING PAGE: CARA MEMBUAT, MEMASUKKAN, DAN MENGAKSES FORM DI LP
Pada dashboard, pilih Forminator > Dashboard
![image139.png](Tech SOP_images/image139.png)
Klik create untuk membuat form baru atau duplicate dari form yang sudah ada. Buat pertanyaan sesuai kebutuhan
![image132.png](Tech SOP_images/image132.png)
Atur Submission Behaviour untuk menampilkan link grup untuk membagikan link free class
![image131.png](Tech SOP_images/image131.png)
Setelah selesai klik Update dan klik Copy Shortcode pada setting form
![image134.png](Tech SOP_images/image134.png)
Masuk ke lama Elementor page tempat form ingin dimasukan. Pilih widget Shortcode, drag and drop ke website
![image133.png](Tech SOP_images/image133.png)
Paste shortcode dari Forminator dan form siap digunakan
![image136.png](Tech SOP_images/image136.png)
Data pengisi form dapat diakses melalui dashboard LP > forminator > submissions.
![image135.png](Tech SOP_images/image135.png)

## MAILKETING: CARA MENAMBAHKAN EMAIL FORWARDER
Mailketing:, Email: davehenokh@gmail.com, Password: @MustiMusik1d
Masuk ke menu *Setup Domain > Tambah Domain > +Whitelabel Sender* untuk membuat email domain baru
![image140.png](Tech SOP_images/image140.png)
Masukan nama email domain yang ingin dibuat dan klik next hingga submit
![image120.png](Tech SOP_images/image120.png)
Masuk ke menu *Setup Domain > Email Forwarder > Add Forwarder*
![image119.png](Tech SOP_images/image119.png)
Masukan email domain yang ingin di-forward dan email tujuan forward.
![image112.png](Tech SOP_images/image112.png)

## MAIL: CARA MENAMBAHKAN EMAIL DOMAIN KE GMAIL

## CPANEL: CARA MEMBUAT SUBDOMAIN (SUBDOMAIN.MUSTIMUSIK.ID)
CPanel Musti Musik:
Username: davehenokh
Email: davehenokh@gmail.com
Password: zpG05=]FC^N$

Masuk ke menu Domains > Create A New Domain
![image116.png](Tech SOP_images/image116.png)
Masukan nama domain yang ingin dibuat dan jangan centang Share Document Root. Klik Submit.
![image115.png](Tech SOP_images/image115.png)

## CAREERS: MENAMBAH LOWONGAN PEKERJAAN (MUSTIMUSIK.ID/CAREERS)
Jika perlu menambahkan lowongan pekerjaan, maka hal yang harus dilakukan adalah:
Buat subpage (duplicate aja dari lowongan sebelumnya) dari dengan link sesuai dengan lowongan yang dibutuhkan. Misalnya, jika dibutuhkan web developer, buat subpage. Cara membuat subpage sama seperti page biasa tapi dibagian page attributes masukin parent page-nya. Misalnya subpage careers seperti ini:
![image82.png](Tech SOP_images/image82.png)
Ganti isi dan deskripsinya menggunakan elementor.
Tambahkan card job openings di dan
![image85.png](Tech SOP_images/image85.png)

## CARA MEMBUAT AKUN UNTUK USER & CHECKOUT PAKET
Video Tutorial Cara Menambahkan User & Checkout Paket
Berikut merupakan video tutorial mengenai cara menambahkan user & checkout di

## TUTORLMS SETUP
Arahkan kursor ke Tutor LMS Pro > Settings.
![image64.png](Tech SOP_images/image64.png)
Di dalam settings, anda akan melihat beberapa navigation bar yang terdiri dari General, Course, Monetization, dll. Klik pada bagian “Course” (disini kita hanya akan melakukan setup yang penting saja).
![image63.png](Tech SOP_images/image63.png)
Pada gambar diatas di bagian “Course Visibility”, “Course Content Access”, “Content Summary”, “Spotlight Mode” geser toggle ke kanan yang berarti “on”.
Pada bagian “Auto redirect to courses” bisa kamu set sesuai keinginan, apakah user akan diarahkan langsung ke course atau ke thank you page terlebih dahulu setelah melakukan pembayaran.
Lalu beralih ke bagian “Advance” lalu scroll hingga menemukan bagian “Options”
![image52.png](Tech SOP_images/image52.png)
Pada bagian “Enable Tutor Login” set toggle menjadi on. Hal ini agar pada tampilan login di tidak menggunakan tampilan default login dari wordpress, melainkan tampilan login yang telah disediakan oleh TutorLMS.
Pada bagian “Maintenance Mode”, kamu bisa memodifikasi sesuka kamu apabila website sedang dalam development atau maintenance, kamu bisa mengaktifkan fitur tersebut jika kamu mau.
Beralih ke bagian “Authentication” scroll ke bawah hingga kamu menemukan bagian “Manage Active Login Session”.
![image53.png](Tech SOP_images/image53.png)
Pada bagian “Limit Active Login Sessions” set toggle menjadi on.
Pada bagian “Maximum Active Sessions” set menjadi “2”. Ini berarti bahwa agar user bisa login di 2 device, yaitu Smartphone dan Laptop. Apabila “Limit Active Login Sessions” dan “Maximum Active Sessions” tidak diaktifkan maka user hanya bisa login pada akun mereka di satu device saja.

## CARA MEMBUAT COURSE BUNDLE
Pergi ke halaman , arahkan kursor ke Tutor LMS Pro > Course Bundles.
![image20.png](Tech SOP_images/image20.png)
Pada halaman Course Bundles, di pojok kiri atas klik “+ Add New”.
![image19.png](Tech SOP_images/image19.png)
Berikan Judul sesuai dengan Course Bundle yang ingin anda buat. Sebagai contoh kita beri nama course bundle ini sebagai “AKADEMI COURSE BUNDLE TEST”.
![image18.png](Tech SOP_images/image18.png)
Scroll ke bawah, lalu anda akan menemukan dropdown “Select Courses”. Pilihlah course yang sesuai yang akan anda masukkan ke dalam course bundle tersebut.
![image17.png](Tech SOP_images/image17.png)
Scroll lagi ke bawah, pada bagian “Bundle Sale Price” set harga untuk course bundle ini dengan harga yang telah ditentukan oleh tim & perusahaan. Sebagai contoh disini saya memberikan harga sebesar “Rp900.000,-”. Setelah selesai, klik button “Publish” yang berada di kanan.
![image11.png](Tech SOP_images/image11.png)

## CARA MEMBUAT CUSTOM FUNCTION DI functions.php
Arahkan kursor ke Appearance > Theme File Editor.
![image10.png](Tech SOP_images/image10.png)
Setelah masuk ke halaman Theme File Editor, di sebelah kanan terdapat direktori dan silahkan klik pada functions.php
![image9.png](Tech SOP_images/image9.png)
Scroll ke bawah pada code-code tersebut. Lalu anda bisa melihat bahwa ada custom code untuk menampilkan tampilan My Profile, Enrolled Course, Purchase History, dll.
![image8.png](Tech SOP_images/image8.png)
![image13.png](Tech SOP_images/image13.png)
![image12.png](Tech SOP_images/image12.png)
Jika anda perhatikan baik-baik, setiap custom function yang dibuat dibawahnya memiliki method “add_shortcode()”, nah disinilah kita akan menyimpan potongan code ini ke halaman yang kita inginkan.
Kita lihat pada contoh function untuk “Purchase History” yaitu kita namakan “custom_purchase_history_shortcode()”. Lalu dibawahnya ada shortcode yang dinamakan “custom_tutor_purchase_history”.
Kita panggil shortcode tersebut ke halaman “Purchase History”, yaitu arahkan kursor ke Pages > All Pages > Purchase History.
![image71.png](Tech SOP_images/image71.png)
![image80.png](Tech SOP_images/image80.png)
Pada Halaman “Purchase History” kita tempelkan shortcode tersebut yaitu dengan sintaks berikut “[custom_tutor_purchase_history]”. Di halaman ini anda bisa melihat ada pilihan “Visual” dan “Text”. Pilihlah “Text” lalu tempelkan shortcode “[custom_tutor_purchase_history]” di field tersebut. Setelah itu jangan lupa scroll ke bawah lalu tekan button “Update”. Hasilnya akan terlihat di halaman Member Area.
![image79.png](Tech SOP_images/image79.png)
Melalui custom function di functions.php, kita bisa mengcustom apapun sesuai kebutuhan kita di masa depan. Anda bisa mengaplikasikan tutorial ini untuk page apapun.
![image78.png](Tech SOP_images/image78.png)

## MANUAL ENROLLMENT UNTUK USER YANG TELAH MEMILIKI AKUN, NAMUN BELUM MELAKUKAN CHECKOUT.
Silahkan tekan & lihat video tutorial ini, atau langsung kunjungi Google Drive Musti Musik pada folder bernama “Tutorial”.

## CARA BUAT AKUN BARU MEMBER PRO DAN BASIC

Siapkan Identitas Member yang akan didaftarkan, minimal ada nama, email, dan nomor HP.
Buka, Klik Register now, Masukan identitas user yang sudah disiapkan seperti username, email dll, setelah itu klik tombol register
Masukan kembali akun yang sudah di buat sebelumnya, lalu akan dashboard yang berisi 0 course (karena belum di enroll)
Selanjutnya Masuk ke, masukan username dan password berikut :
username: admin
password: wGRbH&5iK2
Setelah itu Masuk ke menu Tutor LMS Pro, lalu pilih Enrollment
![image43.png](Tech SOP_images/image43.png)
Setelah itu Klik Enroll a student untuk memberikan coursenya
![image41.png](Tech SOP_images/image41.png)
Setelah itu pada kolom select a course/bundle, masukan bundle ”Akademi Musti Musik Membership” jika member PRO ”Membership Musti Musik Basic Course Bundle” jika member BASIC
Pada kolom Search a Student Masukan Username atau Email yang barus saja di daftarkan
Setelah itu tunggu beberapa saat hingga muncul banner Succes dan klik tombol View Order di banner tersebut
Selanjutnya akan di arahkan ke Pengaturan Order dari, Klik saja Orderan yang baru dibuat yang paling atas dengan status “Pending Payment”
Setelah itu ubah statusnya menjadi complete dan masukan Kode Coupon, sebagai berikut :
Coupon Member PRO : JA4TYJCC
Coupon Member Basic : VTUXZAVB
Setelah coupon di masukan dan status order di set complete, klik update untuk memperbarui orderan
Curse berhasil di enroll, kembali ke dashboard akun yang sudah dibuatkan, lalu refresh browser dan course akan bertambah, setelah itu jangan lupa untuk logout akun agar tidak terkenal limit user logged in.

### Cara Install Tracker Sales Page di Orderonline.id

Buka produk yang ingin di tracking landing site nya.
Tekan tombol “Install tracker” kemudian “Copy tracking code”
![image50.png](Tech SOP_images/image50.png)
Buka landing page produk tersebut melalui  dan klik “Edit with Elementor”
Tekan tombol plus (+) di pojok kiri atas editor Elementor.
Tambahkan elemen “HTML”.
![image48.png](Tech SOP_images/image48.png)
![image46.png](Tech SOP_images/image46.png)
Paste kode HTML yang sudah di copy dari orderonline lalu publish.

Jumlah views pada landing page akan tercatat secara otomatis di halaman produk Orderonline.id
![image39.png](Tech SOP_images/image39.png)

### Cara Deteksi Platform Free Class

Buat form baru di forminator dengan fields sesuai keperluan.
Tambahkan field baru dengan tipe “hidden field”
![image38.png](Tech SOP_images/image38.png)
Setting sesuai gambar berikut
![image37.png](Tech SOP_images/image37.png)
Cantumkan forminator pada page yang diinginkan
Saat menyebarkan link page pada berbagai platform, bedakan utm_source dari tiap platform. (misal  untuk promosi melalui WhatsApp)
Value yang dimasukkan pada utm_source di URL link akan otomatis tertangkap oleh forminator saat user mengsubmit form.
Data yang terkumpul kemudian dapat di export dan diolah dengan excel/sheets.

## MEMBER AREA: CARA MENAMBAHKAN MODUL DI DASHBOARD MEMBER AREA

![image126.png](Tech SOP_images/image126.png)
Ke tab Appearance dan pilih Theme File Editor

Setelah masuk ke halaman Theme File Editor Scroll ke bawah sampai menemukan code editor seperti di bawah ini
![image125.png](Tech SOP_images/image125.png)
![image124.png](Tech SOP_images/image124.png)
Pada Bagian Theme File masuk ke file tutor > dashboard > dashboard.php

`

Setelah masuk ke menu dashboard.php, scroll ke bawah di bagian code editor sampai ketemu code untuk mengatur course di dashboard
![image130.png](Tech SOP_images/image130.png)

Gambar menunjukkan bagian kode di file dashboard.php, khususnya di dalam folder tutor/dashboard. Bagian kode ini berkaitan dengan **pengaturan dashboard untuk member area** berdasarkan **role pengguna**.
Setiap kotak merah dalam gambar menyoroti array yang berisi daftar ID course yang diatur untuk masing-masing role. ID-ID tersebut merupakan identitas unik dari course yang ada di sistem.
Urutan nya adalah sebagai berikut :
Member pro (*$ordered_courses_pro*)
Member Lifitime (*$ordered_courses_lt*)
Member basic (*$ordered_courses_basic*)
Member Jazz Only (*$ordered_courses_jazz*)
Member Worship Only (*$ordered_courses_worship*)

## MEMBER AREA: CARA MENGAMBIL ID DARI MASING MASING COURSE
![image129.png](Tech SOP_images/image129.png)
Ke Tutor LMS Pro Lalu Pilih Course

Di Halaman Course, pilih salah satu course, lalu dekatkan kursor ke judul course(hover) dan liat ke kiri bawah layar akan ada ID dari Course Tersebut
![image128.png](Tech SOP_images/image128.png)
Bisa dilihat disini yang artinya course belajar baca not balok dari 0 memiliki ID 16852

Setelah itu nanti ID course tersebutlah yang di taro di dashboard.php
![image130.png](Tech SOP_images/image130.png)

## MEMBER AREA: CARA MENAMBAHKAN SECTION DI DASHBOARD MEMBER AREA

Ini adalah Section Member Lifetime musti musik
![image127.png](Tech SOP_images/image127.png)

Ke halaman member area musti musik wp admin, selanjutnya cari snippet dan pilih ke all snippet
![image122.png](Tech SOP_images/image122.png)

Setelah itu cari section add and remove sidebar dan klik edit
![image121.png](Tech SOP_images/image121.png)

Cari kode yang menunjukkan untuk menambahkan section di setiap Role member
![image102.png](Tech SOP_images/image102.png)
kode ini menunjukkan bahwa ini adalah section dari member yang memiliki role lifetime
Setelah itu bisa di copy 1 section untuk menambahkan section baru
![image101.png](Tech SOP_images/image101.png)
Setelah itu ganti nama dan role sesuaikan dengan yang dibutuhkan penjelasan nya sebagai berikut :

### Title = untuk menamakan modul nanti di dashboard member nya
### Url = untuk mengarahkan jika section tersebut di klik
### Icon = untuk menambahkan icon di halaman dashboard member

## LANDING PAGE AREA: CARA JIKA WEBSITE BERANTAKAN SAAT DI PUBLISH

Pastikan terlebih dahulu, halaman mana yang berantakan, jika hanya 1 halaman saja berarti ada yg salah di halaman tersebut dan jika terjadi di semua halaman yang ada di mustimusik.id maka berikut ini merupakan cara untuk membenarkan nya

![image100.png](Tech SOP_images/image100.png)
Pilih Plugin dan masuk ke Installed Plugin

Pilih Semua Plugin
![image99.png](Tech SOP_images/image99.png)

Scroll ke bawah dan pilih **Deactive **lalu klik** Apply**
![image110.png](Tech SOP_images/image110.png)

Setelah sudah ulangi hal yang sama namun memilih **Activate **lalu klik **Apply**
![image108.png](Tech SOP_images/image108.png)
## GANTI PASSWORD MEMBER

Login ke
Klik Member Area → Dashboard
Pilih User (All User) dan search email member
![image104.png](Tech SOP_images/image104.png)
Pilih email yang sesuai, klik Edit User
Scroll sampai ketemu Account Management, klik New Password
![image97.png](Tech SOP_images/image97.png)
Pilih set new password, masukkan password yang diinginkan
Klik use weak password
Scroll sampai ketemu button Update User, klik Update User

## PERPANJANG MEMBERSHIP
Login ke
Klik Member Area → Dashboard
Pilih User (All User) search email member tersebut
Pilih email yang sesuai, klik Edit user
Scroll ke bawah, cek apakah status masih pro
![image95.png](Tech SOP_images/image95.png)
Jika masih pro biarkan, jika belum pro, pillih pro
Scroll sampai ketemu user roles, centang bagian pro jika belum tercentang. Jika sudah tercentang biarkan.
![image86.png](Tech SOP_images/image86.png)
Klik Update User
