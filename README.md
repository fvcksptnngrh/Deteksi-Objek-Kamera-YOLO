# Deteksi Objek Kamera Sederhana (YOLO)

Skrip Python (`deteksi_kamera.py`) untuk deteksi objek secara real-time dari kamera (webcam) menggunakan model YOLO.

## Kebutuhan

1.  **Python 3:** Pastikan sudah terinstal.
2.  **pip:** Untuk instalasi library Python.
3.  **Kamera:** Webcam yang terhubung dan berfungsi.
4.  **Library Python:** Instal library yang dibutuhkan. Buka terminal/CMD dan jalankan:
    ```bash
    pip install opencv-python numpy
    # PERHATIKAN: Cek juga bagian 'import' di awal file deteksi_kamera.py.
    # Jika ada library lain (seperti torch, ultralytics, dll.), instal juga.
    ```
5.  **File Model YOLO:** **(PENTING!)** Skrip ini butuh file model YOLO:
    * File bobot (`.weights` atau `.pt`)
    * File konfigurasi (`.cfg`, jika pakai Darknet)
    * File nama kelas (`.names`)
    File-file ini **TIDAK ADA** dalam repositori ini. Anda harus **mendapatkannya sendiri** (dari sumber model YOLO asli) dan **meletakkannya di folder yang sama** dengan `deteksi_kamera.py`.

## Cara Menjalankan

1.  Pastikan semua kebutuhan di atas sudah siap (Python, library terinstal, kamera terhubung, file model ada di folder yang sama).
2.  Buka terminal atau command prompt.
3.  Arahkan terminal ke folder tempat Anda menyimpan `deteksi_kamera.py` dan file-file model YOLO.
4.  Jalankan skrip:
    ```bash
    python deteksi_kamera.py
    ```
5.  Sebuah jendela akan muncul menampilkan gambar dari kamera dengan kotak deteksi objek.
6.  Tekan tombol **'q'** pada keyboard saat jendela kamera aktif untuk menghentikan program.

---
