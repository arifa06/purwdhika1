num = (input('Masukkan No. Hp : '))
def program (per):
        if len(num) > 13:
            print('Maksimal 13 angka')
        elif num [0:2] != '08':
            print('Dimulai dari angka 08')
        else:
            print('Nomor HP saya adalah',num)

program(num)