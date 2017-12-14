class Animal:
    def __init__(self, tail, paw, wool):
        self.tail = tail
        self.paw = paw
        self.wool = wool
    def outing(self):
        return self.tail, self.paw, self.wool

class Dog(Animal):
    def say_someting(self):
        return 'Woof-woof'

class Cat(Animal):
    def say_someting(self):
        return 'Meow-meow'

class SphynxCat(Cat):
    def say_someting(self):
        return 'Murr-murr'

class Rooster(Animal):
    def say_someting(self):
        return 'Cocorico'

some_animal = Animal(tail = 1, paw = 4, wool = True)
doggy = Dog(tail = 1, paw = 4, wool = True)
kitty = Cat(tail = 1, paw = 4, wool = True)
vasya = SphynxCat(tail = 1, paw = 4, wool = False)
petya = Rooster(tail = 1, paw = 2, wool = False)

print some_animal.outing()
print doggy.outing(), doggy.say_someting()
print kitty.outing(), kitty.say_someting()
print vasya.outing(), vasya.say_someting()
print petya.outing(), petya.say_someting()
