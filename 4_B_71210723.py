

#data awal
print("=====GEBYAR DISKON=====")
print("=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")
kps = int(input("KIPAS ANGIN DISKON 10%   Rp 25.000,00   : "))
spd = int(input("SEPEDA DISKON 55%        Rp 6.000,00    : "))
hlm = int(input("HELM ROSSI DISKON 77%    Rp 8.000,00    : "))

#jumlah
ttlkps = kps*25000
ttlspd = spd*6000
ttlhlm = hlm*8000
diskps = ((ttlkps)*10)/100
disspd = ((ttlspd)*55)/100
dishlm = ((ttlhlm)*77)/100
total = diskps+disspd+dishlm

#data hasil
print("=====TOTAL=====")
print("TOTAL KIPAS ANGIN   : {} {}".format("Rp", diskps))
print("TOTAL SEPEDA SUPER  : {} {}".format("Rp", disspd))
print("TOTAL HELM ROSSI    : {} {}".format("Rp", dishlm))
print("Jumlah total diskon yang didapat adalah Rp ", total)
