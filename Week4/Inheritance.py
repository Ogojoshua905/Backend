# class Father():
#     def __init__(self):
#         self.surname= "Pepple"
#     def description(self):
#         return f"This is from the Line Of the {self.surname} family"
# class Son(Father):
#     def  __init_subclass__(cls):
#         return super().__init_subclass__()
#     def description(self):
#         return "I'm now part of the Family of Ajegunle"
    
# excel = Son()
# print(excel.description())

#Polymorphism
"""
The Condition of Occuring in Several different Forms
The Ability of different object to respond each in its own way or method call 
"""
def Sum(a, b):
    return a + b

class Merge():
    def sum(self, a,b):
        return a + b
    
addition = Merge()

concat = Merge()

print(concat.sum("Hello", "World"))

print(f"{addition.sum(1, 2.0695):.2f}")