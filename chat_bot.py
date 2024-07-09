def chat_bot():
    print("Welcome gangy!!") 
    response = input("What can I help you with today?")
    if (response == "calculate"):

        function = input ("what do you wanna calculate\n")
        num1 = int( input ("what's your first number\n"))
        num2 = int(input("what's your second number\n"))
        result = 0

        if (function == "addition"):
            result = num1 + num2
        elif (function == "substration"):
            result = num1 - num2
        elif (function == "multiplication"):
            result = num1 * num2
        elif (function == "division"):
            result = num1 / num2
        elif (function == "power"):
            result = num1 ** num2

            print("Your result is ", result)
chat_bot() 