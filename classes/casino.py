#Below is a casino class for updating casino information:
from random import randint


from classes.character import Character
from classes.bank import bank
from classes.time_tracker import Time


class Casino:
    def __init__(self, casino_money=100000, character: Character = None, Bank: bank = None, time: Time=None):
        self.Bank = None
        self.casino_money = casino_money
        self.player = character
        self.Bank = Bank
        self.time = time
    
    def bet(self, bet):
        random_integer = randint(1, 100)
        if 1 <= random_integer <= 10:
            self.player.player_money = round(float(self.player.player_money + 2 * bet), 2)
            self.casino_money = round(float(self.casino_money - 2 * bet), 2)
            print("Congradulation, {player}! You have just won the +2x award!".format(player=self.player.name))
            if float(self.casino_money) <= 0:
                self.casino_money = 100000
        elif 11 <= random_integer <= 40:
            self.player.player_money = round(float(self.player.player_money + 1.6 * bet), 2)
            self.casino_money = round(float(self.casino_money - 1.6 * bet), 2)
            print("Congradulation, {player}! You have just won the +1.6x award!".format(player=self.player.name))
            if float(self.casino_money) <= 0:
                self.casino_money = 100000
        elif 41 <= random_integer <= 60:
            print("Sorry, {player}! You have just lost -1.2x.".format(player=self.player.name))
            if float(self.player.player_money) < 1.2 * bet and float(self.player.money_in_bank < 1.2 * bet):
                print("It doesn't seem like you have enough money in your purse and in your bank account. You will now be sent to jail.")
                self.player.casino_repay = round(float(1.2 * bet), 2)
                self.casino_jail()
            elif float(self.player.player_money) < 1.2 * bet and float(self.player.money_in_bank >= 1.2 * bet):
                self.player.money_in_bank = round(float(self.player.money_in_bank - 1.2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.2 * bet), 2)
            elif float(self.player.player_money) > 1.2 * bet:
                self.player.player_money = round(float(self.player.player_money - 1.2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.2 * bet), 2)
            else:
                print("Software Error")
        elif 61 <= random_integer <= 80:
            print("Sorry, {player}! You have just lost -1.5x.".format(player=self.player.name))
            if float(self.player.player_money) < 1.5 * bet and float(self.player.money_in_bank < 1.5 * bet):
                print("It doesn't seem like you have enough money in your purse and in your bank account. You will now be sent to jail.")
                self.player.casino_repay = round(float(1.5 * bet), 2)
                self.casino_jail()
            elif float(self.player.player_money) < 1.5 * bet and float(self.player.money_in_bank >= 1.5 * bet):
                self.player.money_in_bank = round(float(self.player.money_in_bank - 1.5 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.5 * bet), 2)
            elif float(self.player.player_money) > 1.5 * bet:
                self.player.player_money = round(float(self.player.player_money - 1.5 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.5 * bet), 2)
            else:
                print("Software Error")
        elif 81 <= random_integer <= 100:
            self.player.player_money = round(float(self.player.player_money - 2 * bet), 2)
            self.casino_money = round(float(self.casino_money + 2 * bet), 2)
            print("Sorry, {player}! You have just lost -2x.".format(player=self.player.name))
            if float(self.player.player_money) < 2 * bet and float(self.player.money_in_bank < 2 * bet):
                print("It doesn't seem like you have enough money in your purse and in your bank account. You will now be sent to jail.")
                self.player.casino_repay = round(float(2 * bet), 2)
                self.casino_jail()
            elif float(self.player.player_money) < 2 * bet and float(self.player.money_in_bank >= 2 * bet):
                self.player.money_in_bank = round(float(self.player.money_in_bank - 2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 2 * bet), 2)
            elif float(self.player.player_money) > 2 * bet:
                self.player.player_money = round(float(self.player.player_money - 2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 2 * bet), 2)
            else:
                print("Software Error")
        else:
            print("Software Error.")

    def casino_jail(self):
        self.Bank.bank_money = round(float(self.Bank.bank_money + self.player.player_money), 2)
        self.player.player_money = 0
        self.player.money_in_bank = 0

        if 0 < self.player.casino_repay <= 100:
            self.player.time = int(self.player.time + 12)
            self.time.time = int(self.time.time + 12)
            self.player.repay_countdown = int(self.player.repay_countdown + 12)
            self.player.criminal_record += "A"
            self.player.casino_repay = 0
        elif 100 < self.player.casino_repay <= 1000:
            self.player.time = int(self.player.time + 24)
            self.time.time = int(self.time.time + 24)
            self.player.repay_countdown = int(self.player.repay_countdown + 24)
            self.player.criminal_record += "B"
            self.player.casino_repay = 0
        elif 1000 < self.player.casino_repay <= 5000:
            self.player.time = int(self.player.time + 36)
            self.time.time = int(self.time.time + 36)
            self.player.repay_countdown = int(player.repay_countdown + 36)
            self.player.criminal_record += "C"
            self.player.casino_repay = 0
        elif 5000 < self.player.casino_repay <= 10000:
            self.player.time = int(self.player.time + 48)
            self.time.time = int(self.time.time + 48)
            self.player.repay_countdown = int(self.player.repay_countdown + 48)
            self.player.criminal_record += "D"
            self.player.casino_repay = 0
        elif 10000 < self.player.casino_repay <= 20000:
            self.player.time = int(self.player.time + 96)
            self.time.time = int(self.time.time + 96)
            self.player.repay_countdown = int(self.player.repay_countdown + 96)
            self.player.criminal_record += "E"
            self.player.casino_repay = 0
        elif 20000 < self.player.casino_repay <= 80000:
            self.player.time = int(self.player.time + 240)
            self.time.time = int(self.time.time + 240)
            self.player.repay_countdown = int(self.player.repay_countdown + 240)
            self.player.criminal_record += "F"
            self.player.casino_repay = 0
        elif 80000 < self.player.casino_repay:
            self.player.time = int(self.player.time + 480)
            self.time.time = int(self.time.time + 480)
            self.player.repay_countdown = int(self.player.repay_countdown + 480)
            self.player.criminal_record += "G"
            self.player.casino_repay = 0

    def __repr__(self):
        casino_introduction = """
Welcome, {player}! In the casino, we provide the best gambling service! You can enter any amount of money you want to bet.
In the gambling, you can win/lose the following ratios:
+2x --> 10%
+1.6x --> 30%
-1.2x --> 20%
-1.5x --> 20%
-2x --> 20%
Currently the casino has ${money}.
""".format(player=self.player.name, money=self.casino_money)
        return casino_introduction