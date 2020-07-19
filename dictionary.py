# key--> value

# 58- sivas  12- bingöl

# sehirler=["bingöl", "sivas"]
# plakalar=[12,58]

# print(plakalar[sehirler.index("sivas")])

# #print(plakalar["sivas"]) => 58    buna ulaşmak istiyoruz..

# # #####################
# değişken={key:value, key:value, ...}

# plakalar={"sivas":58, "bingöl":12, "malatya":44, "ankara":6}

# print(plakalar["bingöl"])

# plakalar["izmir"]=35  #### dic. eleman eklemek için kullanırız
# plakalar["sivas"]=588  #### dic içindeki var olan elemanın değerini değiştirmek için

# print(plakalar)

users= {
    "fatih": {
        "age":41,
        "roles": ["admin","user"],
        "email": "aaaaa@.com",
        "gender": "E",
        "adress":"ankara",
        "phone":"02145114"
    },

    'songul':{
        "age":39,
        "roles": ["user"],
        "email": "ssss@.com",
        "gender": "K",
        "adress":"ankara",
        "phone":"12555554"
        
    }
}
print(users["fatih"]["roles"][0])
print(users)