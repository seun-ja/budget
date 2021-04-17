class NewBudget:
    def __init__(self):
        self.categories = {
            'Food': [500],
            'Clothing': [10],
            'Entertainment': [0]
        }

    def add_category(self, category):
        self.categories[category] = []

    def add_deposit(self, category):
        if category in self.categories:
            amount = int(input("How much would you like to deposit?"))
            self.categories[category].append(amount)
            return self.balance(category)
        else:
            self.add_category(category)
            amount = int(input("How much would you like to deposit?"))
            self.categories[category] = [amount]
            return self.balance(category)

    def withdraw_funds(self, category):
        amount = int(input("How much would you like to withdraw?"))
        balance = self.balance(category)
        if amount <= balance:
            return print("Here is your funds ₦%d" % amount)
        else:
            return "insufficient funds"

    def transfer_funds(self, originating_category, receiving_category):
        amount = int(input("How much would you like to transfer? "))
        balance = self.balance(originating_category)
        if amount <= balance:
            new_receiving_category_bal = amount + self.balance(receiving_category)
            new_balance = print("Here is your balance ₦%d" % new_receiving_category_bal)
            return new_balance
        else:
            return "insufficient funds"

    def balance(self, category):
        return sum(amt for amt in self.categories.get(category, []))        

nb = NewBudget()

nb.transfer_funds('Food', 'Clothing')
