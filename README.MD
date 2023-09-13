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

Dalam ringkasan, ketiga pendekatan ini bertujuan untuk memisahkan konsep data, tampilan, dan logika dalam aplikasi. Pemilihan salah satu tergantung pada jenis aplikasi yang Anda kembangkan, kebutuhan pengembangan, dan kerangka kerja yang digunakan. MVC dan MVT umumnya digunakan dalam aplikasi web, sedangkan MVVM lebih umum digunakan dalam aplikasi berbasis antarmuka pengguna.