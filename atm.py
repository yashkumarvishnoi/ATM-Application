import time
import sys

code=3472
balance=45000

def start():
    print("=======================================================")
    print("=======================================================")
    print("Welcome To YKB Bank")
    print("Please Insert Your ATM CARD in the Machine")
    print("=======================================================")
    print("=======================================================")
    time.sleep(2)
    print("Please wait till the ATM Machine Processes the card")
    time.sleep(4)
    print("-------------------------------------------------------")
    print("Press 1: For Viewing Account Balance")
    print("Press 2: For Cash Withdrawal")
    print("Press 3: For Cash Deposit")
    print("Press 4: For Changing Account Pin")
    print("Press 5: For Exiting ATM")
    print("-------------------------------------------------------")
    time.sleep(3)
    try:
        ch=(input("Please make your Choice:-  ")) 
    except ValueError:
        print("-------------------------------------------------------")
        print("Error: Invalid input. Please enter a valid integer.") 
        print("-------------------------------------------------------")      
    choices={
        '1':check_Balance,
        '2':cash_Withdrawal,
        '3':cash_Deposit,
        '4':change_Pin,
        '5':exit_Atm
    }
    operation=choices.get(ch)
    count=3
    if(operation):
        operation(count)
    else:
        print("=======================================================")
        print("The Selected option is Invalid. Try Again!!")
        print("=======================================================")
        start()

def check_Balance(count):
    global code,balance
    try:
        print("-------------------------------------------------------")
        pin=int(input("Enter Your pin code:-  "))
        print("-------------------------------------------------------")
    except ValueError:
        print("-------------------------------------------------------")
        print("Error: Invalid input. Please enter a valid integer.")
        print("-------------------------------------------------------")
    if(count==0):
        print("=======================================================")
        print("Sorry 0 Chances left. Try Again after 24 Hours Until then Bank Authorities Have been alerted")
        print("=======================================================")
        sys.exit()
    if(pin == code):
        print("=========================================================")
        print("Please wait till the Machine fetches your details")
        time.sleep(3)
        print(f"Bank Statement:-\nAccount No- XXXXXXXXXX\nBalance Amount- {balance}")
        time.sleep(8)
        print("Thanks For Using YKB Bank")
        print("=========================================================")
    else:
        print("-------------------------------------------------------")
        print(f"Wrong Pin Entered!! try again {count-1} chances left")
        print("-------------------------------------------------------")
        count=count-1
        check_Balance(count)



def cash_Withdrawal(count):
    global code,balance
    try:
        print("-------------------------------------------------------")
        pin=int(input("Enter Your pin code:-"))
        print("-------------------------------------------------------")
    except ValueError:
        print("-------------------------------------------------------")
        print("Error: Invalid input. Please enter a valid integer.")
        print("-------------------------------------------------------")
    if(count==0):
        print("=======================================================")
        print("Sorry 0 Chances left. Try Again after 24 Hours Until then Bank Authorities Have been alerted")
        print("=======================================================")
        sys.exit()

    if(pin == code):
        print("=======================================================")
        print("Please wait till the Machine fetches your details")
        amt=int(input("Please Enter the amount you want to Withdraw"))
        if(amt<=balance):
            print("Please Wait Patiently For Cash")
            time.sleep(5)
            print("Please Collect Your Card and Wait for Cash")
            time.sleep(3)
            balance=balance-amt
            display(code,balance)
            print("Please Check Your Cash and Thanks for Using YKB Bank")
            print("=======================================================")
        else:
            print("-------------------------------------------------------")
            print("Insufficient Balance to Process Request. Try Again!!!")
            print("-------------------------------------------------------")
            start()
            
    else:
        print("-------------------------------------------------------")
        print(f"Wrong Pin Entered!! try again {count-1} chances left")
        print("-------------------------------------------------------")
        count=count-1
        cash_Withdrawal(count)
 
def cash_Deposit(count):
    global code,balance
   
    try:
        print("-------------------------------------------------------")
        pin=int(input("Enter Your pin code:-"))
        print("-------------------------------------------------------")
    except ValueError:
        print("-------------------------------------------------------")
        print("Error: Invalid input. Please enter a valid integer.")
        print("-------------------------------------------------------")
    if(count==0):
        print("=======================================================")
        print("Sorry 0 Chances left. Try Again after 24 Hours Until then Bank Authorities Have been alerted")
        print("=======================================================")
        sys.exit()
    if(pin == code):
        print("=======================================================")
        print("Please wait till the Machine fetches your details")
        amt=int(input("Please Enter the amount you want to Deposit"))
        balance=balance+amt
        display(code,balance)
        print("=======================================================")

    else:
        print("-------------------------------------------------------")
        print(f"Wrong Pin Entered!! try again {count-1} chances left")
        print("-------------------------------------------------------")
        count=count-1
        cash_Deposit(count)

def change_Pin(count):
    global code,balance

    try:
        print("-------------------------------------------------------")
        pin=int(input("Enter Your pin code:-"))
        print("-------------------------------------------------------")
    except ValueError:
        print("-------------------------------------------------------")
        print("Error: Invalid input. Please enter a valid integer.")
        print("-------------------------------------------------------")
    if(count==0):
        print("=======================================================")
        print("Sorry 0 Chances left. Try Again after 24 Hours Until then Bank Authorities Have been alerted")
        print("=======================================================")
        sys.exit()
    if(pin == code):
        print("=======================================================")
        print("Please wait till the Machine fetches your details")
        new_pin=int(input("Please Enter the new Pin you want to Set"))
        code=new_pin
        print(f"New Pin Chnaged successfully!!!")
        print("=======================================================")
        display(code,balance)
    else:
        print("-------------------------------------------------------")
        print(f"Wrong Pin Entered!! try again {count-1} chances left")
        4
        print("-------------------------------------------------------")
        count=count-1
        change_Pin(count)
    

def exit_Atm(count):
    print("=======================================================")
    print("Thanks for using the services")
    print("=======================================================")
    sys.exit()    

def display(pin,balance):
    print("=======================================================")
    print(f"Your current pin is :- {pin}\nYour current Balance Amount is :- {balance}")
    print("=======================================================")

while True:
    start()


