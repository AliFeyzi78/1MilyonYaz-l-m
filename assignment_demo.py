x,y,z= 2,5,10
numbers=1,5,7,10,6


# 1- Kullanıcıdan aldğınız 2 sayının çarpımı ile x y z toplamının farkı nedir
# sayı1=int(input("1. sayıyı giriniz: "))
# sayı2=int(input("2. sayıyı giriniz: "))
# print((sayı1*sayı2)-(x+y+z))

# 2- y nin x e kalansız bölümünü hesaplayınız
print  (y//x)

# 3- x y z toplamının mod3 ü nedir
print ((x+y+z)%3)

# 4- y nin x inci kuvveti
print (y**x)

# 5- x *y z = numbers işlemine göre  z nin küpü kaçtır
x,*y,z = numbers
print(z**3)

# 6- x *y z = numbers işlemine göre y nin değerleri toplamı kaçtır
x,*y,z = numbers
print((y[0])+y[1]+y[2])
