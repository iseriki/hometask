#1
class Boxer:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height= height
    def kick(self):
        return "I'll kill you!!!"
    def pull_ups(self):
        return "I can make 50 pull-ups!!!"

vasily = Boxer(name='Vasily:', age='age 22,', weight='weight 100,', height='height 150.')

print vasily.name, vasily.age, vasily.weight, vasily.height
print vasily.kick()
print vasily.pull_ups()

