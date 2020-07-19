#x,y,z= 5, 7 ,11

# print(x,y,z)

# x +=5  #x=x+5
# x -=8  #x=x-5
# x /=8  #x=x/8
# x *=8  #x=x*8
# x %=8  #x=x%8
# x //=8  #x=x//8

# print(x,y,z)

values = 1,2,3,4,5,6,[1,2,3]

print(type(values))

x,y,*z=values # x ve y sıradan elamanlara atanır. Sonra * sayesinde kalan tüm elemanlar z ye listelenir.

print(x,y,z)
print(z[4][0])