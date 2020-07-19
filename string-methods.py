message= "  hello there. my name is Fatih"

#message=message.upper()  tüm strg i büyük harfe çevirir.
#message=message.lower() tüm strg i küçük harfe çevirir.
#message=message.title() tüm string de her kelimenin baş harfi büyük
#message=message.capitalize() tüm string de sadece ilk kelimenin baş harfi büyük
#message=message.strip() kullanıcının girdiği boşlıkları-space- siler
message=message.split() #string i bölerek her bir karakter ayrı ayrı elaman olarak yazılır.
#message=message.split(".") #string i noktadan böler
message="--".join(message) #ayırdığımız string i arasına -- koyarak tekrar birleştirdik.
print(message)
print(message[1])
