import random

database = {
   'seyi': ['Seyi','Bob','seyi@seyi.com','passwordSeyi', 0, 3446666777]
}

def init():
    print("Welcome to bankPHP")
    print("What would you like to do?")
    
    task = int(input("\nDo you have account with us: 1 (yes) 2 (no) \n1. Login \n2. Register \n"))

    if task == 1:
        login()
    elif task == 2:
        register()
    else:
        print("You have selected invalid option")
        init()

def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    user_name = input("Create a username")
    password = input("create a password \n")
    balance = 0

    account_number = generate_account_number()

    database[user_name] = [first_name, last_name, email, password, balance, account_number]

    login()

def login():
    username = input("What is your username? \n")
    password = input("Your password? \n")

    if(username in database and password == database[username][3]):
        bankOperations()           
    else:
        print('Login failed, username or password incorrect')
        login()

def bankOperations():
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        withdraw_operation(2222222)
                
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        deposit_operation()
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        complaint()

    elif(selectedOption == 4):
        logout()   
    else:
        print('Invalid Option selected, please try again')

def generate_account_number():
    new_number = random.randint(999999999, 10000000000)
    print("Your Account number is: %d" % new_number)

    return new_number

def complaint():
    print("got it")

def set_current_balance(account):
    balance = database[account][4]
    return balance

def deposit_operation(amount, account):
    print("deposit")

def withdraw_operation(account):
    print("withdraw")

def logout():
    print("loging out")

init()
