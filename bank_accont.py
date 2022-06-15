class BankAccount:

    # for Ninja Bonus - Create a class variable
    accounts = []

    # constructor
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

        # for Ninja Bonus
        BankAccount.accounts.append(self)

    # increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount 
        return self
        

    # print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self # also need a return self

    # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.interest_rate)
        return self

    # for Ninja Bonus
    @classmethod
    def display_all_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()




# Create accounts
acct1 = BankAccount(0.015, 0)
acct2 = BankAccount(0.03, 1000)

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
acct1.display_account_info()    # intital info
acct1.deposit(100).deposit(200).deposit(1500).withdraw(500).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
acct2.display_account_info()    # intital info
acct2.deposit(200).deposit(3000).withdraw(150).withdraw(300).withdraw(250).withdraw(220).yield_interest().display_account_info()

# for Ninja Bonus
BankAccount.display_all_account_info()
