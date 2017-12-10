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

#2

class Person: 
    def __init__(self, age, name, second_name, birthday_month): 
        self.age = age 
        self.name = name.capitalize()
        self.second_name = second_name.capitalize()
        self.birthday_month = birthday_month 
    def full_name(self):
        return self.name + ' ' + self.second_name
    def email(self):
        return (self.name + '.' + self.second_name + '@email.com').lower()

body = Person(age=18, name='peDro', second_name='VillALobos', birthday_month='Marth') 

print body.age, body.name, body.second_name, body.birthday_month 
print body.full_name()
print body.email()
