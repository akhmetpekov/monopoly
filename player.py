import random

class Player:
    def __init__(self, name, balance=2000000, position=0):
        self.name = name
        self.balance = balance
        self.position = position
        self.assets = []

    def __str__(self):
        return f"{self.name} has a balance of {self.balance} and is at position {self.position}"
    
    def roll_dice(self):
        return random.randint(1, 6)
    
    def move(self, steps):
        self.position = (self.position + steps) % 40
        if self.position == 0:
            self.balance += 5000000
            print("You passed the start position and received 5000000 tenge")

    def buy_asset(self, asset):
        if asset.owner in None:
            if self.balance >= asset.cost:
                self.balance -= asset.cost
                self.assets.append(asset)
                asset.owner = self
                print(f"You bought {asset.name} for {asset.cost}")
            else:
                print(f"You don't have enough money to buy {asset.name}")
        else:
            self.pay_rent(asset)

    def pay_rent(self, asset):
        rent = asset.rent
        if asset.color in self.get_owned_colors():
            rent*=3
        if self.balance >= rent:
            self.balance -= rent
            asset.owner.balance += rent
            print(f"You paid {rent} in rent to {asset.owner.name} for {asset.name}")
        else:
            print(f"You don't have enough money to pay rent for {asset.name}")
            self.bankrupt(asset.owner)

    def get_owned_colors(self):
        colors = set()
        for asset in self.assets:
            colors.add(asset.color)
        return colors
    
    def bankrupt(self, creditor):
        creditor.balance += self.balance
        for asset in self.assets:
            asset.owner = creditor
            creditor.assets.append(asset)
        self.assets.clear()
        print(f"{self.name} went bankrupt and all assets were transferred to {creditor.name}")