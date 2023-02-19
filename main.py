import random
from player import Player
from asset import Asset

class Monopoly:
    def __init__(self):
        self.players = []
        self.board = self.setup_board()

    def setup_board(self):
        board = []
        board.append(Asset("START", "none", 0, 0))
        board.append(Asset("Park Place", "blue", 500000, 100000))
        board.append(Asset("Chance", "none", 0, 0))
        board.append(Asset("Boardwalk", "blue", 700000, 150000))
        board.append(Asset("Income Tax", "none", 0, 200000))
        board.append(Asset("B&O Railroad", "black", 200000, 50000))
        board.append(Asset("Reading Railroad", "black", 200000, 50000))
        board.append(Asset("Water Works", "none", 300000, 75000))
        board.append(Asset("Electric Company", "none", 300000, 75000))
        board.append(Asset("Go To Jail", "none", 0, 0))
        board.append(Asset("St. James Place", "green", 400000, 75000))
        board.append(Asset("Community Chest", "none", 0, 0))
        board.append(Asset("Tennessee Avenue", "green", 350000, 50000))
        board.append(Asset("New York Avenue", "green", 400000, 75000))
        board.append(Asset("Free Parking", "none", 0, 0))
        board.append(Asset("Kentucky Avenue", "red", 300000, 50000))
        board.append(Asset("Chance", "none", 0, 0))
        board.append(Asset("Indiana Avenue", "red", 350000, 50000))
        board.append(Asset("Illinois Avenue", "red", 400000, 75000))
        board.append(Asset("Pennsylvania Railroad", "black", 200000, 50000))
        board.append(Asset("Atlantic Avenue", "yellow", 260000, 40000))
        board.append(Asset("Ventnor Avenue", "yellow", 280000, 45000))
        board.append(Asset("Water Works", "none", 300000, 75000))
        board.append(Asset("Marvin Gardens", "yellow", 300000, 50000))
        board.append(Asset("Go to Jail", "none", 0, 0))
        board.append(Asset("Pacific Avenue", "purple", 350000, 50000))
        board.append(Asset("North Carolina Avenue", "purple", 300000, 50000))
        board.append(Asset("Community Chest", "none", 0, 0))
        board.append(Asset("Pennsylvania Avenue", "purple", 450000, 100000))
        board.append(Asset("Short Line", "black", 200000, 50000))
        board.append(Asset("Chance", "none", 0, 0))
        board.append(Asset("Park Place", "blue", 500000, 100000))
        board.append(Asset("Luxury Tax", "none", 0, 200000))
        board.append(Asset("Boardwalk", "blue", 700000, 150000))
        return board
    
    def register_player(self):
        name = input("Enter player name: ")
        self.players.append(Player(name))

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, roll):
        position = player.position + roll
        if position >= len(self.board):
            position -= len(self.board)
            print(f"{player.name} passed START and received 500000!")
            player.balance += 500000
        player.position = position
        print(f"{player.name} moved to {self.board[position].name}")

    def buy_asset(self, player, asset):
        if asset.owner:
            rent = asset.get_rent()
            print(f"{player.name} pays {rent} in rent to {asset.owner.name}")
            player.pay_rent(rent, asset.owner)
        else:
            if player.balance >= asset.cost:
                player.balance -= asset.cost
                asset.owner = player
                player.assets.append(asset)
                print(f"{player.name} bought {asset.name} for {asset.cost}")
                if self.check_group_ownership(player, asset.color):
                    self.bonus = True
            else:
                print(f"{player.name} does not have enough money to buy {asset.name}")

    def check_group_ownership(self, player, color):
        group_assets = [asset for asset in player.assets if asset.color == color]
        if len(group_assets) == len(Asset.get_group_assets(color)):
            return True
        return False
    
    def player_bankrupt(self, player, creditor):
        creditor.balance += player.balance
        for asset in player.assets:
            asset.owner = creditor
            creditor.assets.append(asset)
        self.players.remove(player)
        print(f"{player.name} is bankrupt and out of the game")

    def play_game(self):
        print("Welcome to Monopoly!")
        for i in range(2):
            self.register_player()
        for player in self.players:
            player.balance = 2000000
        while len(self.players) > 1:
            for player in self.players:
                print(f"{player.name}'s turn:")
                print("Choose option:")
                print(
                    """
                    1. Roll Dice
                    2. Balance
                    """
                )
                option = input()
                if option == "1":
                    roll = self.roll_dice()
                    print(f"{player.name} rolled a {roll}")
                    self.move_player(player, roll)
                    print(player.position)
                elif option == "2":
                    print(player.balance)
                asset = self.board[player.position]
                if isinstance(asset, Asset):
                    print("Choose option:")
                    print(
                        """
                        1. Buy this field
                        2. Don't buy it
                        """
                    )
                    option = input()
                    if option == "1":
                        self.buy_asset(player, asset)
                    elif option == "2":
                        continue
                # if self.bonus:
                #     print(f"{player.name} gets a rental bonus for owning all {asset.color} assets!")
                #     self.bonus = False
                # print(f"{player.name}'s balance: {player.balance}")
                # if player.balance <= 0:
                #     self.player_bankrupt(player, self.bank)

        print(f"{self.players[0].name} wins the game!")

monopoly_game = Monopoly()
monopoly_game.play_game()