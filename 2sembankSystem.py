#samuel angelo udtohan
#baw unsa ni
#btw bvank system ni


def acceptAccNum():
    while True:
        acc_num = input("Enter your account number: ")
        if acc_num.strip():
            return acc_num
        print("Account number is required, Please try again")
        
        
        
        
        
def acceptAmount(prompt, min_amount):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= min_amount:
                return amount
            else:
                print(f"Amount must be at least {min_amount:.2f}")
        except ValueError:
            print("Invalid Input")



def computeDepBalance(balance, deposit_amount):
    return balance + deposit_amount
    
    
    
    
    
def computeWithBalance(balance, withdraw_amount):
    return balance - withdraw_amount
    
    
    
    
    
def displayClientRecord(acc_num, name, address, balance):
    print("\nClient Bank Account")
    print(f"Name:       {name}   ")
    print(f"Address:    {address}   ")
    print(f"Balance:    {balance: .2f}\n")







def main():
    client_account = None
    client_name = None
    client_address = None
    client_balance = 0.0
    
    
    
    
    while True:
        print("\n====Bank account===")
        print("\n1. Open New Account    ")
        print("\n2. Deposit             ")
        print("\n3. Withdraw            ")
        print("\n4. Display your Record ")
        print("\n5. Exit                ")
        
        choice = input("\nPick your bet Number:   ")
        
        
        
        
        
        
        #Open new Account
        if choice == "1" :
            client_account = acceptAccNum()
            client_name = input("Enter your name:        ")
            client_address = input("Enter your address:  ")
            client_balance = acceptAmount("Enter initial deposit amount|DAPAT 500 PATAAS!!!: ", 500.00)
            print("Succesfully Opened Account")
            
            
            
            
            
            
            
            
        #Deposit
        elif choice == "2":
            if client_account is None:
                print("Huy wla pakay account, PAG GAMA SA!!!")
            else:
                deposit_amount = acceptAmount("Enter deposit amount: ", 0.0)
                client_balance = computeDepBalance(client_balance, deposit_amount)
                print("Deposit was successful New Balance {client_balance:.2f}")
            
            
            
            
            
            
            
        #Withdraw
        elif choice == "3":
            if client_account is None:
                print("Huy wla pakay account, PAG GAMA SA!!!")
            else:
                withdraw_amount = acceptAmount("Enter withdraw amount:  ", 0.0)
                if client_balance - withdraw_amount >= 500.00:
                    client_balance = computeWithBalance(client_balance, withdraw_amount)
                    print("wirhdrawal was succesfully New Balance {client_balance:.2f}")
                else:
                    print("Kulang ang imong balance")
            
            
            
            
            
            
            
        #To display Cient Record
        elif choice == "4":
            if client_account is None:
                    print("Huy wla pakay account, PAG GAMA SA!!!")
            else:
                    displayClientRecord(client_account, client_name, client_address, client_balance)
        
        
        
        
        
        
        #Exiting the program
        elif choice == "5":
            print("Thank you for using the bank system")
            break
            
            
        else:
            print("Tarungang Input Ba!!!!")


if __name__ == "__main__":
    main()


