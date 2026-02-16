class ValorantAgent:
    def __init__(self, name, gender, role ):
        self.name = name
        self.gender = gender
        self.role = role

    def best_agent(self):
        return f"{self.name} is the best {self.role} in this game"
    def worst_agent(self):
        return f"{self.name} is the worst {self.role} in this game"

agent1 = ValorantAgent("Jett", "Female", "Duelist")
agent2 = ValorantAgent("Sage", "Female", "Sentinel")
agent3 = ValorantAgent("Iso", "Male", "Duelist")

agent2.name = "Skye"
agent2.role = "Innitiator"

print(agent2.name)
print(agent2.role)
print(agent1.best_agent())
print(agent2.worst_agent())
print(agent3.best_agent())