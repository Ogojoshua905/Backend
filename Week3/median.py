numbers = []
count = 0
while 1:
    user = input("Enter Your Numbers: ")
    if user.isdigit():
        user = int(user)
        count += 1
        numbers.append(user)
        if count == 8:
            break
numbers.sort()
mean = sum(numbers) / len(numbers)
length = len(numbers)
if length % 2 == 0:
    a = numbers[length%2-1]
    b = numbers[length%2]
    median = (a + b) / 2
    print(f"Median : {median}")
else: 
    median = numbers[length%2]
    print(f"Median: {median}")
print(f"Mean: {mean}")
