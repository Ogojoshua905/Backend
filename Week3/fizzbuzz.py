def fizzBuzz(n):
    for a in range(1, n+1):
        if a%3==0 and a%5==0:
            print(str("fizzBuzz"))
        elif a%5==0:
            print(str("Buzz"))
        elif a%3==0:
            print(str("Fizz"))
        else:
            print(a)
fizzBuzz(30)