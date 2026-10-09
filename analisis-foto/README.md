# Analisis Foto Menggunakan Python

## 1. Latar Belakang

Gambar yang terlihat oleh manusia sebenarnya disimpan oleh komputer sebagai data angka.

Pada gambar berwarna RGB, setiap pixel mempunyai tiga nilai:

- **R (Red)** = merah
- **G (Green)** = hijau
- **B (Blue)** = biru

Setiap nilai biasanya berada pada rentang 0 sampai 255. Karena itu, warna sebuah pixel dapat ditulis seperti `[255, 0, 0]` untuk merah.

Project ini dibuat untuk membongkar sebuah foto nyata menggunakan Python, melihat informasi file, membaca metadata EXIF bila tersedia, dan melihat pixel sebagai angka dengan NumPy.

> **Catatan:** Foto pada folder `foto/` adalah foto nyata yang dimasukkan ke project, bukan foto yang dibuat secara manual oleh program.

---

## 2. Tujuan Project

Project ini bertujuan untuk memahami:

1. Apa itu gambar digital.
2. Apa itu pixel.
3. Apa itu RGB.
4. Bagaimana gambar dibaca oleh Python.
5. Bagaimana metadata/EXIF dibaca.
6. Bagaimana gambar diubah menjadi NumPy array.
7. Bagaimana cara membaca nilai pixel tertentu.

---

## 3. Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Pillow (PIL)** — membuka gambar, membaca informasi gambar, dan membaca EXIF.
- **NumPy** — mengubah pixel menjadi array angka.

Project sengaja tidak memakai framework atau library tambahan yang tidak diperlukan.

---

## 4. Struktur Project

```text
analisis-foto-python/
│
├── foto/
│   └── foto.jpg
│
├── analisis_foto.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 5. Cara Instalasi

### A. Pastikan Python sudah terpasang

Di terminal / PowerShell jalankan:

```bash
python --version
```

Contoh:

```text
Python 3.10.6
```

Versi Python yang lebih baru juga dapat digunakan selama library yang diperlukan berhasil terpasang.

### B. Masuk ke folder project

```bash
cd analisis-foto-python
```

### C. Buat virtual environment (disarankan)

Windows:

```bash
python -m venv .venv
```

Aktifkan:

```bash
.venv\Scripts\activate
```

### D. Install dependency

```bash
pip install -r requirements.txt
```

---

## 6. Cara Menjalankan Program

Pastikan foto berada di:

```text
foto/foto.jpg
```

Kemudian jalankan:

```bash
python analisis_foto.py
```

Program akan:

1. membuka foto,
2. membaca informasi dasar,
3. membaca EXIF,
4. mengubah foto menjadi NumPy array,
5. menampilkan beberapa nilai pixel.

---

## 7. Penjelasan Proses Analisis

### A. Informasi dasar gambar

Program menampilkan:

- nama file,
- format,
- ukuran file,
- resolusi,
- mode warna,
- jumlah pixel.

Untuk foto yang digunakan pada project ini, hasil pembacaan file adalah:

```text
Nama file       : foto.jpg
Format gambar   : JPEG
Ukuran file     : 638,794 byte
Resolusi        : 1152 x 2048 pixel
Mode warna      : RGB
Jumlah pixel    : 2,359,296 pixel
```

Jumlah pixel dihitung:

```text
1152 x 2048 = 2,359,296 pixel
```

Jadi foto ini mempunyai lebih dari 2,3 juta pixel.

---

## 8. Penjelasan Metadata / EXIF

EXIF (Exchangeable Image File Format) adalah informasi tambahan yang dapat disimpan bersama file foto.

Contoh data yang sering dapat ditemukan:

- Camera Make
- Camera Model
- Date/Time
- ISO
- Exposure Time
- F-Number / Aperture
- Focal Length
- GPS

Namun, **EXIF tidak selalu tersedia**.

Pada foto yang dipakai dalam project ini, Python membaca:

```text
EXIF: Tidak tersedia pada foto ini.
```

Artinya program tidak membuat atau mengarang metadata. Program hanya menampilkan data yang benar-benar ada di file.

Hal ini penting ketika membandingkan foto asli dari kamera/HP dengan foto yang berasal dari media sosial, screenshot, website, atau hasil kompresi, karena metadata dapat hilang saat file diproses ulang.

---

## 9. Pixel dan RGB

Satu pixel pada gambar RGB mempunyai tiga angka.

Contoh:

```text
[255, 0, 0]
```

artinya:

```text
R = 255
G = 0
B = 0
```

Hasilnya adalah warna **merah**.

Contoh lain:

```text
[0, 255, 0]
```

adalah hijau.

Dan:

```text
[0, 0, 255]
```

adalah biru.

Karena setiap channel menggunakan nilai 0 sampai 255, sebuah pixel RGB dapat direpresentasikan dengan tiga angka.

---

## 10. Array NumPy

Ketika gambar RGB diubah menggunakan:

```python
array_image = np.array(image)
```

bentuk array foto menjadi:

```text
(2048, 1152, 3)
```

Artinya:

- `2048` = tinggi gambar,
- `1152` = lebar gambar,
- `3` = jumlah channel warna RGB.

Secara konsep:

```text
array_image[y][x] = [R, G, B]
```

Perhatikan bahwa NumPy menggunakan urutan:

```text
[y, x]
```

bukan:

```text
[x, y]
```

Karena itu, jika kita ingin membaca pixel pada koordinat:

```text
x = 100
y = 100
```

maka Python membaca:

```python
array_image[100, 100]
```

---

## 11. Contoh Nilai Pixel dari Foto Nyata

Beberapa hasil pembacaan pixel dari foto yang digunakan:

```text
Pixel (x=0, y=0) = [118, 118, 110]
Pixel (x=10, y=10) = [132, 131, 126]
Pixel (x=100, y=100) = [129, 130, 125]
Pixel (x=500, y=500) = [162, 159, 152]
Pixel (x=1000, y=500) = [214, 213, 211]
```

Misalnya:

```text
[162, 159, 152]
```

berarti pixel tersebut mempunyai:

```text
Red   = 162
Green = 159
Blue  = 152
```

Karena nilainya berbeda-beda, warnanya bukan merah, hijau, atau biru murni. Kombinasi ketiga angka tersebut menghasilkan warna tertentu yang dilihat mata.

---

## 12. Penjelasan Line-by-Line

Bagian ini sengaja dibuat untuk membantu memahami alur kode.

### 12.1 Import Library

```python
from pathlib import Path
import os

from PIL import Image, ExifTags
import numpy as np
```

**`from pathlib import Path`**

Mengambil class `Path` dari library Python bawaan. `Path` digunakan untuk membuat dan membaca lokasi file dengan lebih rapi.

**`import os`**

Mengimpor modul `os`. Pada project ini digunakan untuk mengambil ukuran file:

```python
os.path.getsize(...)
```

**`from PIL import Image, ExifTags`**

`PIL` adalah bagian dari Pillow.

- `Image` digunakan untuk membuka gambar.
- `ExifTags` digunakan untuk mengenali nama tag EXIF.

**`import numpy as np`**

Mengimpor NumPy dengan nama pendek `np`. NumPy dipakai untuk bekerja dengan array angka.

---

### 12.2 Menentukan Lokasi File

```python
IMAGE_PATH = Path("foto/foto.jpg")
```

`IMAGE_PATH` menunjuk ke foto yang akan dianalisis.

---

### 12.3 Mengecek File

```python
if not IMAGE_PATH.exists():
```

`exists()` mengecek apakah file benar-benar ada.

`not` berarti kondisi dibalik.

Jika file tidak ada, program masuk ke:

```python
raise FileNotFoundError(...)
```

Program berhenti dan memberikan pesan kesalahan agar pengguna tahu bahwa foto belum diletakkan di folder yang benar.

---

### 12.4 Membuka Foto

```python
image = Image.open(IMAGE_PATH)
```

`Image.open()` membaca file gambar.

Variabel `image` sekarang menyimpan objek gambar yang dapat diperiksa dan diproses oleh Pillow.

---

### 12.5 Mengambil Nama File

```python
file_name = IMAGE_PATH.name
```

`.name` mengambil bagian nama file dari sebuah path.

Hasil:

```text
foto.jpg
```

---

### 12.6 Mengambil Format

```python
image_format = image.format
```

Pillow membaca jenis file yang dibuka.

Pada foto project ini:

```text
JPEG
```

---

### 12.7 Mengambil Ukuran File

```python
file_size = os.path.getsize(IMAGE_PATH)
```

Baris ini membaca ukuran file dalam byte.

Hasil pada foto project:

```text
638,794 byte
```

---

### 12.8 Mengambil Resolusi

```python
width, height = image.size
```

`image.size` menghasilkan dua nilai:

```text
(lebar, tinggi)
```

Pada foto project:

```text
1152 x 2048
```

---

### 12.9 Mengambil Mode Warna

```python
color_mode = image.mode
```

Pada foto ini hasilnya:

```text
RGB
```

RGB berarti gambar mempunyai tiga channel:

```text
R, G, B
```

---

### 12.10 Menghitung Jumlah Pixel

```python
total_pixels = width * height
```

Jumlah pixel dihitung dari:

```text
lebar x tinggi
```

Pada foto project:

```text
1152 x 2048 = 2,359,296
```

---

### 12.11 Membaca EXIF

```python
exif = image.getexif()
```

Pillow mencoba membaca data EXIF dari file.

Pada foto project, hasilnya kosong sehingga program menampilkan:

```text
EXIF: Tidak tersedia pada foto ini.
```

Tidak tersedia bukan berarti program error. Artinya file tersebut memang tidak mempunyai EXIF yang dapat dibaca.

---

### 12.12 Mencari Data Kamera

```python
exif_tags = {
    "Camera Make": 271,
    "Camera Model": 272,
    ...
}
```

Dictionary tersebut berisi nama data yang ingin dicari dan ID tag EXIF-nya.

Contoh:

```text
271 = Camera Make
272 = Camera Model
```

---

### 12.13 Mengambil Nilai EXIF

```python
value = exif.get(tag_id)
```

Python meminta nilai dari tag EXIF tertentu.

Jika nilai tidak ditemukan:

```python
if value is None:
```

program menampilkan:

```text
Tidak tersedia
```

Hal ini mencegah program mengarang data.

---

### 12.14 Mengubah Gambar Menjadi Array

```python
array_image = np.array(image)
```

Ini adalah salah satu baris terpenting project.

Gambar yang awalnya berupa objek gambar diubah menjadi kumpulan angka NumPy.

Hasil:

```text
(2048, 1152, 3)
```

Artinya:

```text
2048 baris
1152 kolom
3 channel
```

---

### 12.15 Membaca Informasi Array

```python
array_image.shape
```

`.shape` memberi tahu bentuk atau dimensi array.

```python
array_image.dtype
```

`.dtype` menunjukkan jenis angka yang digunakan.

Pada foto ini:

```text
uint8
```

`uint8` berarti satu nilai channel disimpan sebagai bilangan unsigned 8-bit, dengan rentang 0 sampai 255.

---

### 12.16 Membaca Pixel

```python
pixel = array_image[y, x]
```

Baris tersebut mengambil satu pixel.

Misalnya:

```text
x = 100
y = 100
```

maka:

```python
array_image[100, 100]
```

akan menghasilkan:

```text
[129, 130, 125]
```

Tiga angka itu adalah:

```text
R = 129
G = 130
B = 125
```

---

## 13. Kenapa Gambar Bisa Diubah Menjadi Array?

Karena komputer tidak memahami gambar seperti manusia.

Manusia melihat:

> meja, makanan, piring, kaca, dan warna.

Komputer bekerja dengan data numerik.

Gambar RGB dapat dilihat secara sederhana seperti:

```text
Pixel 1 -> [118, 118, 110]
Pixel 2 -> [132, 131, 126]
Pixel 3 -> [129, 130, 125]
...
```

Jadi gambar dapat dianggap sebagai matriks besar yang berisi angka.

Untuk RGB:

```text
tinggi x lebar x 3
```

Pada project ini:

```text
2048 x 1152 x 3
```

---

## 14. Apa Bedanya Metadata dan Pixel?

**Pixel** adalah isi visual gambar.

Pixel menentukan warna dan tampilan gambar.

**Metadata/EXIF** adalah informasi tambahan mengenai file/foto.

Contoh metadata:

```text
kamera
tanggal pengambilan
ISO
aperture
focal length
GPS
```

Jadi:

```text
Pixel   -> membentuk gambar
EXIF    -> memberi informasi tentang gambar
```

Keduanya berbeda.

---

## 15. Kenapa EXIF Foto Bisa Tidak Ada?

Tidak semua file JPG menyimpan EXIF.

Metadata dapat tidak tersedia karena:

- foto sudah diproses ulang,
- di-screenshot,
- diunduh dari website,
- diekspor dari aplikasi,
- dikompresi oleh platform tertentu.

Karena itu, hasil EXIF dari foto Google, media sosial, screenshot, dan foto asli dari kamera dapat berbeda.

---

## 16. Kesimpulan

Project ini menunjukkan bahwa gambar digital sebenarnya adalah data numerik.

Foto yang digunakan mempunyai:

```text
Resolusi : 1152 x 2048 pixel
Pixel    : 2,359,296
Mode     : RGB
Array    : (2048, 1152, 3)
```

Setiap pixel RGB terdiri dari tiga angka yang mewakili Red, Green, dan Blue.

Dengan Pillow, Python dapat membuka gambar dan membaca metadata jika tersedia.

Dengan NumPy, pixel dapat dilihat sebagai angka.

---

## 17. Pertanyaan yang Mungkin Ditanyakan Dosen

### 1. Apa itu pixel?

Pixel adalah unit terkecil yang menyusun gambar digital. Setiap pixel menyimpan informasi warna.

### 2. Mengapa RGB memiliki 3 angka?

Karena RGB menggunakan tiga channel warna dasar: Red, Green, dan Blue.

### 3. Apa arti `[255, 0, 0]`?

Artinya:

```text
R = 255
G = 0
B = 0
```

Sehingga warnanya merah.

### 4. Apa itu EXIF?

EXIF adalah metadata yang dapat menyimpan informasi tambahan tentang foto, misalnya kamera, waktu pengambilan, ISO, aperture, focal length, dan GPS.

### 5. Apa perbedaan metadata dan pixel?

Pixel membentuk isi visual foto, sedangkan metadata memberikan informasi tambahan tentang file/foto.

### 6. Mengapa gambar bisa diubah menjadi array?

Karena gambar digital pada dasarnya dapat direpresentasikan sebagai angka. NumPy sangat cocok untuk mengolah kumpulan angka tersebut.

### 7. Apa fungsi NumPy?

NumPy digunakan untuk membuat dan mengolah array angka secara efisien. Pada project ini, NumPy dipakai untuk membaca nilai pixel.

### 8. Apa fungsi Pillow?

Pillow digunakan untuk membuka gambar, membaca informasi gambar, dan membaca EXIF.

### 9. Berapa jumlah pixel pada gambar yang digunakan?

```text
1152 x 2048 = 2,359,296 pixel
```

### 10. Mengapa metadata foto dari Google bisa berbeda dengan foto asli?

Karena file yang diunduh dari internet bisa sudah diproses, dikompresi, diekspor ulang, atau metadata EXIF-nya dihapus.

### 11. Mengapa indeks array ditulis `[y, x]`?

Karena NumPy menyimpan data gambar berdasarkan urutan baris kemudian kolom, yaitu tinggi/y lalu lebar/x.

### 12. Apa arti `uint8`?

`uint8` adalah tipe data bilangan bulat tanpa tanda yang menggunakan 8 bit. Untuk data RGB umum, nilainya berada pada 0 sampai 255.

### 13. Apakah setiap JPG pasti memiliki EXIF?

Tidak. EXIF bersifat metadata tambahan dan dapat tidak ada pada sebuah file JPG.

---

## 18. GitHub

### A. Buat repository

Contoh nama repository:

```text
analisis-foto-python
```

Buat repository kosong di GitHub.

### B. Dari folder project

```bash
git init
git add .
git commit -m "Initial project analisis foto Python"
```

### C. Hubungkan ke GitHub

Contoh:

```bash
git branch -M main
git remote add origin https://github.com/USERNAME/analisis-foto-python.git
git push -u origin main
```

Ganti `USERNAME` dengan username GitHub sendiri.

### D. Struktur di GitHub

```text
analisis-foto-python/
├── foto/
│   └── foto.jpg
├── analisis_foto.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 19. Saran Saat Presentasi

Jangan hanya menunjukkan hasil akhir.

Urutan penjelasan yang mudah:

```text
Foto
  ↓
Pillow membuka file
  ↓
Baca informasi dasar
  ↓
Baca EXIF
  ↓
Gambar diubah menjadi NumPy array
  ↓
Ambil beberapa pixel
  ↓
Pixel berupa angka RGB
```

Kalimat kunci yang mudah diingat:

> **"Gambar digital yang terlihat oleh manusia sebenarnya direpresentasikan oleh komputer sebagai data angka. Pada gambar RGB, setiap pixel mempunyai tiga nilai angka yang mewakili Red, Green, dan Blue."**
