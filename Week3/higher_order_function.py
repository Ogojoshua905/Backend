# def func_one(name, def ):
#     return ""

#map() , filter(), reduce()

from functools import reduce

nums = [1,2,3,4,5]


# def add(x):
#     return x  + 2

mapped_func = map(lambda x:x + 2, nums)
# print(list(mapped_func))

# print(nums[4] % 2)

def modulos_calc(item_in_list):
    return (item_in_list % 2)  == 0
            # Or
# def modulos_calc2(item_in_list):
#     return (item_in_list % 2)  != 0

even_numbers = filter(modulos_calc, nums)

# print(list(even_numbers))


engineers = [
    {"person": "Sarah", "Profession": "Engineer"},
    {"person": "Kayode", "Profession": "Footballer"},
    {"person": "Charlse", "Profession": "Kung Fu Master"},
    {"person": "Joshua", "Profession": "Fullstack Developer"},
]

finding_engineers = filter(lambda person: person["Profession"] == "Engineer", engineers)

# print(list(finding_engineers))


# Reduce: Combine All the Items In a List Into a Single Result
num_1 = [
    1,
    2,
    3,
    4,
    5
    ]

def func(value_to_update,items_in_the_list):
    print(value_to_update + items_in_the_list)
    #print above
    return value_to_update + items_in_the_list

single_value = reduce(func,num_1) #number
# print(single_value)
# filter()

words = ['A', 'Stitch', "In", 'time', 'saves','nine']

def combine_words(initial_value, word):
    print(initial_value + "_____" + word)
    return initial_value + " " + word

result = reduce(combine_words, words)

print(result)