age = int(input("How old are you? \n"))
x = True
def age_checker(age):
    
    while(x == True):
        
        if (age <= 11):
            print("You are a child")
            
        elif(age >11 and age <= 19):
            print("You are a teen")
            
        elif(age >=20):
            print("You are an adult")
        ans = input("Do you want to continue? (all lowercase)\n")
        if ans == "no":
            break
        
age_checker(age)