print("=== REGISTRASI PESERTA SEMINAR ===")

class NamaInvalidError(Exception):
    pass

while True :
    try :
        nama = input(str('Masukkan Nama: ' ))
        if len(nama) < 3 :
            raise NamaInvalidError()
        
        print('Nama Lengkap: ', nama)
        break

    except NamaInvalidError :
        print('[ERROR] Nama terlalu pendek! Minimal 3 karakter.')

class UmurInvalidError(Exception):
    pass

while True :
    try:
        umur = int(input('Masukkan umur: ' ))
        if umur < 17 or umur > 60 :
            raise UmurInvalidError()
        
        print("umur: ", umur)
        break

    except UmurInvalidError :
            print('[ERROR] Umur tidak memenuhi Syarat (17-60 Tahun)')


class EmailInvalidError(Exception):
    pass

while True :
    try :
        email = str(input("Masukkan Email: " ))
        if "@" not in email :
            raise EmailInvalidError()

        print("Email: ", email)
        break

    except EmailInvalidError :
        print("[ERROR] Email tidak valid! Harus mengandung '@'.")


class NomorInvalidError(Exception):
    pass

while True :
    try :
        nomor = (input("Masukkan No HP: "))
        if len(nomor) < 10 or len(nomor) > 13 or not nomor.isdigit():
            raise NomorInvalidError()

        print("No HP: ", nomor)
        print("Proses input selesai\n\n")
        break

    except NomorInvalidError :
        print("[ERROR] No HP tidak valid! Harus 10-13 digit angka.")


print("=== DATA PESERTA ===")
print('Nama     : ', nama)
print("umur     : ", umur)
print("Email    : ", email)
print("No HP    : ", nomor)
print("Status   : Terdaftar")

