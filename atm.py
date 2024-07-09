def atm():
    num = int(input("What is your starting amnt"))
    process = input("what do you want to do?")
    if process == "deposit":
        depositamnt = int(input("How much do you want to deposit"))
        num = depositamnt + num
        print("Total is: " + str(num))

    elif process == "withdrawal":
        withdrawalamnt = int(input("How much would you like to withdraw?"))
        num = num - withdrawalamnt 
        print("Total is: " + str(num))
    else:
        print("Error")

atm()