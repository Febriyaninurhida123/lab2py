# input nilai variabel
a=input("masukkan nilai a:")
b=input("masukkan nilai b:")

# cetak nilai variabel
print("Variabel a=",a)
print("Variabel b=",b)

# cetak hasil operasi kedua variabel dengan String format
print("Hasil Penggabungan {1}&{0}=%s".format(a , b) %(a+b))

#koversi nilai variabel
a=int(a)
b=int(b)
print("Hasil Penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil Pembagian {1}/{0}=%d".format(a,b) %(a/b))
