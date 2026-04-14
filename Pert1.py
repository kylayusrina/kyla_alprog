# Program Input Nama dan Umur

nama = input("Masukkan nama anda (nama pendek): ")

if nama.lower() == "kyla":
    print(f"Selamat datang {nama}")
else:
    print("Program selesai")

umur = int(input("Masukkan umur anda: "))

if umur <= 0:
    print("Anda belum lahir")
elif umur < 18:
    print("Anda belum cukup umur")
elif umur <= 60:
    print("Anda cukup umur")
else:
    print("Perbanyak ibadah dan jaga kesehatan")

print("Program selesai")
