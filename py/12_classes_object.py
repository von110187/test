class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old." 
    
    def have_birthday (self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}."
    
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.name)
print(person1.age)

print(person1.introduce())
print(person1.have_birthday())

print(Person.species)
print(person1.species)

print("\n")

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deopsited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_transaction_history(self):
        return self.transaction_history
    
account = BankAccount("12345", "Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print(account.get_transaction_history())