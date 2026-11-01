teks = input("Masukkan nilai mahasiswa: ")

try:
    nilai = float(teks)
    print(f"Nilai = {nilai}")

except ValueError:
    print("Input harus berupa angka.")

finally:
    print("Proses validasi selesai.")
