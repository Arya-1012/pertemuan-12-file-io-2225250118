
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                try:
                    # Memisahkan NIM dan nilai
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)

                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    # Mengambil seluruh nilai yang valid
    nilai = [item[1] for item in data]

    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    nilai_minimum = min(nilai)
    nilai_maksimum = max(nilai)

    # Nilai minimal 60 dinyatakan lulus
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    # Menyimpan hasil rekap ke file
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("===== REKAP NILAI MAHASISWA =====\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {nilai_minimum:.2f}\n")
        file.write(f"Nilai maksimum: {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah mahasiswa lulus: {jumlah_lulus}\n")
        file.write(f"Jumlah mahasiswa belum lulus: {jumlah_data - jumlah_lulus}\n")

        file.write("\nDetail nilai valid:\n")
        for nim, angka in data:
            status = "Lulus" if angka >= 60 else "Belum lulus"
            file.write(f"{nim}, {angka:.2f}, {status}\n")

    print(f"Rekap berhasil disimpan ke {nama_file}")


# Program utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data:
    tulis_rekap(output_file, data)
