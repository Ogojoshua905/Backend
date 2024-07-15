class Dog:
    def __init__(self, species):
        self.species = species
    legs=4

    def sound(self):
         self.type = "woof"
         return "Bark"
    
    def dog_say(self):
         total = self.sum(1,1)
         return f"I am a Dog, But i know MAth. One Plus One Equals to {total}"
    @classmethod #v decorator
    def print_legs(cls):
        return f"I have {cls.legs} leg"
    @staticmethod #utils function
    def sum(a, b):
            return a + b

#del fluffy.species -- attribute deleted
#del fluffy.dog_says -- method deleted
#del fluffy -- Object or Instance deleted

dg = Dog("German Shephard")
# del dg.species
# print(f"{dg.print_legs()} so {dg.species}")



# Inheritance


class Father:
    def __init__(self):
          self.surname = "Nnanna"
          self.net_worth = 65000000

    def description(self):
        return f"The Family Of {self.surname}"


class Daughter(Father):
     def __init__(self):
        super().__init__() #super() is used to call the parent class
     
mari = Daughter()

print(mari.surname)