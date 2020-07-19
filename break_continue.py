# name="fatih KAYA"

# for letter in name:
#     if letter=="i":
#         break
#     print (letter)

# for letter in name:
#     if letter=="i":
#         continue
#     print (letter)

# x=0
# while x<5:
#     if x==2:
#         break
#     print(x)
#     x+=1

# while x<5:
#     x+=1
#     if x==2:
#         continue
#     print(x)
    
# 1- 1-100 arası tek sayıların toplamı nedir
x=0
y=0
while x<=100:
    x+=1
    if x%2==0:
        continue
    y+=x
    
    
print(y)
