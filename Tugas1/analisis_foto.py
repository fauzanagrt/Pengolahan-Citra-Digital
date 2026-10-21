from pathlib import Path
import os
import hashlib

from PIL import Image, ExifTags
import numpy as np


# ============================================================
# 1. IMPORT LIBRARY
# ============================================================
# Path       -> mengatur lokasi file
# os         -> membaca ukuran file
# hashlib    -> membuat hash untuk identifikasi file
# Pillow     -> membaca gambar dan EXIF
# NumPy      -> mengubah gambar menjadi kumpulan angka


# ============================================================
# 2. MENENTUKAN LOKASI FILE
# ============================================================

IMAGE_PATH = Path("foto/IMG_2.jpg")


if not IMAGE_PATH.exists():
    raise FileNotFoundError(
        f"Foto tidak ditemukan: {IMAGE_PATH}"
    )


# ============================================================
# 3. HEADER PROGRAM
# ============================================================

print("=" * 70)
print("ANALISIS FOTO DIGITAL MENGGUNAKAN PYTHON")
print("=" * 70)


# ============================================================
# 4. MEMBUKA GAMBAR
# ============================================================

image = Image.open(IMAGE_PATH)


# ============================================================
# [1] INFORMASI DASAR FILE
# ============================================================

print("\n[1] INFORMASI DASAR FILE")
print("-" * 70)

file_name = IMAGE_PATH.name
file_extension = IMAGE_PATH.suffix
file_size = os.path.getsize(IMAGE_PATH)

width, height = image.size
image_format = image.format
color_mode = image.mode

total_pixels = width * height

print(f"Nama file          : {file_name}")
print(f"Ekstensi           : {file_extension}")
print(f"Format gambar      : {image_format}")
print(f"Ukuran file        : {file_size:,} byte")
print(f"Ukuran file        : {file_size / 1024:.2f} KB")
print(f"Ukuran file        : {file_size / (1024 * 1024):.2f} MB")

print(f"Lebar              : {width:,} pixel")
print(f"Tinggi             : {height:,} pixel")
print(f"Resolusi           : {width:,} x {height:,} pixel")
print(f"Jumlah pixel       : {total_pixels:,} pixel")

print(f"Mode warna         : {color_mode}")


# ============================================================
# [2] ASPEK RASIO
# ============================================================

print("\n[2] ASPECT RATIO")
print("-" * 70)

aspect_ratio = width / height

print(f"Aspect ratio       : {aspect_ratio:.4f}")

if width > height:
    print("Orientasi          : Landscape")
elif height > width:
    print("Orientasi          : Portrait")
else:
    print("Orientasi          : Square")


# ============================================================
# [3] METADATA / EXIF
# ============================================================

print("\n[3] METADATA / EXIF")
print("-" * 70)

exif = image.getexif()

if not exif:
    print("EXIF tidak tersedia.")
else:

    # Membaca seluruh EXIF
    print(f"Jumlah tag EXIF    : {len(exif)}")

    exif_tags = {
        271: "Camera Make",
        272: "Camera Model",
        306: "Date/Time",
        36867: "Date/Time Original",
        34855: "ISO",
        33434: "Exposure Time",
        33437: "F-Number / Aperture",
        37386: "Focal Length",
        282: "X Resolution",
        283: "Y Resolution",
        296: "Resolution Unit",
        305: "Software",
        274: "Orientation",
    }

    for tag_id, tag_name in exif_tags.items():

        value = exif.get(tag_id)

        if value is None:
            print(f"{tag_name:<25}: Tidak tersedia")
            continue

        # Exposure
        if tag_id == 33434:
            try:
                value = f"{float(value):.6f} detik"
            except:
                pass

        # Aperture
        elif tag_id == 33437:
            try:
                value = f"f/{float(value):.2f}"
            except:
                pass

        # Focal Length
        elif tag_id == 37386:
            try:
                value = f"{float(value):.2f} mm"
            except:
                pass

        print(f"{tag_name:<25}: {value}")


# ============================================================
# [4] MEMBACA GPS
# ============================================================

print("\n[4] INFORMASI GPS")
print("-" * 70)

try:
    gps_info = exif.get_ifd(ExifTags.IFD.GPSInfo)
except Exception:
    gps_info = {}

if not gps_info:

    print("GPS                  : Tidak tersedia")

else:

    print("GPS                  : Tersedia")

    for key, value in gps_info.items():

        tag_name = ExifTags.GPSTAGS.get(key, key)

        print(f"{tag_name:<23}: {value}")


# ============================================================
# [5] MENGUBAH GAMBAR MENJADI NUMPY ARRAY
# ============================================================

print("\n[5] REPRESENTASI GAMBAR SEBAGAI ANGKA")
print("-" * 70)

array_image = np.array(image)

print(f"Shape                : {array_image.shape}")
print(f"Jumlah dimensi       : {array_image.ndim}")
print(f"Tipe data            : {array_image.dtype}")
print(f"Ukuran array         : {array_image.nbytes:,} byte")
print(f"Ukuran array         : {array_image.nbytes / (1024 * 1024):.2f} MB")


# ============================================================
# [6] ANALISIS DIMENSI ARRAY
# ============================================================

print("\n[6] ANALISIS DIMENSI ARRAY")
print("-" * 70)

if array_image.ndim == 3:

    array_height, array_width, channels = array_image.shape

    print(f"Tinggi               : {array_height}")
    print(f"Lebar                : {array_width}")
    print(f"Channel              : {channels}")

    print()
    print("Interpretasi:")
    print("- Dimensi pertama  = posisi Y / baris")
    print("- Dimensi kedua    = posisi X / kolom")
    print("- Dimensi ketiga   = channel warna")

    if channels == 3:
        print("- Channel 0 = Red")
        print("- Channel 1 = Green")
        print("- Channel 2 = Blue")

elif array_image.ndim == 2:

    print("Gambar grayscale.")
    print("Setiap pixel hanya memiliki 1 nilai intensitas.")


# ============================================================
# [7] CONTOH NILAI PIXEL
# ============================================================

print("\n[7] CONTOH NILAI PIXEL")
print("-" * 70)

sample_coordinates = [
    (0, 0),
    (10, 10),
    (100, 100),
    (500, 500),
    (1000, 500),
]

for x, y in sample_coordinates:

    if 0 <= x < width and 0 <= y < height:

        pixel = array_image[y, x]

        print(
            f"Pixel (x={x}, y={y}) = {pixel.tolist()}"
        )


print()
print("Catatan:")
print("array_image[y, x] digunakan karena NumPy")
print("menyimpan baris (Y) sebelum kolom (X).")


# ============================================================
# [8] NILAI PIXEL PALING KECIL DAN TERBESAR
# ============================================================

print("\n[8] NILAI PIXEL MINIMUM DAN MAKSIMUM")
print("-" * 70)

print(f"Nilai pixel minimum seluruh gambar : {array_image.min()}")
print(f"Nilai pixel maksimum seluruh gambar: {array_image.max()}")


# ============================================================
# [9] STATISTIK CHANNEL RGB
# ============================================================

print("\n[9] STATISTIK CHANNEL RGB")
print("-" * 70)

if array_image.ndim == 3 and channels >= 3:

    red = array_image[:, :, 0]
    green = array_image[:, :, 1]
    blue = array_image[:, :, 2]

    print("RED")
    print(f"  Minimum    : {red.min()}")
    print(f"  Maksimum   : {red.max()}")
    print(f"  Rata-rata  : {red.mean():.2f}")
    print(f"  Median     : {np.median(red):.2f}")
    print(f"  Std Dev    : {red.std():.2f}")

    print("\nGREEN")
    print(f"  Minimum    : {green.min()}")
    print(f"  Maksimum   : {green.max()}")
    print(f"  Rata-rata  : {green.mean():.2f}")
    print(f"  Median     : {np.median(green):.2f}")
    print(f"  Std Dev    : {green.std():.2f}")

    print("\nBLUE")
    print(f"  Minimum    : {blue.min()}")
    print(f"  Maksimum   : {blue.max()}")
    print(f"  Rata-rata  : {blue.mean():.2f}")
    print(f"  Median     : {np.median(blue):.2f}")
    print(f"  Std Dev    : {blue.std():.2f}")


# ============================================================
# [10] RATA-RATA WARNA KESELURUHAN
# ============================================================

print("\n[10] RATA-RATA NILAI WARNA")
print("-" * 70)

if array_image.ndim == 3:

    mean_rgb = array_image[:, :, :3].mean(axis=(0, 1))

    print(f"Rata-rata Red      : {mean_rgb[0]:.2f}")
    print(f"Rata-rata Green    : {mean_rgb[1]:.2f}")
    print(f"Rata-rata Blue     : {mean_rgb[2]:.2f}")


# ============================================================
# [11] BRIGHTNESS / KECERAHAN
# ============================================================

print("\n[11] ANALISIS BRIGHTNESS")
print("-" * 70)

if array_image.ndim == 3:

    # Rumus luminance sederhana
    brightness = (
        0.299 * red +
        0.587 * green +
        0.114 * blue
    )

    print(f"Brightness minimum : {brightness.min():.2f}")
    print(f"Brightness maksimum: {brightness.max():.2f}")
    print(f"Brightness rata-rata: {brightness.mean():.2f}")
    print(f"Brightness median  : {np.median(brightness):.2f}")

    average_brightness = brightness.mean()

    if average_brightness < 70:
        kategori = "Cenderung gelap"
    elif average_brightness < 140:
        kategori = "Brightness sedang"
    elif average_brightness < 200:
        kategori = "Cenderung terang"
    else:
        kategori = "Sangat terang"

    print(f"Interpretasi       : {kategori}")


# ============================================================
# [12] KONTRAS
# ============================================================

print("\n[12] ANALISIS KONTRAS")
print("-" * 70)

if array_image.ndim == 3:

    contrast = brightness.std()

    print(f"Standard deviation brightness: {contrast:.2f}")

    if contrast < 30:
        print("Interpretasi: kontras relatif rendah.")
    elif contrast < 60:
        print("Interpretasi: kontras sedang.")
    else:
        print("Interpretasi: kontras relatif tinggi.")


# ============================================================
# [13] JUMLAH WARNA UNIK
# ============================================================

print("\n[13] JUMLAH WARNA UNIK")
print("-" * 70)

if array_image.ndim == 3:

    # Mengubah setiap RGB menjadi satu baris
    pixels = array_image[:, :, :3].reshape(-1, 3)

    unique_colors = np.unique(
        pixels,
        axis=0
    )

    print(f"Jumlah seluruh pixel : {len(pixels):,}")
    print(f"Jumlah warna unik    : {len(unique_colors):,}")

    print()
    print("Artinya:")
    print("Tidak semua pixel harus memiliki warna yang berbeda.")
    print("Beberapa pixel dapat memiliki kombinasi RGB yang sama.")


# ============================================================
# [14] SAMPLE PIXEL DALAM GRID
# ============================================================

print("\n[14] SAMPLING PIXEL DALAM GRID")
print("-" * 70)

grid_x = np.linspace(
    0,
    width - 1,
    5,
    dtype=int
)

grid_y = np.linspace(
    0,
    height - 1,
    5,
    dtype=int
)

print("Koordinat dan RGB:")

for y in grid_y:

    for x in grid_x:

        pixel = array_image[y, x]

        print(
            f"({x:5}, {y:5}) = {pixel.tolist()}"
        )

    print()


# ============================================================
# [15] VERIFIKASI JUMLAH PIXEL
# ============================================================

print("\n[15] VERIFIKASI JUMLAH PIXEL")
print("-" * 70)

calculated_pixels = array_image.shape[0] * array_image.shape[1]

print(f"Tinggi array        : {array_image.shape[0]}")
print(f"Lebar array         : {array_image.shape[1]}")

print(
    f"Perhitungan         : "
    f"{array_image.shape[0]} x {array_image.shape[1]}"
)

print(f"Hasil               : {calculated_pixels:,} pixel")

if calculated_pixels == total_pixels:
    print("STATUS              : SESUAI")


# ============================================================
# [16] ESTIMASI DATA RAW PIXEL
# ============================================================

print("\n[16] ESTIMASI DATA RAW PIXEL")
print("-" * 70)

if array_image.ndim == 3:

    bytes_per_pixel = array_image.itemsize * channels

    raw_size = (
        width *
        height *
        channels *
        array_image.itemsize
    )

    print(f"Byte per channel    : {array_image.itemsize}")
    print(f"Jumlah channel      : {channels}")
    print(f"Byte per pixel      : {bytes_per_pixel}")

    print(f"Data pixel mentah   : {raw_size:,} byte")
    print(
        f"Data pixel mentah   : "
        f"{raw_size / (1024 * 1024):.2f} MB"
    )

    print()
    print("Catatan:")
    print("Ukuran file JPEG tidak sama dengan ukuran")
    print("data pixel mentah karena JPEG menggunakan kompresi.")


# ============================================================
# [17] INFORMASI TIPE DATA
# ============================================================

print("\n[17] TIPE DATA PIXEL")
print("-" * 70)

print(f"NumPy dtype         : {array_image.dtype}")
print(f"Ukuran 1 nilai     : {array_image.itemsize} byte")

if array_image.dtype == np.uint8:

    print()
    print("uint8 berarti setiap nilai pixel berada")
    print("pada rentang 0 sampai 255.")

    print()
    print("Contoh:")
    print("0   = intensitas paling rendah")
    print("255 = intensitas paling tinggi")


# ============================================================
# [18] HASH FILE
# ============================================================

print("\n[18] IDENTITAS FILE DENGAN HASH")
print("-" * 70)

sha256 = hashlib.sha256()

with open(IMAGE_PATH, "rb") as file:

    while True:

        data = file.read(4096)

        if not data:
            break

        sha256.update(data)

print(f"SHA-256             : {sha256.hexdigest()}")


# ============================================================
# [19] INFORMASI JPEG
# ============================================================

print("\n[19] INFORMASI KHUSUS JPEG")
print("-" * 70)

if image.format == "JPEG":

    print("File merupakan JPEG.")

    if hasattr(image, "quantization"):

        print(
            f"Jumlah tabel quantization: "
            f"{len(image.quantization)}"
        )

        print()
        print(
            "JPEG menggunakan quantization sebagai "
            "bagian dari proses kompresi."
        )

else:

    print("File bukan JPEG.")


# ============================================================
# [20] KESIMPULAN OTOMATIS
# ============================================================

print("\n[20] KESIMPULAN ANALISIS")
print("-" * 70)

print(f"""
File "{file_name}" memiliki:

1. Resolusi {width:,} x {height:,} pixel.
2. Total {total_pixels:,} pixel.
3. Mode warna {color_mode}.
4. Data gambar berhasil diubah menjadi NumPy array.
5. Setiap pixel RGB direpresentasikan oleh 3 angka.
6. Nilai pixel berada pada rentang {array_image.min()} sampai {array_image.max()}.
7. Metadata EXIF dapat dibaca menggunakan Pillow.
8. Sebagian informasi EXIF dapat tersedia dan sebagian lainnya tidak.
9. Nilai RGB dapat digunakan untuk melakukan analisis statistik.
10. JPEG menggunakan kompresi sehingga ukuran file tidak sama
    dengan ukuran data pixel mentah.
11. SHA-256 dapat digunakan untuk mengidentifikasi file secara digital.
""")

print("=" * 70)
print("ANALISIS SELESAI")
print("=" * 70)