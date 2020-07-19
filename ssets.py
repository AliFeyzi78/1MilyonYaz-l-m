fruits={"apple", "orange", "banana"}

#print(fruits)
# print(fruits[0]) indexlenemez

for x in fruits:
    print(x)
fruits.add("chery")
#print(fruits)

fruits.update(["grape", "melon"])
#print(fruits)

# myList=[1,2,2,3,4,4,5]
# print(myList)
# print(set(myList))

fruits.remove("melon")
fruits.discard("apple")
fruits.pop()
fruits.clear()


print(fruits)