import random

q = random.randint(0,1001)

print("Permainan tebak angka")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak!")

x = 1
y = input("Masukkan tebakan ke-" + str(x) + " --> ")
w = int(y)
while  w != q:
    if w > q :
        print("Itu terlalu besar. Coba lagi!")
    if w < q :
        print("Itu terlalu kecil. Coba Lagi!")
    x += 1
    y = input("Masukkan tebakan ke -" + str(x) + " -->")
    w = int(y)
print("Ya. Anda benar!")
