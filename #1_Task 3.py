def program(text):
    while True:
        chr = input('Masukkan Sebuah Kalimat : ')
        if 1 < len(chr) < 200:
            print('*'+chr.upper()+'*')
        elif len(chr) > 200:
            print('Batas Karakter Maksimal 200')
        else:
            print('Masukkan Sebuah Inputan')
program(chr)