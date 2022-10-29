class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


klaus = User("Klaus")
sara = User("Sara")
enio = User("Enio")

klaus.make_deposit(200).make_deposit(200).make_deposit(
    100).make_withdrawl(45).display_user_balance()

sara.make_deposit(500).make_deposit(500).make_withdrawl(
    50).make_withdrawl(100).display_user_balance()

enio.make_deposit(3500).make_withdrawl(100).make_withdrawl(
    200).make_withdrawl(150).display_user_balance()

sara.transfer_money(400, klaus)
