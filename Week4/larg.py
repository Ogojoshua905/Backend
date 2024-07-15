numbers = [0, 1, 2, 4, 0, 10, 90]

lnum2 = numbers[0]

for num1 in numbers:
    if num1 > lnum2:
        lnum2 = num1
print(f"The Highest Number in the List is {num1}")

"""
Object Orientated Programming
"""
class LargestNumber:

    def __init__(self, numbers):
        self.numbers = numbers

    def find_largest_number(self):
        if not self.numbers:
            return None
        
        lnum = self.numbers[0]

        for num in self.numbers:
            if num > lnum:
                lnum = num
        
        return lnum

print("This is a program to find the largest number in a list")

finder = LargestNumber(numbers)
print(f"The Largest Number in the Above List is {finder.find_largest_number()}")