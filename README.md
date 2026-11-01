# Pertemuan 12 - File I/O dan Error Handling

## Identitas Mahasiswa
- Nama: [Nama Kamu]
- NIM: [NIM Kamu]
- Kelas: [Kelas Kamu]
- Mata Kuliah: Algoritma dan Pemrograman
- Program Studi: Pendidikan Matematika FKIP Untirta

## Deskripsi Proyek
Proyek ini dibuat untuk memenuhi tugas praktikum
Algoritma dan Pemrograman Pertemuan 12.

Program mempelajari cara membaca dan menulis file menggunakan
Python, memproses data teks, menangani kesalahan (error handling),
serta menghitung rekap nilai mahasiswa dari file.

## Tujuan
1. Memahami penggunaan file input-output pada Python.
2. Memahami mode file r, w, dan a.
3. Membaca dan menulis data menggunakan file teks.
4. Memproses data dengan strip(), split(), dan float().
5. Menangani FileNotFoundError dan ValueError.
6. Menghitung statistik nilai mahasiswa.
7. Menyimpan hasil rekap ke dalam file teks.

## Struktur Folder
```text
pertemuan-12-file-io-NIM/
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
├── tugas/
│   └── rekap_nilai_file.py
├── README.md
└── .gitignore
```

## Teknologi yang Digunakan
- Python 3
- Visual Studio Code
- Git
- GitHub

## Materi yang Dipelajari
- Membaca file dengan mode `r`.
- Menulis file dengan mode `w`.
- Menambahkan data dengan mode `a`.
- Menggunakan `with open()` dan `encoding="utf-8"`.
- Mengolah baris dengan `strip()` dan `split()`.
- Mengubah teks menjadi angka menggunakan `float()`.
- Menangani `FileNotFoundError` dan `ValueError`.
- Menggunakan fungsi untuk membaca dan menulis data.

## Format File Input
File `data/nilai.txt` menggunakan format NIM,nilai.

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Data dengan nilai `abc` digunakan untuk menguji
penanganan data yang tidak valid.

## Cara Menjalankan Program

1. Buka folder proyek di Visual Studio Code.
2. Pastikan Python 3 sudah terpasang.
3. Pilih menu Terminal > New Terminal.
4. Jalankan latihan sesuai kebutuhan.

Contoh menjalankan latihan:

```bash
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
```

Menjalankan program tugas utama:

```bash
python tugas/rekap_nilai_file.py
```

## Output Program
Program utama menghasilkan file `data/hasil_rekap.txt`
yang berisi:
- Jumlah data valid.
- Rata-rata nilai.
- Nilai minimum.
- Nilai maksimum.
- Jumlah mahasiswa lulus.
- Jumlah mahasiswa belum lulus.
- Detail nilai setiap mahasiswa yang valid.

Mahasiswa dinyatakan lulus jika memperoleh nilai
minimal 60.

## Penanganan Error
Program menangani beberapa kondisi berikut:

1. FileNotFoundError
   Terjadi jika file input tidak ditemukan.
   Program menampilkan pesan kesalahan yang jelas.

2. ValueError
   Terjadi jika nilai tidak dapat dikonversi menjadi angka
   atau format baris tidak sesuai.
   Baris yang tidak valid dilewati dan data lainnya
   tetap diproses.

3. Baris kosong
   Baris kosong dilewati agar tidak mengganggu
   proses pengolahan data.

## Pengujian Program

| No. | Test Case | Hasil yang Diharapkan |
|---|---|---|
| 1 | Semua data valid | Data diproses dan rekap dibuat |
| 2 | File tidak ditemukan | Pesan kesalahan ditampilkan |
| 3 | Nilai berisi teks, seperti abc | Baris tidak valid dilewati |
| 4 | Terdapat baris kosong | Baris kosong dilewati |
| 5 | Nilai sama dengan 60 | Dihitung sebagai lulus |

## Git dan GitHub

Perintah untuk menyimpan perubahan proyek:

```bash
git init
git add .
git commit -m "feat: menambahkan latihan file io"
git add latihan data
git commit -m "feat: menyelesaikan latihan baca tulis file"
git add tugas/rekap_nilai_file.py
git commit -m "feat: menyelesaikan tugas rekap nilai"
git add README.md
git commit -m "docs: menambahkan dokumentasi proyek"
```

Hubungkan repositori lokal dengan GitHub dan unggah
perubahan menggunakan:

```bash
git branch -M main
git remote add origin https://github.com/USERNAME/pertemuan-12-file-io-NIM.git
git push -u origin main
```

Ganti `USERNAME` dan `NIM` sesuai akun GitHub
dan identitas proyek masing-masing.

## Refleksi
Melalui proyek ini, saya mempelajari cara menyimpan,
membaca, dan mengolah data menggunakan file pada Python.
Saya juga memahami pentingnya penanganan error agar
program tetap dapat memproses data yang valid ketika
terdapat file yang tidak ditemukan atau data yang salah.

## Kesimpulan
File input-output memungkinkan data disimpan agar tetap
tersedia setelah program selesai dijalankan. Penggunaan
try-except membantu menangani kesalahan yang diperkirakan,
sedangkan fungsi membuat kode lebih terstruktur dan mudah
dipelihara.