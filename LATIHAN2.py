#NOMOR 1

nilai = [75, 80, 65, 90, 85]
#tambahkan nilai
nilai.append(95)
print(nilai)
#tampilkan nilai terkecil
nilai_terkecil = min(nilai)
#hapus nilai terkecil
nilai.remove(nilai_terkecil)
print(nilai)
#urutkan dari terbesar
nilai.sort()
print(nilai)
#tampilkan nilai terendah, tertinggi, jumlah data
nilai_terkecil = min(nilai)
nilai_terbesar = max(nilai)
print(nilai_terkecil)
print(nilai_terbesar)
print (sum(nilai))
#rata rata
print(sum(nilai)/len(nilai))
print(nilai)

#NOMOR 2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print(dosen[1:3])
#PERULANGAN
for x in dosen:
  print(x)
#GANTI NILAI
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
y = list(dosen)
y[3] = 14
dosen = tuple(y)
print(dosen) #mengubah menjadi list dan mengubah data didalam lalu diubah menjadi tuple kembali
print("kelebihan tuple yaitu data tidak mudah berubah tanpa sepengetahuan, mencegah kesalahan membaca data")

#NOMOR 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

#NOMOR 4
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}
