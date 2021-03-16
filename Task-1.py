#Soal 1
for i in range(2):
    num = int(input('Masukkan Angka : '))
    if num == 0:
        print('0 bukan bilangan positif dan negatif')
    elif num < 0:
        print('masukkan bilangan bulat')
    elif num % 2 == 0:
        print(num,'bilangan genap')
    else:
        print(num,'bilangan ganjil') 
print('')

#Soal 2
print('menu menghitung segiiga dan persegi')
print('masukkan 1 untuk luas segitiga')
print('masukkan 2 untuk luas persegi')
for i in range(2):
    num1 = int(input('Masukkan Angka :'))
    if num1 == 1:
        t = int(input('Masukkan Tinggi Segitiga :'))
        a = int(input('Masukkan Alas Segitiga :'))
        print('luas segitiga adalah ',(t*a/2))
    elif num1 == 2:
        s = int(input('Masukkan Sisi Persegi :'))
        print('luas persegi adalah ',s**2)
    else:
        print('masukkan inputan yang benar')
print('')

#Soal 3
for i in range(2):
    import math
    day = int(input('Masukkan jumlah hari : '))
    t = math.floor (day/360)
    b = math.floor ((day%360)/30)
    m = math.floor (((day%360)%30)/7)
    h = math.floor (((day%360)%30)%7)
    if day > 0:
        print(day,'hari =',t,'tahun',b,'bulan',m,'minggu',h,'hari')
    else:
        print('masukkan angka yang benar')
print('')

#Soal4
for i in range(2):
    kal = input('Masukkan sebuah kalimat : ')
    if len(kal) > 50:
        print('Kalimat terlalu panjang')
    else:
        print('kalimat ideal')
print('')

#Soal5
for i in range(2):
    suhuF = int(input('Masukkan suhu (F) : '))
    suhuC = (suhuF-32) * 5/9
    if suhuC > 37.2:
        print('suhu badan anda : ',suhuC,'derajat celcius\nanda hipertermia')
    elif  36.5 < suhuC < 37.2:
        print('suhu badan anda : ',suhuC,'derajat celcius\nanda normal')
    else:
        print('suhu badan anda : ',suhuC,'derajat celcius\nanda hipotermia')