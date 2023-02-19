class Asset:
    def __init__(self, name, color, cost, rent):
        self.name = name
        self.color = color
        self.cost = cost
        self.rent = rent
        self.owner = None
        
    def set_owner(user):
        self.owner = user
        print(f"New owner of {self.name} is {user.name}")
        
    def get_owner():
        return self.owner
    
