# common object

a=10
b=10
c=10


print(a,id(a), b, id(b), c, id(c))

c=11
b=12

print(a,id(a), b, id(b), c, id(c))


c=c-1
print(a,id(a), b, id(b), c, id(c))



# Garbage collection
a=10
b=10
c=10


print("before deleting ",a,id(a), b, id(b), c, id(c))

# deleting the reference
del a

print("after deleting ", b, id(b), c, id(c))


# OPERATORS
# true division return float ans
print(9/5)

#flor division  -> return int ans only
print(9//5)

# Priority operator
# ** , / , //, *,  %
 
# In case of same order associativity  as below example then left to right 
print(2 * 3 // 2 % 2 * 5 / 2)


# for exponent it will be right to left
print(2** 3** 2)

print(len('''hello
world'''))

print(0 or (5>2))