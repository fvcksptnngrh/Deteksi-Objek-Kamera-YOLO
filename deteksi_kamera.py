import cv2
from ultralytics import YOLO

# --------------------------------------------------
# Pengaturan Model dan Kamera
# --------------------------------------------------
# Muat model YOLOv8 (misalnya 'yolov8n.pt' untuk kecepatan, atau 'yolov8s.pt'/'yolov8m.pt' untuk akurasi lebih)
# Model akan diunduh otomatis jika belum ada.
try:
    model = YOLO("yolov8n.pt")
    print("Model YOLOv8 berhasil dimuat.")
except Exception as e:
    print(f"Error memuat model YOLO: {e}")
    exit()

# Tentukan sumber kamera. 0 biasanya untuk webcam internal/default.
# Jika Anda punya lebih dari satu kamera, coba ganti dengan 1, 2, dst.
camera_index = 0
cap = cv2.VideoCapture(camera_index)

# Periksa apakah kamera berhasil dibuka
if not cap.isOpened():
    print(f"Error: Tidak dapat membuka kamera dengan index {camera_index}.")
    print("Pastikan kamera terhubung dan tidak digunakan oleh aplikasi lain.")
    exit()
else:
    print(f"Kamera dengan index {camera_index} berhasil dibuka.")
    # Coba atur resolusi (opsional, jika diperlukan)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Dapatkan nama kelas yang diketahui model (COCO dataset names)
# Ini berguna jika Anda ingin memfilter kelas tertentu nanti
class_names = model.names
print("Kelas yang dapat dideteksi:", class_names)


# --------------------------------------------------
# Loop Pemrosesan Frame Kamera
# --------------------------------------------------
print("\nMulai deteksi real-time... Tekan 'q' untuk keluar.")

while True:
    # 1. Baca satu frame dari kamera
    success, frame = cap.read()

    # Jika gagal membaca frame (misalnya, kamera terputus), hentikan loop
    if not success:
        print("Error: Gagal membaca frame dari kamera.")
        break

    # 2. Lakukan Deteksi Objek dengan YOLOv8
    #    'frame' adalah gambar inputnya.
    #    'conf=0.5' berarti hanya tampilkan deteksi dengan confidence score >= 50% (bisa diubah)
    #    'classes=0' jika hanya ingin deteksi 'person'. Hapus parameter ini untuk deteksi semua objek.
    results = model.predict(frame, conf=0.5) # Deteksi semua objek dengan confidence > 0.5

    # Anda bisa filter kelas secara spesifik di sini jika mau, contoh hanya orang (kelas 0 di COCO):
    # results = model.predict(frame, conf=0.5, classes=0) # Hanya deteksi 'person'

    # 3. Visualisasikan Hasil Deteksi pada Frame
    #    Metode .plot() dari ultralytics sangat praktis,
    #    ia akan menggambar kotak pembatas (bounding box) dan label pada frame.
    annotated_frame = results[0].plot()

    # 4. Tampilkan Frame yang Sudah Dianotasi
    cv2.imshow("Deteksi Real-time Orang & Benda (YOLOv8)", annotated_frame)

    # 5. Cek Tombol Keluar
    #    Tunggu 1 milidetik untuk input keyboard.
    #    Jika tombol 'q' ditekan, hentikan loop.
    #    cv2.waitKey(1) juga penting agar jendela OpenCV bisa menampilkan gambar.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Tombol 'q' ditekan. Menghentikan program...")
        break

# --------------------------------------------------
# Membersihkan Sumber Daya
# --------------------------------------------------
# Lepaskan objek kamera
cap.release()
# Tutup semua jendela OpenCV yang terbuka
cv2.destroyAllWindows()
print("Sumber daya kamera dan jendela tampilan sudah dilepaskan.")