def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 * num1

def cube(num1):
    #return num1**3
    return num1 * num1 * num1

def power(num1, num2):
    #return num1**num2
    
    # anything to the power of 0 is 1
    if num2 == 0:
        return 1

    result = 1
    # otherwise, for num2, multiply num1 by itself that many times
    for i in range(num2):
        result = result * num1

    return result 

def mod(num1, num2):
    return num1 % num2