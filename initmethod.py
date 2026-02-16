#init
class ValorantAgent:
    def __init__(self, name, gender, role ):
        self.name = name
        self.gender = gender
        self.role = role

#default
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
print(p1.name, p1.age)

#self parameter
class ValorantSentinelAgent:
    def __init__(self, name, gender, tier ):
        self.name = name
        self.gender = gender
        self.tier = tier

#access prperty
def best_agent(self):
        return f"{self.name} is the best {self.role} in this game"
