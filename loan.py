name = input ("Name: ")

def takeincome(num):
    if num < 500:
        return 'payscale1'
    elif num < 1000:
        return 'payscale2'
    else:
        return 'payscale3'

def criteria1 ():
    print('''Are you employed?)
                 - No
                 - Part time''')
    employment = input ('Please choose one of the provided options: ')
    if employment == 'No':
        print ("Unfortunatelly we cannot lend you any money")
    else:
        print('''What will you use this money for?
                 - Debt
                 - Car
                 - Holiday''')
        purpose = input ('Please choose one of the provided options: ')
        criteria2(purpose)

def lencalc (money):
    print('''How long do you want to borrow it for(in months)?
                         - 1
                         - 6 
                         - 12''')
    length = int(input(": "))
    calculation = money*5/length
    print("We have done our calculation and the good news is that you'll have to pay us back", money * 5,"over", length, "months.")
    print("Your monthly rate will be £", calculation)


def criteria2 (strg):
    amountborr = [100,200,300,400,500,600,700,800,900,1000]
    income = int (input("What's your annual income?: "))
    if takeincome(income)== 'payscale1':
        if strg == 'Debt':
            print ("you can borrow between £100 and £400.")
            amount = int(input("How much would you like to borrow? (The amount has to be in hundreds): "))
            if amount in amountborr[0:4]:
                print ("Luky you, we can lend you", amount,"pounds straightaway.")
                lencalc (amount)
            else:
                print("Sorry, it has to be between £100 and £400.")
        else:
            print ("you can borrow between £100 and £600.")
            amount = int(input("How much would you like to borrow? "))
            if amount in amountborr[0:6]:
                print ("Luky you, we can lend you", amount,"pounds straightaway.")
                lencalc (amount)
            else:
                print("Sorry, it has to be between £100 and £600.")
          
    elif takeincome(income)== 'payscale2': 
        print ("you can borrow between £100 and £1000.")
        amount = int(input("How much would you like to borrow? "))
        if amount in amountborr[0:]:
            print ("Luky you, we can lend you", amount,"pounds straightaway.")
            lencalc (amount)
        else:
            print("Sorry, it has to be between £100 and £1000.")
    else:
        print(name,",you are making lots of money, you don't need a loan!")


def checkage():
    age = int (input ("How old are you: "))
    if age <=18:
        print (name,",you are too young to get a loan!")
    else:
        criteria1()


checkage()








        
    
