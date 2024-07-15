# from random import randint

# rolls = [randint(1, 6) for _ in range(100)]

# count = sum(1 for roll in rolls if roll == 6)

# print(count)

import random
import math

# count = 0
# for i in range(11):
#     n = [random.random() for _ in range(11)]
#     count +=1
#     if count == 10:
#         mean = sum(n) / count
#         print(mean)

def statistical_analysis(n):
    numbers = [random.random() for _ in range(n)]
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    std_dev = math.sqrt(variance)
    inside_one_std_dev = sum(1 for x in numbers if mean - std_dev <= x <= mean + std_dev)
    
    print(f"Mean: {mean:.2f}")
    print(f"Numbers: {numbers}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Numbers within one standard deviation: {inside_one_std_dev:.2f}")

statistical_analysis(10)
