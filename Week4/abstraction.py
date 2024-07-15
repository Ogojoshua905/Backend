# Abstraction
from abc import ABC, abstractmethod
""" 
Abstraction is the process of hiding the implementation details 
from the user and providing only the essential information.
it's Like a Simplified model of a Complex System. 
Think Of it as focusing on what an Object does rather than How it does it
"""

"""
My Understanding Of Abstraction:
So In General. An Abstraction is A Class that creates necessary Methods That Must
be used when It's inherited in Other Class or Other Subclasses
"""

class Payment(ABC):
    def process_payment():
        pass
    @abstractmethod
    def refund(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class Paystack(Payment):
    def process_payment(self, amount):
        return f"Processing Payment of Amount Of {amount}"
    def refund(self, amount):
        return f"Refunding Payment Of Amount {amount}"
    def check_balance(self, amount):
        return f"Your Balance is {amount}"
    def description(self, amount):
        return "This is Paystack's Payment Services"
    
class Flutter(Payment):
    def process_payment(self, amount):
        return f"Processing Payment of Amount Of {amount}"
    def refund(self, amount):
        return f"Refunding Payment Of Amount {amount}"
    def check_balance(self, amount):
        return f"Your Balance is {amount}"
    def description(self, amount):
        return "This is Flutterwave's Payment Services"
     
paystack = Paystack()

print(paystack.check_balance(45360))
