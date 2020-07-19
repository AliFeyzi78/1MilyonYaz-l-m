# 1- kullanıcıdan yaş isim ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#     ehliyet alabilme durumu en az 18 eğitim lise veya üniversite olmalıdır

"""name= input("isminiz:  ")
#bdate= int(input("Doğum yılınız:  "))
#age= 2020-bdate
age= 2020-int(input("Doğum yılınız:  "))
edu= input("mezunuyetini Lise ise 'L', universite ise 'U', değilse 'D' giriniz:  ")

if (age >= 18) and (edu == "L" or edu=="U") :
    print (f"Sayın {name} yaşınız {age} ve mezuniyetiniz {edu} olduğu için: Ehliyet alabilirsiniz....")
else:
    print("Şartları sağlamadığınız için Ehliyet ALAMAZSINIZ... ")"""

"""2- örencinin 2 yazılı  1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığını yazdırın.
    0-24 =>0
    25-44 =>1
    45-54 =>2
    55-69 =>3
    70-84 =>4
    85-100 =>5"""
"""yNotu1=float(input("1. Yazılı Notunuz: "))
yNotu2=float(input("2. Yazılı Notunuz: "))
sNotu=float(input("Sözlü Notunuz: "))
ort=(yNotu1+yNotu2+sNotu)/3

if (0 < ort <=24):
    print(f"Ortalamanız:{ort} ve Notunuz: 0")
elif (25< ort <= 44 ):
    print(f"Ortalamanız:{ort} ve Notunuz: 1")
elif (45< ort <= 54 ):
    print(f"Ortalamanız:{ort} ve Notunuz: 2")
elif (55< ort <= 69 ):
    print(f"Ortalamanız:{ort} ve Notunuz: 3")
elif (70< ort <= 84 ):
    print(f"Ortalamanız:{ort} ve Notunuz: 4")
else:
    print(f"Ortalamanız:{ort} ve Notunuz: 5")"""

""" 3- trafiğe çıkış tarihi alınan bir aracın servis zamanı hesapla ve yazdır
1. Bakım => 1. yıl
2. Bakım => 2. yıl
3. Bakım => 3. yıl
** süre hesabını gün, ay, yıl bilgisine göre gün bazlı hesaplayın
***datetime modülü kullanılacak """

import datetime

x=datetime.datetime.now()
print("Aracın trafiğe çıkış tarihini gün/ay/yıl olarak giriniz")
gun = int(input("gün: "))
ay = int(input("ay: "))
yıl = int(input("yıl: "))

t= datetime.datetime(year=yıl, month=ay, day=gun)
tfark=x-t
#tfark=tfark.days (bu kısım gün farkını bize sadece gün olarak verir.)

print("geçen gün sayısı:", tfark)


if tfark<=datetime.timedelta(365):
   print("Bakım tarihiniz henüz gelmedi...")
elif datetime.timedelta(365)<tfark<=datetime.timedelta(730):
    print("1. bakımınızı yaptırınız....")
elif datetime.timedelta(731)<tfark<=datetime.timedelta(1095):
    print("2. bakımınızı yaptırınız....")
else:
    print("3. bakımınızı yaptırınız....")

"""tarih=input("aracınızın trafiğe çıkış tarihini 'yıl/ay/gün' olarak  giriniz: ")
tarih=tarih.split("/")
trafigeCıkıs=datetime.datetime(int(tarih[0]), int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi - trafigeCıkıs    
tfark=fark.days
print(tfark)

if tfark<=365:
       print("Bakım tarihiniz henüz gelmedi...")
elif 365<tfark<=365*2:
    print("1. bakımınızı yaptırınız....")
elif 365*2<tfark<=365*3:
    print("2. bakımınızı yaptırınız....")
else:
    print("3. bakımınızı yaptırınız....")"""