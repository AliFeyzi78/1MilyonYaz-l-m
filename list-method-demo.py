names= ["Ali", "Yağmur", "Hakan", "Deniz"]
years= [1998, 2000, 1998, 1987]

# 1. "Cenk" isini listenin sonuna ekleyiniz.
names.append("Cenk")
result=names

# 2. "Sena" listenin başına ekleyiniz
names.insert(0,"Sena")
result=names

# 3. "Deniz" listeden siliniz
#names.remove("Deniz")
#names.pop(2)

# index=names.index("Deniz")
# names.pop(index)
result=names

# 4. "Deniz" indeksi nedir
result=names.index("Deniz")

# 5. "Ali" listenin bir elemanımıdır
#result=names.index("Ali")
result="Ali" in names

# 6. Elemanları Ters çevirin
names.reverse()
result=names

# 7. Alfabetik sıraya koyun
names.sort()
years.sort()
result=names,years

# 8. years rakamsal büyüklüğe göre sırala

# 9. str= "Kia, Dacia" karakter dizisini listeye çevirin
str= "Kia, Dacia"
result=str.split(",")


# 10. years en büyük ve en küçük elemanı nedir
result=max(years),min(years)

# 11. years kaç tane 1998 var
#result=years.count(1998)
print(years.count(1998))

# 12. years tüm Elemanlarını siliniz
years.clear()
result=years

# 13. kullanıcıdan 3 marka alıp liste yapın.
# a=input("1. Oto. Markası girin:   ")
# b=input("2. Oto. Markası girin:   ")
# c=input("3. Oto. Markası girin:   ")
# marka=[a,b,c]
#print(marka)

markalar=[]

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

marka=input("marka: ")
markalar.append(marka)

print(markalar)

print(result)