num = int(input("What do you want to start at? \n"))
def countdown(num):
    for i in range(num):
        print(num-i)

countdown(num)