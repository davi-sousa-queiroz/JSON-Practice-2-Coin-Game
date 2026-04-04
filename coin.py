class Coin:

    def __init__(self):
        self.coins = 0

    def coin(self):
        print("\n+1 coin")
        self.coins += 1

    def view_coins(self):
        print("\nYour coins:")
        print(self.coins)

    def menu(self):
        print("\n1. Coin")
        print("2. View coins")