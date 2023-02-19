class Asset:
    def __init__(self, name, color, cost, rent):
        self.name = name
        self.color = color
        self.cost = cost
        self.rent = rent
        self.owner = None

    def __str__(self):
        if self.owner is None:
            return f"{self.name} is not owned and can be purchased for {self.cost}"
        else:
            return f"{self.name} is owned by {self.owner.name} and costs {self.cost} to buy"