#Below is a shop class for updating shop information:
class Shop:
    def __init__(self, list = [["Nissan Skyline R34 GTR", 100000], ["Modern House", 1000000], ["Playboy Shirt", 1000], ["Nike Shoes", 2000], ["Rolex Watch", 10000]]):
        self.list = list
    
    def purchase(self, player, item):
        for items in self.list:
            if item == items[0]:
                player.player_money = round(float(player.player_money - items[1]), 2)
                for i in player.items:
                    if item == i[0]:
                        i[1] = int(i[1] + 1)
                        break
                    else:
                        continue
                break
            else:
                continue

    def __repr__(self):
        shop_introduction = """
Welcome, {player}! Here we have 5 items currently in stock:
""".format(player = player.name)
        for items in self.list:
            shop_introduction += items[0]
            shop_introduction += ": $"
            shop_introduction += str(items[1])
            shop_introduction += """
"""
        return shop_introduction
