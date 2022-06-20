# Below is a character class for updating player informations and possibly future saving system.
class Character:
    def __init__(self, name, player_money=0, money_in_bank=0, time=0, hunger=100, iq=0, items=None, repay_countdown=0, repay=False, criminal_record="", casino_repay=0, grade="Primary School", completed_time=0):
        if items is None:
            items = [["Nissan Skyline R34 GTR", 0], ["Modern House", 0], ["Playboy Shirt", 0], ["Nike Shoes", 0],
                     ["Rolex Watch", 0]]
        self.name = name
        self.money_in_bank = money_in_bank
        self.player_money = player_money
        self.time = time
        self.hunger = hunger
        self.iq = iq
        self.items = items
        self.repay_countdown = repay_countdown
        self.repay = repay
        self.criminal_record = criminal_record
        self.casino_repay = casino_repay
        self.grade = grade
        self.completed_time = completed_time

    def __repr__(self):
        representing_sentence = """
The Current Time is {time} hours.
{player} has ${money} in his purse, ${money_in_bank} in the bank account.
{player} currently has {hunger} hunger points
{player} currently has {iq} iq points
""".format(player=self.name, money_in_bank=self.money_in_bank, money=self.player_money, time=self.time,
           hunger=self.hunger, iq=self.iq)

        if self.repay:
            representing_sentence += "{name} need to pay back his borrowed money to the bank in {hour} hours.".format(
                name=self.name, hour=24 - float(self.repay_countdown))

        if self.criminal_record != "":
            representing_sentence += """
{player} has the following criminal record:
{criminal_record}
""".format(criminal_record=self.criminal_record, player=self.name)
        else:
            representing_sentence += """
{player} has no criminal record.
""".format(player=self.name)

        representing_sentence += """
{player} is currently at {grade} grade.
""".format(player=self.name, grade=self.grade)

        representing_sentence += """
{player} currently have the following items:
""".format(player=self.name)

        if self.items != []:
            for items in self.items:
                representing_sentence += " "
                representing_sentence += str(items[1])
                representing_sentence += " "
                representing_sentence += str(items[0])
                representing_sentence += ","
        else:
            representing_sentence += "None"

        if self.completed_time != 0:
            representing_sentence += "The player has completed the game in {hour} hours.".format(
                hour=self.completed_time)

        return representing_sentence
