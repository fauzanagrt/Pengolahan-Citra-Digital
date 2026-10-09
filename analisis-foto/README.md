# Analisis Foto Digital Menggunakan Python

## Deskripsi Proyek

Proyek ini dibuat untuk menganalisis sebuah citra digital menggunakan bahasa pemrograman Python. Analisis dilakukan untuk memahami informasi yang tersimpan dalam file gambar, metadata, representasi gambar sebagai angka, serta statistik nilai pixel.

Program menggunakan gambar `IMG_2.jpg` sebagai objek analisis. Gambar diproses menggunakan beberapa library Python untuk memperoleh informasi teknis dan melakukan pemeriksaan terhadap data citra.

Proyek ini dibuat sebagai tugas mata kuliah **Pengolahan Citra Digital**.

## Tujuan

Tujuan dari proyek ini adalah:

1. Mengetahui informasi dasar dari sebuah file gambar.
2. Memahami metadata dan EXIF yang terdapat pada gambar.
3. Memahami representasi citra digital dalam bentuk array NumPy.
4. Mengetahui hubungan antara koordinat pixel dan nilai warna RGB.
5. Menghitung statistik warna dan tingkat kecerahan gambar.
6. Menganalisis kontras serta jumlah warna unik.
7. Memverifikasi jumlah pixel berdasarkan dimensi gambar.
8. Memahami perbedaan ukuran file JPEG dan ukuran data pixel mentah.
9. Mengidentifikasi file menggunakan algoritma hash SHA-256.
10. Memahami alur kode Python yang digunakan dalam analisis citra digital.

## Teknologi dan Library

Proyek ini menggunakan teknologi berikut:

* **Python** — bahasa pemrograman untuk menjalankan proses analisis.
* **Pillow (PIL)** — membuka gambar dan membaca informasi gambar serta metadata EXIF.
* **NumPy** — mengubah gambar menjadi array numerik dan menghitung statistik pixel.
* **Library standar Python** — mendukung operasi file, pengolahan data, dan perhitungan hash sesuai implementasi program.

## Struktur Proyek

```text
Analisis-Foto-Python/
├── foto/
│   └── IMG_2.jpg
├── analisis_foto.py
├── Output.txt
├── requirements.txt
└── README.md
```

Keterangan:

* `foto/IMG_2.jpg` merupakan gambar yang dianalisis.
* `analisis_foto.py` merupakan program utama untuk melakukan analisis gambar.
* `Output.txt` menyimpan hasil analisis yang dihasilkan program.
* `requirements.txt` berisi daftar library Python yang dibutuhkan.
* `README.md` berisi dokumentasi proyek.

## Fitur Analisis

Program melakukan beberapa jenis analisis terhadap gambar.

### 1. Informasi Dasar File

Mengidentifikasi nama file, ekstensi, format gambar, ukuran file, dimensi gambar, jumlah pixel, dan mode warna.

### 2. Aspect Ratio

Menghitung rasio antara lebar dan tinggi gambar untuk mengetahui proporsi serta orientasi citra.

### 3. Metadata EXIF

Membaca informasi EXIF yang tersedia, seperti merek dan model perangkat, tanggal pengambilan gambar, orientasi, serta informasi resolusi.

Tidak semua gambar memiliki metadata yang lengkap. Informasi yang tidak tersimpan atau tidak tersedia akan ditampilkan sebagai tidak tersedia.

### 4. Informasi GPS

Memeriksa metadata GPS yang tersimpan dalam gambar, termasuk lintang, bujur, ketinggian, waktu GPS, dan metode pemrosesan GPS jika tersedia.

**Catatan privasi:** metadata GPS dapat mengungkap lokasi pengambilan gambar. Pastikan informasi lokasi tidak dibagikan secara publik jika bersifat pribadi.

### 5. Representasi Gambar sebagai Array NumPy

Gambar RGB diubah menjadi array tiga dimensi yang berisi nilai numerik setiap pixel.

Struktur array:

```python
(height, width, channels)
```

Pada gambar yang dianalisis, bentuk array adalah `(4080, 3072, 3)`.

Artinya:

* Dimensi pertama menunjukkan tinggi atau baris pixel.
* Dimensi kedua menunjukkan lebar atau kolom pixel.
* Dimensi ketiga menunjukkan tiga channel warna, yaitu Red, Green, dan Blue.

### 6. Analisis Nilai Pixel

Program mengambil beberapa sampel pixel untuk mengetahui nilai RGB pada koordinat tertentu.

Setiap pixel RGB direpresentasikan oleh tiga nilai, dengan rentang masing-masing channel dari 0 sampai 255.

Contoh:

```python
pixel = array_image[y, x]
```

NumPy menggunakan urutan baris kemudian kolom, sehingga koordinat gambar `(x, y)` diakses melalui `array_image[y, x]`.

### 7. Statistik Warna RGB

Menghitung nilai minimum, maksimum, rata-rata, median, dan standar deviasi pada setiap channel warna.

Statistik tersebut membantu menjelaskan distribusi intensitas warna dalam gambar.

### 8. Analisis Brightness dan Kontras

Menghitung statistik kecerahan gambar dan standar deviasi brightness untuk membantu memahami variasi intensitas pixel.

Nilai standar deviasi yang lebih besar menunjukkan penyebaran nilai brightness yang lebih lebar, tetapi tidak secara langsung menentukan kualitas visual gambar.

### 9. Jumlah Warna Unik

Menghitung jumlah kombinasi warna RGB berbeda yang ditemukan pada seluruh pixel gambar.

Dua pixel dapat memiliki warna yang sama meskipun berada pada posisi berbeda.

### 10. Sampling Pixel dalam Grid

Mengambil sampel nilai RGB dari sejumlah koordinat yang tersebar di seluruh gambar untuk memberikan gambaran tentang variasi warna pada berbagai bagian citra.

### 11. Verifikasi Jumlah Pixel

Memeriksa apakah jumlah pixel sesuai dengan hasil perkalian tinggi dan lebar gambar.

```text
Jumlah pixel = tinggi × lebar
             = 4080 × 3072
             = 12.533.760 pixel
```

### 12. Estimasi Data Pixel Mentah

Mengestimasi ukuran data pixel berdasarkan jumlah pixel dan jumlah channel warna.

Untuk gambar RGB dengan tipe data `uint8`, setiap channel membutuhkan 1 byte.

```text
Ukuran data mentah = tinggi × lebar × channel
                   = 4080 × 3072 × 3
                   = 37.601.280 byte
```

Ukuran data mentah ini berbeda dari ukuran file JPEG karena JPEG menggunakan kompresi.

### 13. Tipe Data Pixel

Memeriksa tipe data array NumPy. Pada hasil analisis, tipe datanya adalah `uint8`, yaitu bilangan bulat tanpa tanda dengan rentang nilai 0 sampai 255.

### 14. Identitas File dengan SHA-256

Menghitung hash SHA-256 untuk menghasilkan sidik digital file. Hash dapat digunakan untuk membandingkan apakah dua file memiliki isi identik, selama hash dihitung atas keseluruhan byte file dengan metode yang sama.

### 15. Informasi Khusus JPEG

Memeriksa keberadaan tabel kuantisasi JPEG. Tabel ini berkaitan dengan proses kompresi JPEG yang dapat memengaruhi detail dan kualitas citra.

## Hasil Analisis

Berdasarkan output program, diperoleh hasil sebagai berikut.

| Parameter                    | Hasil             |
| ---------------------------- | ----------------- |
| Nama file                    | `IMG_2.jpg`       |
| Format                       | JPEG              |
| Ukuran file                  | 5.345.947 byte    |
| Dimensi                      | 3072 × 4080 pixel |
| Jumlah pixel                 | 12.533.760        |
| Aspect ratio                 | 0,7529            |
| Orientasi                    | Portrait          |
| Mode warna                   | RGB               |
| Bentuk array NumPy           | `(4080, 3072, 3)` |
| Tipe data                    | `uint8`           |
| Ukuran data pixel mentah     | 37.601.280 byte   |
| Jumlah warna unik            | 192.992           |
| Rata-rata Red                | 105,61            |
| Rata-rata Green              | 106,65            |
| Rata-rata Blue               | 96,56             |
| Rata-rata brightness         | 105,19            |
| Standar deviasi brightness   | 70,47             |
| Jumlah tabel kuantisasi JPEG | 2                 |

### Ringkasan Metadata

Metadata yang terbaca menunjukkan bahwa gambar memiliki informasi merek perangkat Xiaomi dan model `220333QAG`. Tanggal dan waktu yang tercatat adalah `2026:08:13 07:45:32`.

Metadata GPS juga tersedia dalam file. Karena informasi tersebut dapat menunjukkan lokasi, detail koordinat tidak dicantumkan dalam ringkasan README ini.

### Interpretasi Hasil

1. Gambar memiliki lebih dari 12,5 juta pixel, sehingga menyediakan banyak data untuk dianalisis.
2. Array NumPy memungkinkan setiap pixel diakses dan diolah sebagai data numerik.
3. Nilai rata-rata channel RGB menunjukkan ringkasan intensitas masing-masing warna, bukan identifikasi warna dominan secara keseluruhan.
4. Standar deviasi brightness sebesar 70,47 menunjukkan variasi intensitas pixel yang cukup lebar.
5. Terdapat 192.992 kombinasi RGB unik di antara seluruh pixel gambar.
6. Ukuran data pixel mentah lebih besar daripada ukuran file JPEG karena data gambar pada file JPEG telah dikompresi.
7. Hash SHA-256 menyediakan cara untuk membandingkan identitas digital file.
8. Sebagian metadata EXIF tersedia, sedangkan informasi kamera lainnya tidak ditemukan pada output.

## Instalasi dan Cara Menjalankan

### Persyaratan

Pastikan Python sudah terpasang di komputer. Periksa instalasi melalui terminal:

```bash
python --version
```

### 1. Clone Repository

Jika proyek berada di GitHub, unduh repository menggunakan:

```bash
git clone URL_REPOSITORY
```

Ganti `URL_REPOSITORY` dengan alamat repository yang digunakan.

### 2. Masuk ke Folder Proyek

```bash
cd Analisis-Foto-Python
```

Sesuaikan nama folder dengan struktur repository yang sebenarnya.

### 3. Instal Library

Jalankan perintah berikut:

```bash
python -m pip install -r requirements.txt
```

Pastikan `requirements.txt` memuat library yang benar-benar digunakan oleh program, misalnya Pillow dan NumPy.

### 4. Jalankan Program

```bash
python analisis_foto.py
```

Program akan membaca gambar yang ditentukan dalam kode, melakukan analisis, dan menampilkan hasil sesuai implementasi program.

Jika program menyimpan hasil ke `Output.txt`, periksa file tersebut setelah proses selesai.

## Cara Membaca Output

Output program dibagi menjadi beberapa bagian agar setiap tahap analisis lebih mudah dipahami:

1. Informasi dasar file.
2. Aspect ratio.
3. Metadata EXIF.
4. Informasi GPS.
5. Representasi gambar sebagai array.
6. Dimensi array.
7. Contoh nilai pixel.
8. Nilai minimum dan maksimum pixel.
9. Statistik channel RGB.
10. Rata-rata nilai warna.
11. Brightness.
12. Kontras.
13. Jumlah warna unik.
14. Sampling pixel.
15. Verifikasi jumlah pixel.
16. Estimasi data mentah.
17. Tipe data pixel.
18. Hash SHA-256.
19. Informasi JPEG.
20. Kesimpulan analisis.

Pembagian ini membantu pengguna memahami bagaimana informasi sebuah foto dapat dibaca, dihitung, dan direpresentasikan menggunakan kode Python.

## Kesimpulan

Proyek ini menunjukkan bahwa citra digital bukan hanya gambar yang dapat dilihat secara visual, tetapi juga sekumpulan data numerik yang dapat dianalisis menggunakan pemrograman.

Dengan Python, Pillow, dan NumPy, informasi dasar gambar, metadata, nilai pixel, statistik warna, brightness, kontras, serta karakteristik file JPEG dapat diperiksa secara sistematis.

Melalui proyek ini, pengguna dapat mempelajari dasar pengolahan citra digital dan memahami hubungan antara gambar visual dengan representasi numeriknya.

## Catatan

Hasil analisis dalam dokumentasi ini berdasarkan output program pada saat dijalankan. Nilai dan metadata dapat berbeda jika file gambar diganti, dimodifikasi, atau diproses menggunakan metode yang berbeda.
