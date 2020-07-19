#1- girilen sayı 0-100 arasıda olup olmadığını kontrol ediniz
# a=int(input("Bir sayı giriniz: "))
# result= 0<a and a<100

# print(f" Girilen sayı {a} 0 ile 100 arasındadır: {result}")

#2- girilen sayının pozitif çift sayı olup olmadığını kontrol ediniz
# result= (0<a) and (a%2==0) and (a<100)
# print(f" Girilen sayı : '{a}', pozitif, çift ve 100'den küçüktür: {result}")

#3- email ve parola bilgileri ile giriş kont yapın
# email="zeron1g2k@gmail.com"
# parola="123"

# g_mail=input("email Giriniz:..@..: ")
# g_parola=input("Parola Giriniz: ")

# result=((email==g_mail.upper().strip()) and (parola==g_parola.upper().strip()))  # büyük küçük önemsememesi için girilen değeri küçük harf yapıyoruz ve boşlıkları kaldırıyoruz..

# print(f"Email ve parola bilgisi doğru mu: {result}")

#4- girilen 3 sayıyı karşılaştırın
# a=int(input("1. sayı giriniz: "))
# b=int(input("2. sayı giriniz: "))
# c=int(input("3. sayı giriniz: "))
# result1= (a<b and a<c)
# result2= (b<a and b<c)
# result3= (c<a and c<b)
# print(f" Girilen en küçük sayı {a} : {result1} ")
# print(f" Girilen en küçük sayı {b} : {result2} ")
# print(f" Girilen en küçük sayı {c} : {result3} ")

#5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayın
    # eğer ort. 50 ve üzeri ise geçti yoksa kaldı yazın
    # a) ortalama 50 olsa da final en az 50 olmalıdır
    # b) finalden 70 alındığında ortalamanın önemi olmasın

# vize1=float(input("vize1 gir:  "))
# vize2=float(input("vize2 gir:  "))
# final=float(input("final gir:  "))
# result=(((vize1+vize2)/2)*0.6)+(final*0.4)

# print(f"not ortalamanız:{result} ve dersten geçme durumu: {(result>=50 and final>=50) or (final>=70)}")

#6- kişinin ad kilo ve boy bilgilerini alıp kilo indexlerini hesaplayınız
# formul:kilo / boy karesi
# 0-18.4 => zayıf
# 18.5-24.9 => normal
# 25.0-29.9 => fazla kilolu
# 30.0-34.9 => obez

# ad=input("Adınız:  ")
# kilo=float(input("Kilonuz:  "))
# boy=float(input("Boyunuz (m):  "))
# result=round((kilo/boy**2),2)
# print(f"Sayın {ad} boy kilo endeksiniz: {result} olduğu için durumunuzu True olan seçenekte görebilirsiniz zayıf:{0<result<=18.49}, normal:{18.50<=result<=24.99}, fazla kilolu:{25.00<=result<=29.99}, obez:{30.00<=result}")