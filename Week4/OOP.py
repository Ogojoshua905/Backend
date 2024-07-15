'''
OOP || Object Oriented Programing
'''

class Person():
    '''
    __init__ is A Constructor
    '''
    # def __init__(self):
        # self.name = "Joshua"
        # self.age = 17
        # self.complexion = "Dark"
        # self.gender = "Male"
    # def speak(self):
    #     return f"Hi My Name is {self.name} and I'm {self.age}"
        # or
# miracle = Person()
    country = str("Nigeria")
    def __init__(self, name, age, complexion, sex):
        self.name = name
        self.age = age
        self.complexion = complexion
        self.sex = sex
    #Methods
    def action(self):
        self.action = "Run"
        return self.action

    def speak(self): #PS: return can be InterChangeable with Print
        print(f"Hi My Name is {self.name} and I'm {self.age} and PS: I'm a {self.complexion} Skin {self.sex}")

byteprowler = Person("Joshua", 17, "Dark", "Boy") #instance
sayrah = Person("Sarah", 25, "Light", "Gyal") #instance

print(byteprowler.speak()) 
print(sayrah.speak())
print(sayrah.action())
# print(sayrah.country) 