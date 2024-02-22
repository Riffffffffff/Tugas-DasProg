# Harga belanja
harga_belanja = int(input("Masukkan total harga belanja: "))

# Inisialisasi variabel diskon
diskon = 0

# Cek apakah harga belanja lebih dari 60 ribu
if harga_belanja > 60000:
    diskon = 10000  # Diskon 10 ribu

# Jumlah yang harus dibayar setelah diskon
total_harga = harga_belanja - diskon

# Menampilkan hasil
print("Jumlah yang harus dibayar: ", total_harga, "rupiah")
