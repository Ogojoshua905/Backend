# Recursion is A Technique Where You call a Function inside another Function

def outer_function(name):
    if name == "Joshua":
        return "Finally"
    else:
        print("Mari")
        outer_function(name)


# print(outer_function("Mari")) 



def factorial(n):
    # Base Case
    return n * factorial(n - 1)
#Example Usage
#print(factorial(5)) #output: 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)



text= "Find The Letter T Inside Of me"


def search(index):
    if text[index] == "T":
        return "FOUND IT !!!"
    else:
        print("Keep Searching....")
        return search(index + 1)
    
print(search(0))