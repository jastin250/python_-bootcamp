# Python program to create Bankaccount 
 
class BankAccount: 

    def __init__(self): 

        self.balance=0

        print(" Welcome to our Bank  ") 

  

    def deposit(self): 

        amount=float(input("Enter amount to be Deposited: ")) 

        self.balance += amount 

        print("\n Amount Deposited:",amount) 

  

    def withdraw(self): 

        amount = float(input("Enter amount to be Withdrawn: ")) 

        if self.balance>=amount: 

            self.balance-=amount 

            print("\n Your withdrawal:", amount) 

        else: 

            print("\n Insufficient balance  ") 

  

    def display(self): 

        print("\n Net Balance=",self.balance) 

  
# Driver code 

   
# creating an object of class 

s = BankAccount() 

   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 

#To use inheritance in ecommerce concept

class Description:              
    descriptionname1 = "This is brought to you by "
  
   
class Products(Description):       
    prod1 = "andhra bank"
    
obj1 = Products()          
print(obj1.descriptionname1 +obj1.prod1)