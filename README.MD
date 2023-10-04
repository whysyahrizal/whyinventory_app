tugas 2

adaptable :  https://whyinventory-app.adaptable.app

## langkah-langkah

jawab :
- langkah awal pada checklist 1 : membuat sebuah proyek Django baru,yang saya lakukan adalah membuat direktori whyinventory-app, kemudian mengaktifkan virtual environment, lalu menginstall requirement.txt, setelah terinstall seluruh item yang dibutuhkan dalam pengembangan proyek, saya menjalankan perintah "django-admin startproject whyinventory_app". maka django proyek baru telah terbuat dengan nama proyek "whyinventory_app"

- pada checklist 2 : membuat aplikasi dengan nama main pada proyek tersebut, yang saya lakukan adalah menjalankan perintah "python3 manage.py startapp main", maka aplikasi django dengan nama main telah terbuat

- pada checklist 3 : melakukan routing pada proyek agar dapat menjalankan aplikasi main, yang saya lakukan adalah dengan membuat urls.py pada direktori whyinventory-app/main, adapun isi dari urls.py adalah "from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]"

- pada checklist 4 : Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
name sebagai nama item dengan tipe CharField.
amount sebagai jumlah item dengan tipe IntegerField.
description sebagai deskripsi item dengan tipe TextField.
yang saya lakukan adalah melakukan modifikasi pada file models.py pada direktori whyinventory-app/main, lalu membuat atribut wajib seperti yang disebutkan pada soal, yaitu name sebagai nama item dengan tipe CharField dst.

- pada checklist 5 : Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu., yang saya lakukan adalah dengan memodifikasi file views.py pada direktori whyinventory-app/main, pada file tersebut saya buat fungsi seperti show_main(request) yang berfungsi untuk menerima objek 'request' sebagai argumen, yang mewakili request HTTP yang diterima oleh client.

- pada checklist 6 : Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py., yang saya lakukan adalah memodifikasi file urls.py pada direktori main, lalu mengimport modul path dari django.urls, agar dapat terhubung dengan proyek utama, saya sertakan include pada file urls.py di direktori proyek whinventory-app/whyinventory_app, include disertakan pada kode setelah import path.

- pada checklist 7 : masuk ke adaptable.io lalu membuat new app dengan memilih existing repo yang sudah di push ke github saya pribadi, kemudian mengkonfigurasi seperti versi python, manage runserver, checklist http lalu klik deploy

## bagan request & response

jawab :
![Django Request-Response Flow](https://niagaspace.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2022/06/17132515/2-belajar-django-framework-mtv-1024x464.jpg) 

Bagan di atas menjelaskan aliran request dan response dalam aplikasi web Django. Berikut penjelasannya:

1. Client mengirim request ke web server.
2. Web server menerima request dan memprosesnya melalui `urls.py` pada proyek Django.
3. `urls.py` akan memetakan request URL ke fungsi view yang sesuai di `views.py`.
4. Fungsi view dapat mengakses data melalui `models.py`, jika diperlukan.
5. Fungsi view akan merender template HTML yang sesuai dan menggabungkannya dengan data yang diterima dari `models.py`.
6. Fungsi view akan mengembalikan response berupa HTML yang telah dirender.
7. Web server mengirimkan response ke client.

## virtual Environment

Virtual environment merupakan suatu lingkungan yang terisolasi untuk mengelola dependensi proyek Python. Penggunaannya sangat direkomendasikan karena memiliki beberapa kelebihan, seperti:

1. Mengisolasi dependensi proyek, sehingga tidak ada konflik antar proyek yang berbeda.
2. Memudahkan untuk mengatur versi pustaka yang berbeda untuk setiap proyek.
3. Menyederhanakan proses deploy aplikasi.

Kita dapat membuat aplikasi web Django tanpa menggunakan virtual environment, tetapi tidak direkomendasikan karena dapat menyebabkan konflik dependensi dan kesulitan dalam mengelola proyek.

## MVC, MVT, MVVM

MVC, MVT, dan MVVM adalah tiga pendekatan desain arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi. Masing-masing memiliki konsep dan peran yang berbeda dalam memisahkan komponen aplikasi agar lebih terorganisir dan mudah dikelola. Berikut adalah penjelasan singkat tentang masing-masing, serta perbedaan utama di antara ketiganya:

**1. MVC (Model-View-Controller):**

- **Model:** Bertanggung jawab untuk mengelola data dan logika bisnis. Model ini mencakup struktur data dan fungsi-fungsi yang digunakan untuk mengakses dan memanipulasi data tersebut.

- **View:** Bertanggung jawab untuk menampilkan informasi kepada pengguna. Ini adalah antarmuka pengguna yang menampilkan data dari model dan mengirimkan input pengguna ke controller.

- **Controller:** Bertanggung jawab untuk mengontrol aliran aplikasi dan mengatur komunikasi antara model dan view. Controller menerima input dari pengguna dan memutuskan tindakan apa yang harus diambil berdasarkan input tersebut.

**Perbedaan Utama:**
   - MVC adalah arsitektur yang biasanya digunakan pada aplikasi desktop atau web tradisional.
   - Pada MVC, controller berperan sebagai perantara antara model dan view.
   - Biasanya, perubahan pada model akan memicu pembaruan pada view yang sesuai, dan controller berperan dalam mengatur proses ini.

**2. MVT (Model-View-Template):**

- **Model:** Mirip dengan Model pada MVC, ini mengelola data dan logika bisnis.

- **View:** Bertanggung jawab untuk menampilkan informasi kepada pengguna seperti pada MVC.

- **Template:** Berbeda dari MVC, MVT memiliki komponen "Template" yang berfungsi untuk mendefinisikan tampilan HTML dengan tag-template yang disematkan. Ini memisahkan tampilan dari logika aplikasi.

**Perbedaan Utama:**
   - MVT adalah varian dari MVC dan biasanya digunakan dalam kerangka kerja web Django.
   - Perbedaan utama adalah penggunaan "Template" untuk memisahkan tampilan HTML dari logika aplikasi.

**3. MVVM (Model-View-ViewModel):**

- **Model:** Mirip dengan Model pada MVC dan MVT, ini mengelola data dan logika bisnis.

- **View:** Bertanggung jawab untuk menampilkan informasi kepada pengguna seperti pada MVC dan MVT.

- **ViewModel:** Ini adalah komponen khusus dalam MVVM yang bertanggung jawab untuk memisahkan logika presentasi (tampilan) dari model. ViewModel mengonversi data dari model ke format yang dapat ditampilkan oleh view dan juga menangani interaksi pengguna. 

**Perbedaan Utama:**
   - MVVM adalah arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile dan aplikasi web yang kaya interaksi.
   - MVVM memperkenalkan komponen "ViewModel" yang memisahkan tampilan dari model, sehingga memungkinkan pengembang UI untuk lebih mudah mengelola tampilan dan interaksi pengguna.

Dalam ringkasan, ketiga pendekatan ini bertujuan untuk memisahkan konsep data, tampilan, dan logika dalam aplikasi. Pemilihan salah satu tergantung pada jenis aplikasi yang kita kembangkan, kebutuhan pengembangan, dan kerangka kerja yang digunakan. MVC dan MVT umumnya digunakan dalam aplikasi web, sedangkan MVVM lebih umum digunakan dalam aplikasi berbasis antarmuka pengguna.
----------------------------------------------------------------------------------------------
tugas 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
Method POST untuk mengirim sebuah data, sedangkan GET untuk mengambil sebuah data

2.  Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
JSON (JavaScript Object Notation) adalah format ringan untuk pertukaran data. JSON mudah dibaca dan ditulis oleh manusia serta mudah diurai dan dihasilkan oleh mesin. JSON biasanya digunakan dalam aplikasi web untuk mengirim dan menerima data melalui API.

XML (eXtensible Markup Language) adalah bahasa markup yang digunakan untuk menyimpan dan mengangkut data. XML adalah format yang agak lebih kompleks dan lebih berat daripada JSON. XML mendukung penggunaan atribut dan namespace, yang membuatnya lebih fleksibel daripada JSON.

HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat dan merender dokumen web. HTML mendefinisikan struktur dan tampilan halaman web menggunakan elemen dan atribut. Berbeda dengan JSON dan XML, HTML lebih fokus pada penyajian data daripada struktur data.

3.  Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON adalah format data yang ringan dan mudah dibaca oleh manusia. Ini membuatnya ideal untuk pertukaran data antara server dan klien, serta untuk debugging dan pemahaman data dengan cepat.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?
Membuat sebuah views.py yang berisi semua requirement yang diperintahkan. Setelah itu untuk melakukan create-item perlu membuat sebuah ModelForm yang nantinya akan ditampilkan pada html template. ModelForm tersebut berguna untuk menambah sebuah object Item yang nantinya dapat ditampilkan.

5. ss hasil postman

*html

![Alt text](<Screenshot from 2023-09-20 11-47-28.png>)

*json

![Alt text](<Screenshot from 2023-09-20 11-47-58.png>)

*xml

![Alt text](<Screenshot from 2023-09-20 11-48-06.png>)

*json/1

![Alt text](<Screenshot from 2023-09-20 11-50-28.png>)

*xml/1

![Alt text](<Screenshot from 2023-09-20 11-50-50.png>)
----------------------------------------------------------------------------------------------------
tugas 4

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

Django UserCreationForm adalah sebuah fitur yang telah disediakan oleh django dengan tujuan untuk memudahkan developer dalam membuat akun untuk pengguna nantinya. Secara umum, fitur ini digunakan dalam tahap register. Untuk contoh lebih lanjut, bisa dilihat dari kode register yang telah dibuat di views.py

Kelebihan dari fitur bawaan ini adalah kemudahan dalam pembuatan user, fleksibel untuk dilakukan perubahan sesuai dengan kebutuhan developer, dan telah tersedia validasi bawaan, seperti dalam pembuatan username dan password. Namun, kekurangan dari hal ini adalah proses registrasi bawaan yang standar dan adanya keterbatasan ketika melakukan autorisasi yang terintegrasi, contohnya ketika melakukan registrasi dengan akun google dan sebagainya

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi berhubungan dengan proses verifikasi dari data-data yang telah diinput oleh pengguna, sebagai contoh ketika melakukan login. Dengan demikian, autentikasi hanya berfokus kepada pengecekan data input dengan data-data yang telah tersimpan. Sebagai contoh, apabila autentikasi berhasil user dapat melakukan tahap selajutnya.

Autorisasi berhubungan dengan izin kepada pengguna untuk mengakses fitur yang dimiliki dari aplikasi. Dengan demikian apabila user memiliki autorisasi yang sesuai maka user dapat menjlankan fitur tersebut. Sebagai contoh ketika ingin mengakses show main, pengguna harus sudah login terlebih dahulu agara terdeteksi sebagai user.

Kedua hal tersebut sangat penting demi keamanan aplikasi yang dibangun oleh developer. Dengan demikian, developer perlu menerapakan kedua hal tersebut pada aplikasi yang dikembangkannya

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies berguna untuk menyimpan data sesi pengguna. cookies pun bisa menjadi sebuah history dari pengguna tersebut. Selain itu, cookies ini akan tersimpan di device user. Hal ini bisa dicek melalui inspect element pada web browser. 

4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Ya, terdapat risiko yang perlu dipahami saat menggunakan cookies, apalagi ketika cookies tersebut menyimpan data-data sensitif sehingga data-data tersebut bisa diambil oleh orang yang tidak bertanggung jawab dan menyalagunakannya. Selain itu, cookies bisa digunakan oleh pihak aplikasi sebagai data yang potensial untuk digunakan diluar persetujuan pengguna (umumnya persetujuan ini terdapat saat registrasi akun)
 
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Hal pertama yang perlu kita buat adalah service untuk login, register, dan logout. Setelah itu kita membuat html yang berkaitan dengan hal-hal terseut dan juga url yang sebagai akses service-service tersebut. Setelah hal tersebut dilakukan, saya membuat cookies yang diset pada views.py dan juga autorisasi kepada service yang menurut saya penting untuk tidak diketahui selain oleh user terkait. Untuk menyelesaikan soal bonus, saya membuat service dan url yang berkaitan dengan menambah amount dan menghapus produk lalu menyambungkannya dengan html yang ada di main.py
----------------------------------------------------------------------------------------------------
tugas 5

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya?

jawab : Setiap elemen selector dalam CSS memiliki manfaatnya masing-masing dan cocok digunakan dalam situasi-situasi tertentu. Di bawah ini, saya akan menjelaskan manfaat dari beberapa elemen selector utama dan kapan waktu yang tepat untuk menggunakannya:

a. **Universal Selector (`*`)**
   - **Manfaat**: Memilih semua elemen di dalam dokumen HTML.
   - **Kapan Menggunakannya**: Biasanya, kita ingin menghindari penggunaan selector ini secara luas karena dapat memengaruhi seluruh elemen di halaman web. Gunakan dengan sangat hati-hati, atau hanya ketika kita memang benar-benar memerlukannya.

b. **Type Selector (Element Selector)**
   - **Manfaat**: Memilih semua elemen dengan tipe tertentu (misalnya, `p` untuk paragraf, `h1` untuk judul level 1, `div` untuk divisi).
   - **Kapan Menggunakannya**: Cocok digunakan ketika kita ingin mengatur gaya untuk semua elemen dengan tipe yang sama dalam dokumen kita.

c. **Class Selector (`.classname`)**
   - **Manfaat**: Memilih semua elemen yang memiliki atribut `class` tertentu.
   - **Kapan Menggunakannya**: Sangat berguna ketika kita ingin memberikan gaya yang sama untuk beberapa elemen yang memiliki kelas yang sama.

d. **ID Selector (`#idname`)**
   - **Manfaat**: Memilih elemen dengan atribut `id` tertentu.
   - **Kapan Menggunakannya**: Berguna ketika kita ingin memberikan gaya khusus untuk satu elemen tertentu dalam halaman. ID seharusnya unik dalam satu halaman.

e. **Descendant Selector (Space)**
   - **Manfaat**: Memilih elemen yang menjadi turunan dari elemen lain.
   - **Kapan Menggunakannya**: Berguna untuk mengatur gaya elemen-elemen dalam konteks tertentu, seperti mengubah gaya semua paragraf di dalam sebuah div.

f. **Child Selector (`>`)**
   - **Manfaat**: Memilih elemen yang merupakan anak langsung dari elemen lain.
   - **Kapan Menggunakannya**: Berguna ketika kita ingin mengubah gaya elemen yang merupakan anak langsung dari elemen lain, tanpa mempengaruhi elemen-elemen yang lebih dalam pada struktur dokumen.

g. **Adjacent Sibling Selector (`+`)**
   - **Manfaat**: Memilih elemen yang merupakan saudara sejajar (sibling) langsung dari elemen lain.
   - **Kapan Menggunakannya**: Berguna ketika kita ingin mengubah gaya elemen yang berada tepat setelah elemen lain yang sama di dalam dokumen.

h. **General Sibling Selector (`~`)**
   - **Manfaat**: Memilih semua elemen yang merupakan saudara sejajar (sibling) dari elemen lain.
   - **Kapan Menggunakannya**: Berguna ketika kita ingin mengubah gaya semua elemen yang memiliki hubungan sibling dengan elemen lain.


2. Jelaskan HTML5 tag yang kamu ketahui!

Jawab : berikut tag HTML5 yang saya ketahui

a. `<header>`: Bagian atas halaman, berisi judul, logo, atau elemen header lainnya.

b. `<nav>`: Digunakan untuk tautan menu navigasi.

c. `<main>`: Menunjukkan konten utama dalam halaman.

d. `<article>`: Mengelompokkan konten yang mandiri, seperti artikel atau posting blog.

e. `<section>`: Mengelompokkan konten yang terkait atau berhubungan dalam halaman.

f. `<aside>`: Digunakan untuk konten terkait, seperti sidebar.

g. `<figure>` dan `<figcaption>`: Untuk menyertakan media dan keterangan.

h. `<footer>`: Bagian bawah halaman, biasanya berisi informasi kontak atau hak cipta.

i. `<video>` dan `<audio>`: Untuk menampilkan video dan audio di halaman web.

j. `<canvas>`: Untuk membuat grafis dan animasi menggunakan JavaScript.

k. Input Jenis Baru: Jenis input seperti `<input type="email">` dan `<input type="date">` untuk validasi dan input data.

l. `<details>` dan `<summary>`: Membuat daftar detail yang dapat dijatuhkan.

m. `<progress>`: Menunjukkan kemajuan dalam proses.

n. `<meter>`: Menggambarkan pengukuran dalam bentuk grafis.

o. `<datalist>`: Memberikan daftar pilihan untuk input pengguna.

p. `<template>`: Menyembunyikan kode HTML yang dapat digunakan kembali.

3. Jelaskan perbedaan antara margin dan padding.

jawab : Margin adalah jarak antara elemen dan elemen-elemen di sekitarnya, sementara padding adalah jarak antara konten elemen dan batas elemen itu sendiri. Margin mengatur ruang di luar elemen, sedangkan padding mengatur ruang di sekitar konten dalam elemen.

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

jawab : 

Perbedaan antara Tailwind CSS dan Bootstrap:

**Tailwind CSS**:
- **Pendekatan Utility-First**: Menggunakan banyak kelas kecil untuk membangun tampilan sesuai kebutuhan.
- **Customisasi Tinggi**: Dapat disesuaikan secara ekstensif dan cocok untuk proyek dengan desain yang unik.
- **Ukuran Kecil**: Lebih ringan karena hanya menghasilkan kode CSS yang digunakan.

**Bootstrap**:
- **Pendekatan Komponen**: Menyediakan komponen siap pakai seperti navbar dan kartu.
- **Desain Terbukti**: Cocok untuk proyek dengan tampilan yang konsisten dan telah terbukti.
- **Kustomisasi Terbatas**: Kustomisasi lebih rumit daripada Tailwind.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

jawab : pada ceklist 1 saya memulainya dari login.html dan register.html dimana saya mendesain tampilan  login ke centre agar terkesan elegan dan minimalis, ditambah dengan efek hover pada button ketika kursor diarahkan ke bagian login. adapun desain yang saya kerjakan menggunakan css biasa. hasilnya sebagai berikut : 

/home/wahyu-syahrizal/Videos/Screencasts/Screencast from 2023-10-04 20-48-03.webm

![Alt text](<Screenshot from 2023-10-04 20-49-31.png>)
 ![Alt text](<Screenshot from 2023-10-04 20-49-39.png>)

pada ceklis 2, saya mengedit bagian show_item.html menggunakan approach lain seperti card, adapun hasilnya seperti ini. 
![Alt text](<Screenshot from 2023-10-04 20-40-51.png>)

