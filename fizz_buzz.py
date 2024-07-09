def fizz_buzz(num):
    if (num % 3 == 0 ):
        print("fizz")
    elif (num % 5 == 0):
        print ("Buzz")
    elif (num % 3 and num % 5):
        print ("buzz fizz")
    else:
        print ("not fizz or buzz")

fizz_buzz (4)
fizz_buzz (35)
fizz_buzz (15)
fizz_buzz (9)

