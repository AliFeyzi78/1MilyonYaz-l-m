"""
ogrenciler= {
    "ogrenci1":{
        "ögr.No1":input("Öğr.no:  "),
        "ad":input("Adınız: "),
        "soyad":input("Soyadınız: "),
        "tel":input("Tel: ")
    },
    "ogrenci2":{
        "ögr.No2":input("öğr.No2: "), 
        "ad":input("Adınız: "),
        "soyad":input("Soyadınız: "),
        "tel":input("Tel: ")
    },
    "ogrenci3": {
        "öğr.No3":input("öğr.No3:"),
        "ad":input("Adınız: "),
        "soyad":input("Soyadınız: "),
        "tel":input("Tel: ")
    }
}
   
print (ogrenciler)

while True:
    ogr = input ("Öğr. No Giriniz: ")
    
    if ogr=="121":
        print(ogrenciler["ogrenci1"])
    elif ogr=="122":
        print(ogrenciler["ogrenci2"])
    elif ogr=="123":
        print(ogrenciler["ogrenci3"])
    else:
        print("yanlış bir no girdiniz. tekrar deneyin..")
        break
"""
ogrenciler = {}

number= input("öğrenci no:  ")
name= input("öğrenci adı:  ")
surname= input("öğrenci soyad:  ")
phone= input("öğrenci telefon:  ")

# ogrenciler[number] = {
#     "ad": name,
#     "soyad": surname,
#     "telefon": phone,
# }

ogrenciler.update({
    number:{
        "ad": name,
        "soyad": surname,
        "telefon": phone, 
    }
})

number= input("öğrenci no:  ")
name= input("öğrenci adı:  ")
surname= input("öğrenci soyad:  ")
phone= input("öğrenci telefon:  ")

ogrenciler.update({
    number:{
        "ad": name,
        "soyad": surname,
        "telefon": phone, 
    }
})

number= input("öğrenci no:  ")
name= input("öğrenci adı:  ")
surname= input("öğrenci soyad:  ")
phone= input("öğrenci telefon:  ")

ogrenciler.update({
    number:{
        "ad": name,
        "soyad": surname,
        "telefon": phone, 
    }
})

print(ogrenciler)

print("*"*75)

ogrNo=input("öğrenci no: ")
ogrenci=ogrenciler[ogrNo]

print(ogrenci)

#print(f "Aradığınız {"ogrNo"} nolu öğrencinin adı: {ogrenci["ad"]} soyadı:{ogrenci["soyad"]} ve telefonu ise {ogrenci["telefon"]}")   


 