# classes
# Customer - names, email, kra, dob, gender
# BankAccount - Customer, acc_no, acc_type, balance

class Customer:
    def __init__(self, names:str, email:str, kra:str, dob:str, gender:str):
        self.names = names
        self.email = email
        self.kra = kra
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(f"Name : {self.names}, KRA PIN : {self.kra}, Gender : {self.gender}")

    #allows printing of eg print(customer1) just showing the details indicated rather than returning an objecf
    def __str__(self):
        return f"{self.names} {self.gender}"


class Account:
    def __init__(self, owner:Customer, acc_no:str, acc_type:str, balance:float):
        self.owner = owner
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("----------------")
    def __str__(self):
        return f"{self.acc_no} {self.owner.names}"

    def deposit(self, amount:float):
        self.balance += abs(amount) #abs means absolute  -- ensures one cant deposit a negative number

    def withdraw(self, amount:float):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= abs(amount)


# ---------------- TEST DATA ----------------

# Create customers
customer1 = Customer(
    "John Kamau",
    "john@gmail.com",
    "A001234567X",
    "2001-05-14",
    "Male"
)

customer2 = Customer(
    "Mary Wanjiku",
    "mary@gmail.com",
    "A009876543B",
    "2002-08-22",
    "Female"
)

customer3 = Customer(
    "Brian Otieno",
    "brian@gmail.com",
    "A005678912C",
    "2000-11-03",
    "Male"
)


# Create bank accounts
account1 = Account(customer1, "ACC1001", "Savings", 50000.00)
account2 = Account(customer2, "ACC1002", "Current", 125000.00)
account3 = Account(customer3, "ACC1003", "Savings", 15000.00)


# ---------------- TESTING ----------------

# Print customer details
customer1.print_details()

# Print account details
account1.print_details()

# Test deposit
print("Depositing 5000...")
account1.deposit(5000)
account1.print_details()

# Test withdrawal
print("Withdrawing 10000...")
account1.withdraw(10000)
account1.print_details()

# Test insufficient funds
print("Attempting to withdraw 100000...")
account1.withdraw(100000)
account1.print_details()

#below is allowed by the def __str__ functions  in the classes...it gives a readable output rather than returning the name  object as the result
print(customer1)
print(account1)