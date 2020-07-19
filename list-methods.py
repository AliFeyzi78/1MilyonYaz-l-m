numbers=  [1,3,7,44,58,12,55]
letters=["a","c","f","k","a","s"]

val=min(numbers)
val=max(numbers)
val=max(letters)
val=min(letters)
val=numbers[3:5]
val=numbers[:5]
numbers[3]=13
numbers.append(2)
numbers.insert(2,22)
#numbers.pop()
numbers.pop(0)
numbers.remove(13)
numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(len(numbers))
print(len(letters))

print(numbers.count(58))
print(letters.count("a"))

print(numbers)
print(letters)
print(val)

numbers.clear()
print(numbers)