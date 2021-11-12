#data
r = int(input("Masukkan jari-jari alas tabung: "))
t = int(input("Masukkan tinggi tabung: "))
pi = 3.14

#proses
hasil = pi*r**2*t
kesimpulan = "Luas permukaan tabung adalah"

#cetak
print("{} {}".format(kesimpulan, hasil))
