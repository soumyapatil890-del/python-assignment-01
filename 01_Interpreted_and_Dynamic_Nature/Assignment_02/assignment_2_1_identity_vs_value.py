# Part A: Mutables
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

# Part B: Memory IDs
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))

# Part C: Small Integer Caching
a = 256
b = 256

print("a is b (256):", a is b)

x = 257
y = 257

print("x is y (257):", x is y)

# Part D: Mutability
list1.append(4)

print("After list1.append(4):")
print("list1:", list1)
print("list3:", list3)