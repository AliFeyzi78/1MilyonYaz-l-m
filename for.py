numbers=[1,2,3,4,5]

# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])

# for <değişken> in <liste,string, tuple...>:    yeni bir değişken atıyoruz. ve listedeki, stringdeki... ***eleman sayısı kadar**** prog. çalışıyor.

for x in numbers:
    print(x, ".hello")

harfler=["a","b","c","d"]
for y in harfler:
    print(f"benim harflerim are: {y}")

name="fatih kaya"
for z in name:
    print(z, "......") 

tuple=[(1,2),(3,4),(3,3)]
for a,b in tuple:
    print (a,b, "meraba") 

dic= {"k1": 1, "k2":2, "k3":3, "k4":4}
for k,v in dic.items():
    print(k,v)