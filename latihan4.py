angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

print(" ")


print("*Ubah Input menjadi nol, huruf, dan negatif")
#setelah diubah
angka_list = [0, "a", -3]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')

print(" ")

#program hasil bagi dari 2 angka
print('*Program hasil pembagian 2 angka')
try:
    angkapertama = float(input("masukkan angka pertama: "))
    angkakedua = float(input("masukkan angka kedua: "))
    hasil = angkapertama / angkakedua
except ValueError:
    print("Error: input harus angka")
except ZeroDivisionError:
    print("Error: tidak bisa membagi dengan nol")
except Exception as e:
    print("Terjadi kesalahan:", e)
else:
    print(f"hasil dari pembagian 2 angka tersebut adalah: {hasil}")
finally:
    print("selesai")