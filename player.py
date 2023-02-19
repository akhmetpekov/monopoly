class Player:
    def __init__(self, name, ):
        self.name = name
        self.position = 0
        self.balance = 2000000000
        self.assets = []
        self.is_prisoner = False
        
    def move(steps):
        if self.is_prisoner:
            print(f"User {self.name} is in the prison and skips this move")
            return
        
        self.position += steps
        if self.position >= 40:
            self.balance += 500000
            
        self.position %= 40
        
    def buy_asset(asset):
        if self.balance >= asset.cost:
            self.assets.append(asset)
            asset.set_owner(self)
            return
        
        print(f"You have not enough money to buy {asset.name}")
        return