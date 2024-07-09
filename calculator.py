def calculator (num1, num2, function):
    if (function == "addition"):
        print(num1 + num2)
    elif (function == "substration"):
        print(num1 - num2)
    elif (function == "multiplication"):
        print(num1 * num2)
    elif (function == "division"):
        print(num1 / num2)
    elif (function == "power"):
        print(num1 ** num2)    
    else:
        print ("error")
calculator(3,6,"subtraction")
calculator (4,6,"multiplication")
calculator (43,7,"division")
calculator (5,8, "addition")