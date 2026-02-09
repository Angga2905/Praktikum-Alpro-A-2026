#arithmetic
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#division
x = 12
y = 5

print(x / y)

x = 12
y = 5

print(x // y)

#Assignment Operators


#walrus operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operator
x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))

#identity operator  
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#membership
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

#membership in strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#bitwise operators
print(6 & 3)

#Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

