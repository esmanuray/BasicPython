citizens = []


class Citizen:
    def __init__(self, tc, password, name, surname, bday, location, montlyPay):
        self.tc = tc
        self.password = password
        self.name = name
        self.surname = surname
        self.birthday = bday
        self.location = location
        self.montlypay = montlyPay
        with open("citizen.txt", "a", encoding='utf-8') as file:
            citizen = 'tc:' + self.tc + ' , ' + 'sifre: ' + self.password + ' , ' + 'isim: ' + self.name + ' , ' + 'soyad: ' + self.surname
            citizen = citizen + ' , ' + 'dogum tarihi: ' + self.birthday + ' , ' + 'ikametgah: ' + self.location + ' , '
            citizen = citizen + 'aylık gelir: ' + self.montlypay + '\n'
            file.write(citizen)
            citizens.append(self)


def tcControl(tcNo):
    if len(tcNo) != 11:
        raise Exception('kimlik numarası 11 haneli olmalıdır.')
    elif not tcNo.isdigit():
        raise Exception('kimlik numarası rakamlardan oluşmalıdır.')
    elif tcNo.startswith('0'):
        raise Exception('kimlik numarası sıfır ile başlamaz.')
    elif int(tcNo) <= 0:
        raise Exception('kimlik numarsı sıfırdan küçük olamaz.')


def passwordcontrol(password):
    import re
    if 7 >= len(password):
        raise Exception('şifreniz en az 8 karakter olmalıdır.')

    elif not re.search('[a-z]', password):
        raise Exception('şifreniz en az bir tane küçük harf içermelidir.')

    elif not re.search('[A-Z]', password):
        raise Exception('şifreniz en az bir tane büyük harf içermeli.')

    elif not re.search('[!+%&@*_]', password):
        raise Exception('şifreniz (!+%&@*-_) karakterlerinden en az bir tane içermeli.')

    elif not re.search('[0-9]', password):
        raise Exception('şifreniz en az bir tane rakam içermeli.')


def bdayControl(bday):
    import re
    mount = list(range(1, 13))
    days = list(range(1, 32))
    list1 = bday.split('.')
    if len(bday) != 10:
        raise Exception('eksik giris yaptiniz.yıl ay ve gün arasına nokta koymayı unutmayın.\n'
                        'eğer noktaları doğru yerlere koyduysanız tek basamaklı tarihlerin başına sıfır ekleyin\n'
                        'örneğin: 1999.03.05')
    elif bday.count('.') != 2:
        raise Exception('Noktaları doğru yere koydugunuzdan emin olun.')
    elif len(list1[0]) != 4:
        raise Exception('yanlış yıl girdiniz.')
    elif int(list1[0]) < 1940:
        raise Exception('yanlış yıl girdiniz.')
    elif len(list1[1]) != 2:
        raise Exception('yanlış ay girdiniz.')
    elif not re.search(str(mount), list1[1]):
        raise Exception('1-12 arasında bir sayı ile ay bilgisini girin.')
    elif not re.search(str(days), list1[2]):
        raise Exception('hatalı ay girişi')
    elif re.search('[a-z]', bday) or re.search('[A-Z]', bday):
        raise Exception('geçersiz karakter.')


def FileUpdate(files, lineNum, change):
    with open(files, 'r') as file:
        lines = file.readlines()

    if lineNum >= 0 and lineNum <= len(lines):
        line = lines[lineNum]

        lineParts = line.split(' , ')

        for i, part in enumerate(lineParts):
            if change in part:
                x = input(f'{change}:')
                lineParts[i] = f'{change}: {x}'
                break
        updatedLine = ' , '.join(lineParts)
        lines[lineNum] = updatedLine

        with open(files, 'w') as file:
            file.writelines(lines)


while True:
    print('vatandaslik menüsune hoşgeldiniz.\n'
          'yapabilecekleriniz:\n'
          '1-yeni vatandaş girişi\n'
          '2-kayıtlı vatandaş görüntüleme\n'
          '3-vatandaş bilgilerini güncelleme\n'
          '4-çıkış')
    choice = input('seçiminiz:')

    if choice == '1':
        while True:
            try:
                a = input('tc kimlik numarası:')
                tcControl(a)
            except Exception as ex:
                print(ex)
            else:
                break
        print('şifreniz en az 8 karakter uzunluğunda, büyük/küçük harf,rakam ,!+%&@*_ karakterlerini içermeli. ')

        while True:
            try:
                b = input('şifre:')
                passwordcontrol(b)
            except Exception as ex:
                print(ex)
            else:
                break

        c = input('ad:')
        d = input('soyad:')
        while True:
            try:
                e = input('doğum tarihi (yyyy.aa.gg):')  # try
                bdayControl(e)
            except Exception as ex:
                print(ex)
            else:
                break
        f = input('ikametgah(il):')
        g = input('aylık gelir:')
        v = Citizen(a, b, c, d, e, f, g)


    elif choice == '2':
        with open('citizen.txt', 'r', encoding='utf-8') as file:
            num = 1
            for line in file:
                name = line.split('isim:')[1].split(', ')[0]
                surname = line.split('soyad:')[1].split(', ')[0]
                print(f'{num}-{name}{surname.upper()}')
                num += 1
        while True:
            print('vatandaşın bilgilerini görmek için sıra numarasını giriniz."0" (sıfır sayısı) girin')
            choice1 = int(input('numara:'))

            if choice1 <= num and choice1 != 0:
                with open('citizen.txt', 'r') as file:
                    kontrol = file.readlines()
                    kontrol = kontrol[(choice1) - 1].split(' , ')
                    print('Güvenlik kontrolü\n')
                    while True:
                        no = input('TC no:')
                        if no != kontrol[0].split('tc:')[1]:
                            print('TC numaraları uyuşmuyor.')
                        else:
                            break
                    while True:
                        sifre = input('Şifre:')

                        if sifre != kontrol[1].split('Şifre: ')[1]:
                            print('Yanlış şifre')
                        else:
                            break
                with open('citizen.txt', 'r') as file:
                    line = file.readlines()
                    print(line[(choice1) - 1])

            elif choice1 == 0:
                print('çıkış yapılıyor....')
                break

            else:
                print('hatalı giriş yaptınız.')


    elif choice == '3':
        with open('citizen.txt', 'r', encoding='utf-8') as file:
            num = 1
            for line in file:
                name = line.split('isim:')[1].split(', ')[0]
                surname = line.split('soyad:')[1].split(', ')[0]
                print(f'{num}-{name}{surname.upper()}')
                num += 1
        while True:
            print('güncellemek istediğiniz vatandaşın sıra numarasını seçin.')
            choice1 = int(input('numara:'))
            if choice1 <= num and choice1 > 0:
                with open('citizen.txt', 'r') as file:
                    kontrol = file.readlines()
                    kontrol = kontrol[(choice1) - 1].split(' , ')
                    print('Güvenlik kontrolü\n')
                    while True:
                        no = input('TC no:')
                        if no != kontrol[0].split('tc:')[1]:
                            print(kontrol[0].split('tc:')[1])
                            print('TC numaraları uyuşmuyor.')
                        else:
                            break
                    while True:
                        sifre = input('Şifre:')

                        if sifre != kontrol[1].split('Şifre: ')[1]:
                            print('Yanlış şifre')
                        else:
                            break
                with open('citizen.txt', 'r') as file:
                    line = file.readlines()
                    print(line[(choice1) - 1], '\n')

                while True:
                    change = input(
                        'değiştirmek istediğiniz veriyi birebir yaziniz.(örn: dogum tarihi)çıkmak için "çıkış" yazın:')
                    title = ['tc', 'sifre', 'isim', 'soyad', 'dogum tarihi', 'ikametgah', 'aylık gelir']
                    if change in title:
                        x = 'citizen.txt'
                        FileUpdate(x, int(choice1) - 1, change)

                        with open('citizen.txt', 'r') as file:
                            for i in file.readlines():
                                if i == int(choice1):
                                    print(i)
                    elif change == 'çıkış':
                        print('çıkış yapılıyor...')
                        break
                    else:
                        print('hatalı giriş. Tekar deneyin.\n')

            elif choice1 <= 0:
                print('çıkış yapılıyor...')
                break
            else:
                print('vatandaş numarasını hatalı girdiniz.\n')



    elif choice == '4':
        print('sistemden çıkılıyor...')
        break


    else:
        print('hatalı giriş yaptınız.\n')
