# 1. "BMW, Mercedes, Opel,Mazda" elemanlarına ait bir liste oluşturun.
arabaM=["BMW", "Mercedes", "Opel", "Mazda"]
result=arabaM

# 2. Liste kaç elemanlıdır.
result=len(arabaM) 

# 3.Listenin ilk ve son elemanı nedir.
result= arabaM[0], arabaM[-1]

# 4. Mazda değerini Toyota ile değiştirin.
#arabaM[-1]="Toyota"
result=arabaM

# 5. Mercedes Listenin bir elemanımıdır.
# result=arabaM.index("Mercedes")
result="Mercedes" in arabaM

# 6. Listenin -2 değerindeki eleman nedir.
result=arabaM[-2]

# 7. Listenin ilk 3 elemanını alın
result=arabaM[0:3]

# 8. Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
#["BMW", "Mercedes", "Opel", "Mazda"]
arabaM[-2:]="Toyota","Renault"
result=arabaM

# 9. Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
#yeni=["Audi","Nissan"]
#arabaM.insert(4,"Audi")
#arabaM.extend(yeni)
#result=arabaM
result=arabaM+["Audi","Nissan"]

# 10. Listenin son elamanını silin.
del arabaM[-1]
#arabaM.remove("Nissan")
# arabaM.pop()
result=arabaM

# 11. Liste elemanlarını tersten yazdırın
#arabaM.reverse()
#result=arabaM
result=arabaM[::-1]

# 12. Aşağıdaki verileri bir liste içinde saklayınız:
     #     studentA: Yiğit Bilgi 2010, (70,60,70)
     #     studentB: Sena Turan  1999, (80,80,70)
     #     studentC: Ahmet Turan 1999, (80,70,90)

studentA= ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB= ["Sena", "Turan" , 1999, [80,80,70]]
studentC= ["Ahmet" ,"Turan", 1999, [80,70,90]]
#liste1=studentA+studentB+studentC
#print(liste1)

# 13. Liste elemanlarını ekrana yazdırın.
# result=studentA[0] 
# result=studentB[2]
# result=studentC[3][1]

# "Yiğit Bilgi 9 yaşında ve not ortalaması 66" yazdırmak istiyoruz
result = f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"  


print(result)