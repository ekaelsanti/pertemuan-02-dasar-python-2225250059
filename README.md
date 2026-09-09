# Tugas Pertemuan 02 - Dasar Python

## Identitas
* **Nama:** Eka Elsanti
* **NIM:** 2225250059
* **Kelas:** 3A

## Tujuan Repositori
Repositori ini dibuat untuk menyimpan, mendokumentasikan, dan mempublikasikan hasil penyelesaian praktikum Pertemuan 2 mata kuliah Algoritma dan Pemrograman.

## Daftar dan Fungsi Berkas
* `latihan/01_biodata.py` : Menampilkan biodata dan menghitung perkiraan umur.
* `latihan/02_persegi_panjang.py` : Menhitung luas dan keliling persegi panjang.
* `latihan/03_konversi_suhu.py` : Mengonversi suhu Celsius ke Fahrenheit dan Kelvin.
* `latihan/04_nilai_akhir.py` : Menghitung nilai akhir berdasarkan bobot Tugas, UTS, dan UAS.
* `tugas/kalkulator_koordinat.py` : Menghitung jarak Euclidean dan titik tengah dari dua titik koordinat 2D.

## Cara Menjalankan Program
Buka terminal di VS Code, lalu jalankan perintah berikut:
```bash
python tugas/kalkulator_koordinat.py

```

## Hasil Pengujian (Test Case) Kalkulator Koordinat

| Case | Titik A | Titik B | Jarak | Titik Tengah |
| --- | --- | --- | --- | --- |
| 1 | (0.00, 0.00) | (3.00, 4.00) | 5.00 | (1.50, 2.00) |
| 2 | (-2.00, 1.00) | (4.00, 1.00) | 6.00 | (1.00, 1.00) |
| 3 | (2.50, -1.00) | (2.50, 3.00) | 4.00 | (2.50, 1.00) |

## Refleksi & Sumber

* **Refleksi Latihan 01:** Perhitungan umur `2026 - tahun_lahir` bersifat perkiraan karena mengabaikan detail bulan dan tanggal lahir.
* **Konsep Dipahami:** Penggunaan `f-string`, format desimal `:.2f`, konversi tipe data `float()`, serta modul `math`.
* **Sumber Referensi:** Modul Materi Pertemuan 2 & Dokumentasi Resmi Python.

```