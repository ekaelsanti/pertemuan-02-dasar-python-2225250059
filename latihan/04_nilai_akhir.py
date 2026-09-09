nama = input("Nama mahasiswa: ")
nilai_tugas = float(input("Nilai Tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.30) + (nilai_uas * 0.50)

print(f"\nNilai Akhir {nama}: {nilai_akhir:.2f}")