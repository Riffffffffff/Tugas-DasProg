def hitung_gaji(gaji_pokok, uang_transport_perhari, uang_makan_perhari, hari_kerja, hari_lembur, jam_lembur_perhari):
    # Menghitung total transport dan total makan
    total_transport = uang_transport_perhari * hari_kerja
    total_makan = uang_makan_perhari * hari_kerja

    # Menghitung upah lembur per jam
    upah_lembur_pertama = 100000  # Untuk 2 jam pertama
    upah_lembur_selanjutnya = 150000  # Untuk jam selanjutnya

    # Menghitung total jam lembur dan upah lembur
    total_jam_lembur = hari_lembur * jam_lembur_perhari
    upah_lembur = 0
    if total_jam_lembur <= 2 * hari_lembur:  # Jika total jam lembur kurang dari atau sama dengan 2 jam per hari lembur
        upah_lembur = total_jam_lembur * upah_lembur_pertama
    else:
        upah_lembur = 2 * hari_lembur * upah_lembur_pertama + (total_jam_lembur - 2 * hari_lembur) * upah_lembur_selanjutnya

    # Menghitung total gaji
    total_gaji = gaji_pokok + total_transport + total_makan + upah_lembur

    return total_gaji

# Masukkan data yang diberikan
gaji_pokok = 2000000
uang_transport_perhari = 100000
uang_makan_perhari = 50000
hari_kerja = 25
hari_lembur = 10
jam_lembur_perhari = 4

# Hitung total gaji
total_gaji = hitung_gaji(gaji_pokok, uang_transport_perhari, uang_makan_perhari, hari_kerja, hari_lembur, jam_lembur_perhari)
print("Total gaji: Rp.", total_gaji)
