#Below is a restaurant class for updating restaurant information:
from classes.character import Character


class Restaurant:
    def __init__(self, food_menu=None, character: Character=None):
        if food_menu is None:
            food_menu = [["Big Mac", 200, 20], ["Little Mac", 20, 10], ["Chicken Nugget", 80, 12],
                         ["Golden Steak", 10000, 100], ["Steak", 1000, 50]]
        self.food_menu = food_menu
        self.player = character
    
    def purchase(self, food):
        for foods in self.food_menu:
            if food == foods[0]:
                self.player.player_money = round(float(self.player.player_money - foods[1]), 2)
                self.player.hunger = round(float(self.player.hunger + foods[2]), 2)
                if float(self.player.hunger) > 100:
                    self.player.hunger = 100
                break
            else:
                continue

    def __repr__(self):
        restaurant_introduction = """
Welcome, {player}! Here we have 5 food in our menu:
""".format(player=self.player.name)
        for foods in self.food_menu:
            restaurant_introduction += foods[0]
            restaurant_introduction += ": $"
            restaurant_introduction += str(foods[1])
            restaurant_introduction += ", +"
            restaurant_introduction += str(foods[2])
            restaurant_introduction += " hunger."
            restaurant_introduction += """
"""
        return restaurant_introduction
