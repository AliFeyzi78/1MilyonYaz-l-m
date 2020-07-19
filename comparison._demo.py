# 1- girilen iki sayıdan hangisi büyük
# a=int(input("1.sayı: "))
# b=int(input("2.sayı: "))
# result=(a>b)
# print(f"1.sayı :{a}, 2. sayıdan: {b} büyüktür: {result} ")

# 2- kullanıcıdan 2 vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız
# vize1=float(input("vize1 gir:  "))
# vize2=float(input("vize2 gir:  "))
# final=float(input("final gir:  "))
# result=(((vize1+vize2)/2)*0.6)+(final*0.4)

#     Eğer ortalama 50 ve üst,ndeyse geçti değilse kaldı yazdırın
# if (result>=50):
#     print("Geçtiniz")
# else:
#     print("kaldınız...") 

# print(f"not ortalamanız:{result} ve dersten geçme durumunuz: {result>=50}")

# 3- girilen sayının tek mi çift mi olduğunu kontrol ediniz.
# a=int(input("1 sayı giriniz: "))
# result=a%2
# # if (result==0):
# #     print("Girilen sayı çifttir")
# # else:
# #     print("Girilen sayı tektir")

# print(f"Girilen sayının çift olma durumu: {result==0}")

# 4- girilen bir sayının negatif pozitif durumunu yazdırın
# a=int(input("1 sayı giriniz: "))
# # if (a>=0):
# #     print("Girilen sayı Pozitiftir")
# # else:
# #     print("Girilen sayı Negatiftir")
# print(f"Girilen sayını pozitif olma durumu: {a>=0}")


# 5- parola ve email bilgisini isteyip doğruluğunu kontrol ediniz
#     email:zeron1g2k@gmail.com  parola:123456
# email=input("email Giriniz:..@..: ")
# parola=input("Parola Giriniz: ")

# if (email=="zeron1g2k@gmail.com") and (parola=="123456"):
#     print("Sisteme Girişiniz başarılı")
# else:
#     print ("Tekrar deneyiniz..")

email="zeron1g2k@gmail.com"
parola="123"

g_mail=input("email Giriniz:..@..: ")
g_parola=input("Parola Giriniz: ")

s_mail=(email==g_mail.upper().strip()) # büyük küçük önemsememesi için girilen değeri küçük harf yapıyoruz ve boşlıkları kaldırıyoruz..
s_parola=(parola==g_parola.upper().strip())

print(f"Email bilgisi doğru mu: {s_mail} ve parola doğru mu: {s_parola}")


#print(result)