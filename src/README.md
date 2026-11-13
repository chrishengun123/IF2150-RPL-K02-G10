# Safeshe

1. **Deskripsi singkat** aplikasi.
2. **Teknologi yang digunakan** beserta versi (bahasa, framework, basis data).
3. **Prasyarat dan instalasi** (software yang harus ada, perintah instalasi dependensi).
4. **Konfigurasi** (environment variable, setup basis data, migrasi/seed) dan langkah demi langkah menjalankannya.
5. **Cara menjalankan aplikasi** (dan cara menjalankan test, jika ada).
6. **Akun/data uji** untuk mencoba tiap peran pengguna (jika ada login).
7. **Daftar modul/fitur yang diimplementasi** beserta pembagian anggota.
8. **Daftar tabel/koleksi basis data** beserta atributnya (atau tautan ke skema/ERD).

**Safeshe** merupakan aplikasi berbasis web bagi perempuan untuk melaporkan tindakan kekerasan seksual (KS) secara **anonim** dan **rahasia**.
Pelaporan KS dapat langsung dilakukan dengan menekan tombol **One-Click SOS**. Tombol tersebut langsung **mengirimkan lokasi korban ke polisi** dan **mengaktifkan mikrofon** untuk merekam suara sekitar.
Safeshe juga memiliki **peta layanan terdekat**, seperti rumah sakit, konseling, *shelter*, dan polisi. Selain itu, Safesha juga memiliki laporan kekerasan yang **terenkripsi**. 
Klien Safeshe bersifat *offline-first*, yang berarti permintaan disimpan di *queue* perangkat dan dikirim saat gawai memiliki koneksi lagi.

*Catatan: data pada repo ini tidak ada yang nyata, alias **fiktif**.*

## Teknologi yang Digunakan
| Komponen | Teknologi |
| --- | --- |
| Bahasa server | Python 3.12 (diuji pada 3.12; 3.10+ seharusnya cukup) |
| Framework | FastAPI 0.115.6, Uvicorn 0.34.0 |
| Basis data | SQLite (bawaan Python) |
| Enkripsi | cryptography 44.0.0 (Fernet) |
| Klien | HTML + JavaScript (tanpa build), Leaflet 1.9.4 via CDN untuk peta |
| Uji | pytest 8.3.4, httpx 0.28.1 |

## Prasyarat dan Instalasi
Butuh Python 3.10+ dan *browser* modern seperti Google Chrome. Jalankan kode berikut di terminal, dan pastikan sudah ada di *root directory*. 
```bash
cd src
python -m venv venv
source venv/bin/activate    # jika di Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Konfigurasi
Semua variabel bersifat **opsional** (contoh di `.env.example`). Berikut adalah yang terjadi tanpa konfigurasi apa pun:
- basis data dan folder rekaman dibuat otomatis di `src/data`,
- kunci enkripsi dibuat otomatis di `src/data/.key`,
- skema tabel dan data fiktif dibuat otomatis saat server pertama berjalan. **Tidak ada langkah migrasi/seed manual**.

## Cara Menjalankan Aplikasi dan Test
### Menjalankan Aplikasi
Pastikan *command* untuk prasyarat dan instalasi sudah dijalankan.
```bash
cd src
uvicorn backend.main:app --reload --port 8000
```
- Aplikasi korban ada di http://localhost:8000/ berukuran ponsel
- *Dashboard* polisi ada di http://localhost:8000/police.html
- Dokumentasi API ada di http://localhost:8000/docs

Geolokasi dan mikrofon di *browser* hanya berfungsi di `localhost` atau HTTPS. Layar dapat tampil *offline*, tetapi peta membutuhkan internet untuk memuat Leaflet dan tile OpenStreetMap.

### Menjalankan Test
```bash
cd src
python -m pytest tests -v
python test/profile_nearby.py 50000
```
`profile_nearby.py` digunakan untuk profiling layanan terdekat.

## Akun/data uji
Korban tidak perlu login (anonim). *Dashboard* polisi memakai API key demo: **`polisi-demo`**

Skenario uji coba:
1. Buka *dashboard* polisi di satu tab dan masukkan *key* `polisi-demo`.
2. Di aplikasi korban, **tahan tombol SOS sekitar 1,5 - 2 detik**. Mikrofon dapat dimatikan dengan menekan tombol *Hentikan rekaman suara*. Sinyal akan muncul di *dashboard* polisi.
3. Di dashboard polisi **pilih sinyal, tulis balasan, lalu kirim balasan**. Di aplikasi korban, layar *Respons Petugas* menampilkan balasan, dan tab *Status* menampilkannya dalam tampilan yang disamarkan sebagai catatan personal.
4. Untuk uji offline, matikan jaringan, kirim SOS atau laporan, lalu nyalakan jaringan lagi.
5. Di dashboard, buka menu **Laporan**, pilih laporan, baca isinya, ubah status penanganan, dan tulis catatan.
6. Untuk pelapor, di layar konfirmasi tekan **Cek status laporan**, atau buka tab *Lapor* lalu **Cek status laporan** dan masukkan kode laporan. Ubah status dan isi *Pesan untuk pelapor* di *dashboard* lalu cek ulang.
7. Tab *Status* dibuat terlihat seperti aplikasi catatan biasa untuk menyamarkan aplikasi SafeShe. Dalam tab ini, pengguna dapat membuat, mengubah, dan menghapus catatan, mencoba filter, dan pencarian. Membuka tab ini pertama kali akan menunjukkan petunjuk singkat yang dapat dilihat lagi dari menu *Panduan*. Untuk kembali, **ketuk tombol "+" dua kali** atau **ketuk judul *Catatan* dua kali**.
8. Di tab *Layanan*, pengguna dapat pilih layanan dan tekan telepon.

## Modul/Fitur dan Pembagian Anggota
| Modul | Use case | Berkas utama | Penanggung jawab |
| --- | --- | --- | --- |
| Frontend aplikasi, dasbor polisi | UC01, UC06, UC07 | `frontend/` | *Mirza Aryasatya Akmal* |
| Backend aplikasi, peta dan layanan, laporan kekerasan | `backend/main.py`, `backend/domain` |  UC02, UC03, UC04 | *Christopher Hendrik Gunawan* |
| Database dan enkripsi | - | `backend/config.py`, `backend/crypto.py`, `backend/db.py`, `backend/seed.py`, `backend/__init__.py`, `env.example`, `requirements.txt` | *Natanael Chris Fabian Santoso* |
| Testing | - | `tests/` | *Ferdinand Valentino Darmawan, Jason Hartanto* |

## Struktur
```
src/
  backend/ main.py (rute API), db.py, config.py, crypto.py, seed.py
           domain/ sos.py, laporan.py, layanan.py     # kelas perancangan C01-C12
  frontend/ index.html, app.js, style.css, icons.svg, police.html
  tests/ test_api.py, profile_nearby.py
```

## Basis Data (SQLite, `src/data/safeshe.db`)
| Tabel | Atribut |
| --- | --- |
| `sos` | id (PK), client_id (unik), nama, lat, lon, status (`dikirim`/`diterima`/`dalam_perjalanan`), reply, polisi_id (FK), created_at |
| `rekaman` | id (PK), sos_id (FK), path, created_at |
| `laporan` | id (PK), token (unik), client_id (unik), mode, payload_enc (terenkripsi), created_at, status, catatan, pesan_pelapor, updated_at |
| `layanan` | id (PK), nama, jenis, lat, lon, kontak, alamat, fasilitas; indeks `idx_layanan_lat_lon` |
| `polisi` | id (PK), nama, lat, lon, tersedia |

## Endpoint
| Metode | Path | Fungsi |
| --- | --- | --- |
| POST | `/api/sos` | kirim SOS (202, idempoten per `client_id`) |
| POST | `/api/sos/{id}/recording` | unggah segmen rekaman |
| GET | `/api/sos/{id}/status` | konfirmasi (teks disamarkan) |
| POST | `/api/laporan` | buat laporan (422 + daftar `kolom` jika tidak lengkap) |
| GET | `/api/laporan/{kode}/status` | status dan pesan petugas untuk pelapor (tanpa isi laporan) |
| GET | `/api/layanan/nearby` | layanan terdekat (`lat`, `lon`, `radius_km`, `jenis`) |
| GET | `/api/layanan/{id}` | detail dan kontak |
| GET/POST | `/api/polisi/...` | daftar SOS, reply, rekaman, laporan, dan tindak lanjut laporan (header `X-API-Key`) |
