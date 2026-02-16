#class property
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

#access

print(p1.name)
print(p1.age)

#modify
p1.age = 26
print(p1.age)

#delete
del p1.age

print(p1.name)