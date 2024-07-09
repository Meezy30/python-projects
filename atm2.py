import getpass
checking = 600
def withdrawal (checking):
    withdrawal=int(input("How much do you want:"))
    newbal=checking=withdrawal
    return newbal
def deposit(checking):
    deposit=int(input("How much do you want to add"))
    newbal=checking+deposit
    return newbal
def balance(checking):
    print(checking)
def main():
    print("Welcome to Myles bank?")
    username=input("What is your username?")
    password= getpass.getpass()
    print(password)
    print ("Welcome!", username)

    choice=int(input("(1)withdrawal,2)deposit,3 balance"))
    if (choice==1):
        withdrawal()
    elif (choice==2):
        deposit()
    elif (choice==3):
        balance()
    else:
        print("Try again")
main()