def kabisat():
    inputTahun = int(input('Input tahun : '))
    if inputTahun % 4 == 0:
        return 'Hasil : TAHUN KABISAT'
    else:
        return 'Hasil : BUKAN TAHUN KABISAT'


print(kabisat())