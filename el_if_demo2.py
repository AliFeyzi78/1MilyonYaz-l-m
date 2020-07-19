"""
1- girilen sayı 0-100 arasıda olup olmadığını kontrol ediniz
a=int(input("Bir sayı giriniz: "))
result= 0<a and a<100

print(f" Girilen sayı {a} 0 ile 100 arasındadır: {result}")
"""
# a=int(input("Bir sayı giriniz: "))
# if 0<a<100:
#     print(f" Girilen sayı:{a},  0 ile 100 arasındadır.")
# else:
#     print(f" Girilen sayı:{a},  0 ile 100 arasında değildir")

"""
2- girilen sayının pozitif çift sayı olup olmadığını kontrol ediniz
result= (0<a) and (a%2==0) and (a<100)
print(f" Girilen sayı : '{a}', pozitif, çift ve 100'den küçüktür: {result}")
"""
# a=int(input("Bir sayı giriniz: "))

# if 0<a<100:
#     if a%2==0:
#         print("sayı çift, pozitif ve 100'den küçüktür..")
#     else:
#         print("sayı tek, pozitif ve 100'den küçüktür.")
# elif a>100:
#     print("sayı 100'den büyüktür...")    

# else:
#     print("girilen sayı negatiftir...")


""" #3- email ve parola bilgileri ile giriş kont yapın
email="zeron1g2k@gmail.com"
parola="123"

g_mail=input("email Giriniz:..@..: ")
g_parola=input("Parola Giriniz: ")


if g_mail==email and g_parola==parola:
    print("bilgileriniz doğru. sisteme girebilirsiniz...")
elif g_mail==email and g_parola !=parola:
    print("yanlış parola girdiniz")
elif g_mail!=email and g_parola==parola:
    print("yanlış email girdiniz")

else:
    print("bilgilerinizi tekrar kontrol ediniz")
"""

"""
#4- girilen 3 sayıyı karşılaştırın
a=int(input("1. sayı giriniz: "))
b=int(input("2. sayı giriniz: "))
c=int(input("3. sayı giriniz: "))

if a<b and a<c:
    print("Girilen en küçük sayı :", a)
elif b<a and b<c:
    print("Girilen en küçük sayı :", b )
else:
    print("Girilen en küçük sayı: ", c)
"""
#5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayın
    # eğer ort. 50 ve üzeri ise geçti yoksa kaldı yazın
    # a) ortalama 50 olsa da final en az 50 olmalıdır
    # b) finalden 70 alındığında ortalamanın önemi olmasın
"""
vize1=float(input("vize1 gir:  "))
vize2=float(input("vize2 gir:  "))
final=float(input("final gir:  "))
result=(((vize1+vize2)/2)*0.6)+(final*0.4)

if result>=50:
    if final>=50:
        print("dersten geçtiniz")
    elif final<50:
        print("kaldınız...")
elif final>=70:
    print("Geçtiniz...")
else:
    print("kaldınız...")   
"""
#6- kişinin ad kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız
#formul:kilo / boy karesi
# 0-18.4 => zayıf
# 18.5-24.9 => normal
# 25.0-29.9 => fazla kilolu
# 30.0-34.9 => obez

ad=input("Adınız:  ")
kilo=float(input("Kilonuz:  "))
boy=float(input("Boyunuz (m):  "))
result=round((kilo/boy**2),2)

if result < 18.4:
    print(f"Sayın {ad} boy kilo endeksiniz: {result} olduğu için obezite durumunuz: Zayıf")
elif 18.5<result<24.9:
    print(f"Sayın {ad} boy kilo endeksiniz: {result} olduğu için obezite durumunuz: Normal")
elif 25<result<29.9:
    print(f"Sayın {ad} boy kilo endeksiniz: {result} olduğu için obezite durumunuz: Fazla kilolu")
else:
    print(f"Sayın {ad} boy kilo endeksiniz: {result} olduğu için obezite durumunuz: OBEZ!")


#print(f"Sayın {ad} boy kilo endeksiniz: {result} olduğu için durumunuzu True olan seçenekte görebilirsiniz zayıf:{0<result<=18.49}, normal:{18.50<=result<=24.99}, fazla kilolu:{25.00<=result<=29.99}, obez:{30.00<=result}")

