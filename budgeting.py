modalAwal=50000000


def pembelian(up):
    print("toko ini membeli dengan harga",up)

def penjualan(up):
    print("barang ini di jual dengan harga",up)

def keuntungan_peritem(penjualan,pembelian):
    total=penjualan-pembelian
    return total


def saldoAkhir(keuntungan):
    global modalAwal
    total=modalAwal+keuntungan
    return total


def labarugi(keuntungan):
    global modalAwal
    if modalAwal<keuntungan:
        laba=keuntungan-modalAwal
        return laba
    elif modalAwal>keuntungan:
        rugi=modalAwal-keuntungan
        return rugi

    elif modalAwal==keuntungan:
        impas=modalAwal==keuntungan
        return impas
    else:
        print("terjadi kesalahan penghitungan")






pembelian(10000)
penjualan(15000)
untung=keuntungan_peritem(15000,10000)
print(untung)
saldoAkhir(70000000)
totalsaldo=saldoAkhir(70000000)
print(totalsaldo)

labaataurugi=labarugi(80000000)
print(labaataurugi)