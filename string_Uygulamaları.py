website= "http://www.sadikturan.com"
course= "Python kursu: Baştan sona Programlama (40 saat)"

#1 " Hello World " karakter dizisindeki baş ve son boşlukları silin
#s= " Hello World "
# print(s)
#s=s.strip()
# #s=s.lstrip() soldaki boşluğu siler
# #s=s.rstrip() sağdaki boşluğu siler
# result=website.lstrip("/:htp") # 'result'-> direkt komutu çalıştırıyor. silmek istediğimiz karakterleri yazıyoruz 
# print(s)
result= ' Hello World  '.strip()

# 2 - "www.sadikturan.com" içindeki sadıkturan haricindeki tüm karakterleri silin.
# print(website)
# print(website[11:25])
result='www.sadikturan.com'.strip('wmoc.')

#3- "course" karakter dizisinin hepsini küçük harf yapın
print(course.lower())
# print(course.upper())
# print(course.title())

#4- "website" içinde kaç tane "a" vardır
# print(website.count("a"))
result=website.count('a')
result=website.count("www",0,10) # 0 ile 10 ncu karakterler arasında arama yapar.

#5- "website" www ile başlayıp com ile bitiyor mu
result= website.startswith("www")
result= website.startswith("http")
result= website.endswith("com")

#6- "website" içinde "com" var mı
result= website.find("com")
result= website.find("com",0,10) # 0 ile 10 ncu karakterler arasında arama yapar. varsa index nosunu yoksa -1 verir. 
#result= course.index("sona")
result= course.rfind("sona")

#7- "course" içindeki karakterlerin hepsi alfabetik mi
result= course.isalpha()
result= course.isdigit()
#result= "123".isdigit() true değerini verir.

#8- "Contents" ifadesini satırda 50 karakter içinde yerleştirip,sağ ve soluna * yerleştirin
result= "*Contents*".center(50,"*")
# result= "*Contents*".ljust(50,"*") ifadeyi sola yaslar ve sağa yıldız ekler
# result= "*Contents*".rjust(50,"*") sağa yaslar

#9- "course" içindeki karakter dizisindeki boşluklara "-" koyun 
# course=course.split()
# course="-".join(course)
# print(course)
result= course.replace(" ", "-")
result= course.replace(" ", "")
#result= course.replace(" ", "-", 2) sadece 2 karaktere - koyar

#10- "Hello World" karakter dizisinin "world" ifadesini "There" olarak değiştirin
#s="Hello World"
# print(s)
#result= s.replace("Hello","There")
result= "Merhaba Dünya".replace("Merhaba", "Naber")

#11- "course" içindeki karakter dizisindeki boşluklardan ayırın.
# course=course.split()
# print(course)
result=course.split(" ")
#result=result[2]
result=result[4]

print(result)