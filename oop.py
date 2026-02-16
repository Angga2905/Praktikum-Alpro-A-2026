#create a class
class MyClass:
  x = 5

#create object
p1 = MyClass()
print(p1.x)

#delete object
del p1
print(p1.x) 

#multiple objects
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)