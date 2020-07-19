sayılar=[1,3,5,7,9,12,19,21]

# 1-sayılar listesini while ile yazdır
# i=0
# while (i<len(sayılar)):
#     print(sayılar[i])
#     i+=1

# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları yazdır.

# i=int(input("Başlangıç değerini gir: "))
# s=int(input("son değeri gir: "))

# while i<=s:
#     if i%2==1:
#         print(i)
#     i+=1

# 3- 1 20 arası sayıları tersten yazdır

# x=20
# while x>0:
#     print(x)
#     x-=1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı şekilde yazdır
"""a = int(input("1. sayı gir: "))
b = int(input("2. sayı gir: "))
c = int(input("3. sayı gir: "))
d = int(input("4. sayı gir: "))
e = int(input("5. sayı gir: "))

f=[a,b,c,d,e]
f.sort()
print(f)"""
# numbers=[]
# i=0
# while i<5:
#     sayi=int(input("sayı: "))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)


# 5- kullanıcıdan alacağınız x sayıdaki  ürün bilgisini ürünler listesi içinde saklayacağımız
    # ** ürün sayısını kullanıcıya sorun
    # ** dic listesi yapısı (name,price) şeklinde olsun
    # ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile yazdır.

urun_say=int(input("Kaç Ürün Gireceksiniz?  :"))
urunler=[]
x=1
while x<=urun_say:
    name=input("name: ")
    price=input("price :")
    urunler.append({
        "name":name,
        "price":price})
    
    x+=1
print(urunler)

for u in urunler:
    print(f'Ürun adı: {u["name"]} ürün fiyatı: {u["price"]}')