<h1>
IF2150 REKAYASA PERANGKAT LUNAK
<br>
TUGAS 1
<br>
TOPIC BRAINSTORMING
</h1>
<br>

## *Nama Perangkat Lunak*

### Untuk: *Aurelia Jennifer Gunawan*

Dipersiapkan oleh:
| Informasi | Keterangan |
| --- | --- |
| Kelas | *K2* |
| Kelompok | *10*  |

| NIM | Nama |
|---|---|
| *13525083* | *Natanael Chris Fabian Santoso* |
| *13525131* | *Mirza Aryasatya Akmal* |
| *13525149* | *Ferdinand Valentino Darmawan* |
| *13525050* | *Jason Hartanto* |
| *13525065* | *Christopher Hendrik Gunawan* |
---

<br>
<br>

# BAB 1: Analisis Permasalahan

## 1.1 Latar Belakang Masalah
Saat ini, Indonesia masih menghadapi krisis Kekerasan Berbasis Gender terhadap perempuan (KBGtP). Berdasarkan catatan tahunan 2025 yang dirilis oleh Komisi Nasional Anti Kekerasan terhadap Perempuan, sepanjang 2025 tercatat 376.529 kasus KBGtP, yang meningkat 14,07% dibandingkan tahun sebelumnya dan juga menjadi angka tertinggi dalam 10 tahun terakhir. Dari total kasus tersebut, 9,76% di antaranya terjadi di ranah personal, seperti rumah tangga dan hubungan personal. Hal tersebut menunjukkan bahwa ruang yang seharusnya paling aman justru sering kali menjadi ruang paling rentan bagi perempuan.

Bentuk kekerasan yang paling banyak dilaporkan adalah kekerasan seksual sebanyak 37,51%, diikuti kekerasan psikis sebesar 32,48%, fisik sebesar 18,93%, dan ekonomi sebanyak 11,07%. Selain itu, jumlah korban terbanyak berada di kelompok usia 18–24 tahun, dengan jumlah kasus yang dilaporkan adalah 1.453 kasus dari pengaduan langsung ke Komnas Perempuan. Fakta ini menunjukkan bahwa kerentanan tinggi pada perempuan muda adalah dalam fase pendidikan dan awal kedewasaan.

Meskipun Undang-Undang Nomor 12 Tahun 2022 tentang Tindak Pidana Kekerasan Seksual (UU TPKS) telah memberikan landasan hukum yang lebih kuat, implementasi aktualnya masih terhambat. Deputi KemenPPPA, Amurwani Dwi Lestariningsih, menyatakan bahwa aparat penegak hukum masih menggunakan ketentuan KUHP dibandingkan UU TPKS sehingga perlindungan terhadap korban belum optimal. Selain itu, fenomena 'gunung es' masih menjadi tantangan besar di mana banyak korban tidak berani melapor karena stigma, ketakutan, dan ketimpangan relasi kuasa.

Permasalahan yang diangkat disini berkaitan dengan SDGs nomor 5 yaitu Kesetaraan Gender, dan khususnya target 5.2 "Eliminate all forms of violence against all women and girls in the public and private spheres", serta target 5.C "Adopt and strengthen sound policies and enforceable legislation for the promotion of gender equality and the empowerment of all women and girls at all levels". 

Urgensi solusi masalah ini tinggi karena angka kekerasan terus meningkat setiap tahun dan mencapai puncak tertinggi dalam dekade terakhir, ruang digital yang juga semakin menjadi medan baru kekerasan, dan sistem pendampingan korban masih terfragmentasi antara lembaga pemerintah, LSM, dan layanan kesehatan, serta korban kekerasan seringkali tidak mengetahui akses layanan terdekat dan prosedur pelaporan.

## 1.2 Analisis Kondisi Saat Ini
Saat ini, proses pelaporan dan pendampingan korban KBGtP di Indonesia masih reaktif, terpecah, dan tidak terintegrasi digital. 

Sistem yang sudah ada saat ini adalah SIMFONI PPA, Layanan 129, Aplikasi SAPA, dan Layanan P2TP2A. SIMFONI PPA (Sistem Informasi Online Perlindungan Perempuan dan Anak) memiliki fungsi sebagai channel pelaporan, tetapi terbatas pada bata agregat dan belum dapat menyediakan pendampingan *real-time* berbasis lokasi. Layanan 129 (Call Center KemenPPPA) menyediakan hotline telepon, tetapi kapasitasnya terbatas dan tidak memiliki sistem triase untuk mementukan prioritas kasus. Aplikasi SAPA menyediakan channel pengaduan, tetapi belum terintegrasi dengan peta layanan terdekat dan sistem rujukan multilembaga secara otomatis. Layanan P2TP2A (Pusat Pelayanan Terpadu Pemberdayaan Perempuan dan Anak) memiliki sistem yang tersebar secara fisik dan tidak semua daerah memiliki fasilitas yang memadai.

Hasil analisis dari keempat sistem yang sudah ada mengungkap beberapa masalah dari keempat sistem tersebut. Pertama, tidak adanya sistem triase yang otomatis. Petugas layanan tidak memiliki alat bantu untuk mengkategorikan urgensi kasus secara objektif dan konsisten, sehingga menyebabkan kasus darurat sering tertunda. Kedua, data dan layanan tidak memiliki sinkronisasi yang baik. Korban harus mencari sendiri informasi tentang rumah sakit rujukan, konseling psikologis, bantuan hukum, dan pendampingan. Ketiga, kurangnya peta keamanan *real-time*. Tidak ada sistem yang memetakan area berisiko tinggi atau area aman terdekat, sehingga korban sulit membuat keputusan evakuasi yang cepat dan aman. Keempat, stigma dan hambatan akses. Banyak korban terutama di daerah terpencil yang tidak mengetahui cara melapor atau merasa tidak aman melapor secara terbukan karena kurangnya opsi anonimitas yang terjamin. Terakhir, keterbatasan dokumentasi digital. Bukti digital seperti chat, foto, dan rekaman, sering tidak terdokumentasi dengan aman dan terstruktur untuk keperluan proses hukum.

Dengan permasalahan dan celah yang ada dalam sistem yang ada saat ini, perangkat lunak kami akan dirancang untuk mengatasi permasalahan tersebut. Perangkat lunak kami yang disebut SafeShe akan menyediakan satu platform terpadu yang mengintegrasikan pelaporan anonim yang teridentifikasi dengan enkripsi *end-to-end*. SafeShe juga dirancang dengan triase berbasis AI untuk menentukan tingkat urgensi dan jenis layanan yang dibutuhkan, serta mapping geospasial yang menunjukkan area berisiko dan fasilitas layanan terdekat. Safeshe akan memiliki sistem rujukan otomatis ke jaringan mitra, seperti RS, psikolog, dan pengacara. Selain itu, SafeShe juga akan memiliki arsip digital terenkripsi untuk menyimpan bukti dengan *blockchain-based timestamp* untuk keabsahan hukum.

---

# BAB 2: Analisis Solusi

## 2.1 Deskripsi Perangkat Lunak

Perangkat lunak SafeShe adalah aplikasi laporan anonim yang diharapkan menjadi sebuah solusi masalah kekerasan terhadap perempuan. Laporan anonim tersebut diwujudkan dengan menggunakan fitur *one-click SOS* yang akan mengirimkan lokasi ke pihak kepolisian. Fitur ini dapat digunakan dengan lebih mudah, anonim, dan diam-diam agar lebih sulit diketahui pelaku kekerasan. Untuk semakin mempermudah akses fitur ini, tombol tersebut dapat diletakkan dalam handphone sebagai sebuah *widget*. Selain itu, handphone juga akan merekam suara selama keadaan darurat untuk mendapat bukti kekerasan yang membantu dalam membuat kasus terhadap pelaku kekerasan.

Aplikasi juga akan menyediakan peta secara *real-time* untuk layanan terdekat yang berguna bagi korban, seperti rumah sakit atau konseling, serta kontak untuk menelepon layanan tersebut.

Aplikasi ini akan berfokus untuk perangkat handphone seperti perangkat Android dan IoS untuk memudahkan penggunaan aplikasi ini. Menggunakan handphone praktis dan mudah dibandingkan perangkat yang lebih besar seperti laptop yang tidak selalu dibawa. Perbedaan solusi yang ditawarkan melalui aplikasi ini adalah untuk memudahkan penyediaan semua fitur menjadi satu aplikasi yang hanya perlu dipantau oleh pengguna dibandingkan fitur-fitur terpisah yang perlu dipantau secara terpisah dan tersendiri.

## 2.2 Asumsi dan Batasan
Aplikasi ini dibuat dengan asumsi bahwa pihak polisi setuju untuk memantau signal SOS aplikasi SafeShe. Selain itu, juga ada asumsi bahwa terdapat API yang menyediakan data lokasi rumah sakit dan konseling, termasuk kontak telepon tempat tersebut.

Batasannya pada regulasi hukum legal yang diperbolehkan dalam penanganan kasus kekerasan seksual, seperti penanganan pengambilan serta penyimpanan bukti. Selain itu, aplikasi tidak dapat digunakan pada lock screen handphone, jadi pengguna perlu membuka handphonenya sebelum dapat menekan tombol SOS. Batasan lainnya terletak pada kemauan dari pihak polisi untuk merespons dengan baik ketika ada notifikasi SOS, bahkan jika SOS tersebut tidak digunakan dengan semestinya.

---

# BAB 3: Spesifikasi Kebutuhan dan Proses Bisnis

## 3.1 Identifikasi Aktor
Buatlah daftar seluruh aktor (pengguna) yang akan berinteraksi langsung dengan sistem solusi yang kalian kembangkan. Berikan penjelasan singkat mengenai peran dan karakteristik dari masing-masing aktor tersebut.

| Aktor | Deskripsi |
| :--- | :--- |
| Korban | Pengguna ini bertindak sebagai pihak yang memerlukan bantuan karena telah mengalami kekerasan seksual. Karakteristik dari pengguna ini adalah mengutamakan keamanan, kecepatan, dan konfirmasi respons untuk bantuan dari pihak kepolisian. |
| Polisi | Pengguna ini bertindak sebagai pihak yang memantau notifikasi SOS yang dikirimkan oleh korban. Karakteristik dari pengguna ini adalah menginginkan lokasi korban untuk memberi bantuan, mendapatkan bukti untuk membantu pembuatan kasus terhadap pelaku kekerasan seksual, serta kemampuan untuk mengirimkan notifikasi kembali kepada korban bahwa SOS telah diterima dan bantuan sedang dalam perjalanan. |


## 3.2 Kebutuhan Pengguna Awal
Definisikan apa yang ingin dicapai oleh pengguna saat menggunakan sistem ini dalam format *User Story* (Sebagai [Aktor], saya ingin [Aktivitas/Kebutuhan], sehingga [Tujuan/Nilai]). Pastikan kalian berfokus pada "apa yang ingin dilakukan pengguna".

| ID | Aktor | Kebutuhan / Aktivitas | Tujuan / Nilai |
| :--- | :--- | :--- | :--- |
| US-01 | *Korban* |  *Melapor kekerasan secara nyaman, anonim, dan diam-diam* | *Proses pelaporan reliable dan pelaku tidak mengetahui akan laporan* |
| US-02 | *Polisi* | *Menerima laporan dengan data deskripsi kejadian, lokasi, dan waktu kejadian yang akurat* | *Data yang diterima lengkap agar dapat mengklasifikasi urgensi kasus dan bertindak sebagaimana mestinya* |
| ... | ... | ... | ... |

## 3.3 Deskripsi Aktivitas
Buatlah daftar seluruh aktivitas yang terdapat dalam sistem solusi, lengkap dengan ID dan penjelasan. Telusuri hubungan aktivitas tersebut dengan *user story* yang sudah dituliskan sebelumnya. Bisa dibuat dalam bentuk tabel.
| ID | Aktivitas | Penjelasan | ID User Story |
| :--- | :--- | :--- | :--- |
| A01 | *Melakukan Pemesanan* | *Pelanggan memulai proses dengan memesan produk.* | *US-01* |
| A02 | *Memproses Pesanan* | *Sistem memproses dan menyiapkan detail sesuai dengan pesanan.* | *US-02*|
| ... | ... | ... | ... |

## 3.4 Model Proses Bisnis
<br>

<p align="center">
<img alt="SafeShe Swimline Diagram" src="./assets/diagram/SafeShe.drawio.png" width="70%">
</p>
<p align="center">
<i>Gambar 1. Swimline Diagram SafeShe</i>
</p>

<br>

# Referensi
- Diagram UML: https://www.drawio.com/, https://staruml.io/