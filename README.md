# H1D024085-PraktikumKB-Pertemuan3
Berikut adalah draf `README.md` yang merangkum dan menjelaskan kode logika fuzzy Anda secara singkat, terstruktur, dan mudah dipahami. 

***

# Sistem Kontrol Logika Fuzzy: Prediksi Stok Makanan

## 📖 Deskripsi Singkat
Sistem ini adalah program berbasis Python yang menggunakan **Logika Fuzzy (Fuzzy Logic)** untuk memprediksi atau menentukan jumlah **Stok Makanan** yang harus disiapkan. Pengambilan keputusan didasarkan pada empat variabel input: jumlah barang terjual, tingkat permintaan, harga per item, dan total profit. 

Program ini dibangun menggunakan library `scikit-fuzzy` dan mengimplementasikan metode Mamdani untuk sistem inferensi fuzzy.

## 🛠️ Prasyarat (Requirements)
Sebelum menjalankan kode ini, pastikan Anda telah menginstal library yang dibutuhkan. Anda bisa menginstalnya melalui terminal atau command prompt:

```bash
pip install numpy scikit-fuzzy
```

## 🧩 Penjelasan Variabel

### Variabel Input (Antecedents)
Sistem menerima 4 parameter input dengan rentang nilai dan himpunan fuzzy (membership function) bertipe *triangular* (segitiga):
1. **`barang_terjual`** (0 - 100):
   * Kategori: *Rendah* (0-40), *Sedang* (30-70), *Tinggi* (60-100)
2. **`permintaaan`** (0 - 300):
   * Kategori: *Rendah* (0-100), *Sedang* (50-250), *Tinggi* (200-300)
3. **`harga_per_item`** (0 - 100.000):
   * Kategori: *Murah* (0-40k), *Sedang* (30k-80k), *Mahal* (60k-100k)
4. **`profit`** (0 - 4.000.000):
   * Kategori: *Rendah* (0-1jt), *Sedang* (1jt-2.5jt), *Tinggi* (1.5jt-4jt)

### Variabel Output (Consequent)
Hasil keputusan dari sistem ini adalah 1 variabel:
* **`stok_makanan`** (0 - 1.000):
  * Kategori: *Sedang* (100-900), *Banyak* (600-1000)

## ⚖️ Aturan Fuzzy (Fuzzy Rules)
Sistem mengevaluasi input berdasarkan **6 Aturan (Rules)** yang telah ditetapkan. Misalnya:
* **Aturan 1:** JIKA barang terjual *tinggi* DAN permintaan *tinggi* DAN harga *murah* DAN profit *tinggi*, MAKA stok makanan *banyak*.
* **Aturan 6:** JIKA barang terjual *rendah* DAN permintaan *rendah* DAN harga *sedang* DAN profit *sedang*, MAKA stok makanan *sedang*.

*(Sistem menggunakan logika `AND` untuk menggabungkan kondisi dari setiap variabel input).*

## 🚀 Cara Kerja dan Simulasi
Pada bagian akhir kode, sistem melakukan simulasi (testing) dengan nilai input spesifik:
* `barang_terjual` = 80
* `permintaaan` = 255
* `harga_per_item` = 25.000
* `profit` = 3.500.000

**Proses Output:**
1. Kode memanggil `system.compute()` untuk menghitung inferensi fuzzy berdasarkan input di atas.
2. Program mencetak estimasi nilai angka (crisp value) untuk `stok_makanan` ke layar (console).
3. `stok_makanan.view(sim=system)` akan memunculkan grafik visualisasi area (defuzzifikasi) yang menunjukkan di mana titik output berada.
4. Program akan tertahan (tidak langsung menutup) berkat perintah `input('Tekan Enter untuk keluar...')` sehingga grafik bisa dilihat.
