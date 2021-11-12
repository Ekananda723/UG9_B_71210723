#data
nama = input("Nama : ")
ttg = input("Tempat tanggal lahir : ")
pnama = nama.split()
pttg = ttg.split()

#kondisi
if len(pnama) == 2:
    namad = pnama[0]
else:
    namad = "{} {}".format(pnama[0], pnama[1])

tanggal = "{} {} {}".format(pttg[1], pttg[2], pttg[3])
#cetak
print("Haloo! {}, {}".format(pnama[-1], namad))
print("Anda lahir di {} pada tanggal {}".format(pttg[0], tanggal))
