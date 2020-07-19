sayılar=[1,3,5,7,9,12,19,21]

# 1- hangi sayılar 3 ün katıdır
# for x in sayılar:
#     if x%3==0:
#         print(f"bu litede 3'e bölünebilen sayılar: {x}")

# 2- sayıların toplamı kaçtır
# y=0
# for x in sayılar:
#     y=y+x    
# print(y)

# 3- tek sayıların karesini alınız
# for x in sayılar:
#     if x%2==1:
#         k=x**2
#         print(f"{x}'in karesi : {k}'dır")


sehirler=["izmir","sivas","malatya","bingöl","istanbul"]
#4- şehirlerden hangileri en fazla 5 karakterlidir.

# for a in sehirler:
#     if (len(a)<=5):
#         print(a)


urunler=[
    {"name":"samsung S6", "price": "3000"},
    {"name":"samsung S7", "price": "4000"},
    {"name":"samsung S8", "price": "5000"},
    {"name":"samsung S9", "price": "6000"},
    {"name":"samsung S10", "price": "7000"}
]

# 5- Ürünlerin fiyatları toplamı nedir

# toplam=0

# for t in urunler:
#     fiyat=int(t["price"])
#     toplam+=fiyat
# print(toplam)

# 6- fiyatları 5000 ve altı ürünleri göster

for fiyat in urunler:
    if int(fiyat["price"])<=5000:
        print(fiyat["name"])