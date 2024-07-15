def Add(first_Number, second_Number):
    return first_Number + second_Number

# def Add():
#     return 1 + 1

# def introduction():
#     name="Stephen"
#     return f"Hi my name is {name}"

# print(introduction())

def Enquiry(item):
    if item == "rice and beans":
        return "700"
    elif item == "egg":
        return "70"
    else:
        return "None"
 
    
def ask_and_response():
    value = input("What do you want to Buy: ")
    return "The Price is" + " " + Enquiry(value)

response = ask_and_response()

print(response)

# def name():
#     #logic
#     num1 = 1
#     num2 = 2
#     return num1 + num2


# print(sum())