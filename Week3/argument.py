# def areguments

def func(name, age):
    # logic
    return (name, age)

print(func("Alice", 31))







# Keyword Argument
def func_one(name="Alice", age=21, sex="female"):
    return (name, age, sex)

#Keyword Arguments
def func_one(name="Alice"):
    print(name)
#print (func_one())

def func_two(name, age, location="Lagos"):
    return (name, age, location)

print(func_two("Alice", 22))

print(func_two("Peter", 21, "Enugu"))


# Variable Length Argument
def func_three(*names):
    print(names)
    return True

# print(func_three("Alice", "Sarah", "Kayode", "Mari"))

# Kwargs
def func_four(**person):
    return person

print(func_four(name="Alice", age=22, Location="Lagos"))