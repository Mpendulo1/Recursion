def factorial(number_1):
    if number_1 == 1 or number_1 == 0:
        return 1
    else:
        return number_1 * factorial(number_1 - 1)
number_1 = int(input('enter any number: '))
print(factorial(number_1))


# Exercise 1
