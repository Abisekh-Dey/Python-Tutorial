# class Atm:
#     def __init__(self):
#         self.__balance = 0

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ${amount}. New balance: ${self.__balance}")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         if amount > 0 and self.__balance >= amount:
#             self.__balance -= amount
#             print(f"Withdrew ${amount}. New balance: ${self.__balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

# # Example usage
# atm = Atm()
# print("Initial balance:", atm.get_balance())
# atm._Atm__balance=12
# atm.deposit(100)
# atm.withdraw(50)
# print("Final balance:", atm.get_balance())



class Atm:
    def __init__(self):
        import sys
        import os
        
        account_number = int(input("Enter The Account Number: "))
        os.system("cls")
        raccount_number = int(input("Re-enter The Account Number: "))
        
        self.__accn = account_number
        self.__raccn = raccount_number
        self.__balance = 0
        self.__default_pin = ["1234"]
        if len(self.__default_pin) == 0:
            os.system("cls")
            ch = int(input("Create PIN -> Press-1: "))
            if ch == 1:
                self.cpin()
            else:
                sys.exit()
                
        if self.__accn == 17632322013 and self.__raccn == 17632322013:
            os.system("cls")
            self.menu()
        else:
            sys.exit()
            
    def menu(self):
        import sys
        import os
        
        os.system("cls")
        print('''
            ____________________
            |                  |
            |Name : Abisekh Dey|
            |Next -> Press-1   |
            |Exit -> Press-2   |
            |__________________|
            ''')
              
        choice = int(input("Enter The Choice: "))
        os.system("cls")
        if choice == 1:
            self.__operation()
        elif choice == 2:
            sys.exit()
        else:
            print("Invalid Choice!")
            sys.exit()
            
    def __operation(self):
        import sys
        import os
        print('''
            _________________________________________________________
            |                                                       |
            | Balance Inquiry -> Press-1 | Cash Withdraw -> Press-2 |
            |                            |                          |
            |  Cash Deposit -> Press-3   |  Generate Pin -> Press-4 |
            |                            |                          |
            |                            |      Exit -> Press-0     |
            |_______________________________________________________|
            ''')
        choice = int(input("Enter The Choice: "))
        if choice == 1:
            os.system("cls")
            self.abalance()
        elif choice == 2:
            os.system("cls")
            print('''
                Withdraw From:
                ______________________
                |                    |
                |# ACCOUNT -> Press-1|
                |                    |
                |# SAVING  -> Press-2|
                |                    |
                |# CURRENT -> Press-3|
                |____________________|
                ''')
            ch = int(input("Enter The Choice: "))
            if ch == 1:
                self.withdraw()
            elif ch == 2:
                self.withdraw()
            elif ch == 3:
                self.withdraw()
            else:
                print("Please Enter Valid Number")
                ch = int(input("Previous Menu -> Press-0: "))
                if ch == 0:
                    self.__operation()
        elif choice == 3:
            os.system("cls")
            self.__deposit()
        elif choice == 4:
            os.system("cls")
            self.gpin()
        elif choice == 0:
            sys.exit()
    
    def abalance(self):
        print("Account Balance:", self.__balance)
    
    def withdraw(self):
        import os
        import sys
        os.system("cls")
        wcash = int(input("Enter The Amount: "))
        if wcash > 25000:
            os.system("cls")
            print("Maximum Withdrawal Limit is 25000 per day")
            i = 0
            while i <= 1:
                os.system("cls")
                wcash = int(input("Re-enter The Amount: "))
                i += 1
                if wcash > 25000:
                    i = i - 1
                    continue
                else:
                    break
        if wcash <= 25000:
            os.system("Cls")
            Pin = input("Enter Pin: ")
            if len(Pin) != 4 or Pin.isalpha():
                os.system("cls")
                print("PIN Should be a 4 Digit Number without any Alphabets in it!")
                sys.exit()
            elif Pin not in self.__default_pin:
                print("Wrong Pin!")
                sys.exit()
            os.system("Cls")
            r_Pin = input("Re-enter Pin: ")
            if len(r_Pin) != 4 or r_Pin.isalpha():
                os.system("cls")
                print("PIN Should be a 4 Digit Number without any Alphabets in it!")
                sys.exit()
            elif Pin != r_Pin:
                print("Wrong Pin!")
                sys.exit()
            if Pin in self.__default_pin and r_Pin in self.__default_pin:
                if self.__balance < wcash:
                    os.system("cls")
                    print("Insufficient Balance")
                    print("Do You Want to Add Money? -> Press 1                 EXIT -> Press - Any Number Except 1")
                    ch = int(input("Enter The Choice: "))
                    if ch == 1:
                        self.__deposit()
                    if ch != 1:
                        sys.exit()
                else:
                    os.system("cls")
                    self.__balance = self.__balance - wcash
                    print("Withdrawal Successful")
                    print("Do You Want to Check Balance -> Press-1")
                    ch = int(input("Enter The Choice: "))
                    if ch == 1:
                        os.system("cls")
                        print("Avaiable Balance:", self.__balance)
                        ch = int(input("Previous Menu -> Press 0: "))
                        if ch == 0:
                            self.__operation()
            else:
                print("Invalid Pin!")
                sys.exit()
    
    def __deposit(self):
        import os
        import sys
        os.system("cls")
        accn = int(input("Enter The Account number: "))
        os.system("cls")
        r_accn = int(input("Re-enter The Account number: "))
        os.system("cls")
        if accn == self.__accn and r_accn == self.__raccn:
            dcash = int(input("Enter The Amount: "))
            if dcash <= 50000:
                self.__balance = self.__balance + dcash
                print("Deposit Successful")
                print("Do You Want to Check Balance -> Press-1")
                ch = int(input("Enter The Choice: "))
                if ch == 1:
                    os.system("cls")
                    print("Avaiable Balance:", self.__balance)
                    ch = int(input("Previous Menu -> Press 0: "))
                    if ch == 0:
                        self.__operation()
                else:
                    sys.exit()
            else:
                print("Maximum Deposit Limit is 50000 per day")
                sys.exit()
        else:
            print("Wrong Account Number!")
    
    def gpin(self):
        import os
        import sys
        x = input("Enter Previous Pin: ")
        if len(x) != 4 or x.isalpha():
            os.system("cls")
            print("You have Entered Wrong PIN!")
            sys.exit()
        if x in self.__default_pin:
            self.__default_pin.clear()
        os.system("cls")
        print("Previous PIN Deleted Successfully")
        pin = input("Set 4-Digit New-Pin: ")
        if len(pin) != 4 or pin.isalpha():
            os.system("cls")
            print("PIN Should be a 4 Digit Number without any Alphabets in it!")
            sys.exit()
        os.system("cls")
        rpin = input("Re-enter New-Pin: ")
        if len(pin) != 4 or rpin.isalpha():
            os.system("cls")
            print("PIN Should be a 4 Digit Number without any Alphabets in it!")
            sys.exit()
        if pin == rpin:
            self.__default_pin.append(pin)
            print("PIN is Set Successfully")
            print("PIN is:", pin)
            ch = int(input("Previous Menu -> Press 0: "))
            if ch == 0:
                self.__operation()
        else:
            print("PINs did not match!")
            sys.exit()
            
    def cpin(self):
        import os
        import sys
        os.system("cls")
        accn = int(input("Enter The Account Number: "))
        os.system("cls")
        r_accn = int(input("Re-enter The Account Number: "))
        if accn == self.__accn and r_accn == self.__raccn:
            os.system("cls")
            pin = input("Set 4-Digit Pin: ")
            if len(pin) != 4 or pin.isalpha():
                os.system("cls")
                print("PIN Should be a 4 Digit Number without any Alphabets in it!")
                sys.exit()
            os.system("cls")
            rpin = input("Re-enter Pin: ")
            if len(rpin) != 4 or rpin.isalpha():
                os.system("cls")
                print("PIN Should be a 4 Digit Number without any Alphabets in it!")
                sys.exit()
        else:
            sys.exit()
        if pin == rpin:
            self.__default_pin.append(pin)
            os.system("cls")
            print("PIN is Set Successfully")
            print("PIN is:", pin)
            ch = int(input("Go To Menu -> Press-1: "))
            if ch == 1:
                self.menu()
            else:
                sys.exit()
        else:
            i = 0
            while i <= 1:
                os.system("cls")
                print("Your PIN and Re-entered PIN Should be Same!")
                pin = input("Set 4-Digit Pin: ")
                if len(pin) != 4 or pin.isalpha():
                    os.system("cls")
                    print("PIN Should be a 4 Digit Number without any Alphabets in it!")
                    sys.exit()
                os.system("cls")
                rpin = input("Re-enter Pin: ")
                if len(rpin) != 4 or rpin.isalpha():
                    os.system("cls")
                    print("PIN Should be a 4 Digit Number without any Alphabets in it!")
                    sys.exit()
                i += 1
                if pin != rpin:
                    i = i - 1
                    continue
                else:
                    self.__default_pin.append(pin)
                    os.system("cls")
                    print("PIN is Set Successfully")
                    print("PIN is:", pin)
                    ch = int(input("Go To Menu -> Press-1: "))
                    if ch == 1:
                        self.menu()
                    else:
                        sys.exit()


# from xyz import Atm

atm_instance = Atm()
print(id(atm_instance))