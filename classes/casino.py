#Below is a casino class for updating casino information:
class Casino:
    def __init__(self, casino_money = 100000):
        self.casino_money = casino_money
    
    def bet(self, player, bet):
        random_integer = randint(1, 100)
        if 1 <= random_integer <= 10:
            player.player_money = round(float(player.player_money + 2 * bet), 2)
            self.casino_money = round(float(self.casino_money - 2 * bet), 2)
            print("Congradulation, {player}! You have just won the +2x award!".format(player = player.name))
            if float(self.casino_money) <= 0:
                self.casino_money = 100000
        elif 11 <= random_integer <= 40:
            player.player_money = round(float(player.player_money + 1.6 * bet), 2)
            self.casino_money = round(float(self.casino_money - 1.6 * bet), 2)
            print("Congradulation, {player}! You have just won the +1.6x award!".format(player = player.name))
            if float(self.casino_money) <= 0:
                self.casino_money = 100000
        elif 41 <= random_integer <= 60:
            print("Sorry, {player}! You have just lost -1.2x.".format(player = player.name))
            if float(player.player_money) < 1.2 * bet and float(player.money_in_bank < 1.2 * bet):
                print("It doesn't seem like you have enough money in your purse and in your bank account. You will now be sent to jail.")
                player.casino_repay = round(float(1.2 * bet), 2)
                self.casino_jail(player)
            elif float(player.player_money) < 1.2 * bet and float(player.money_in_bank >= 1.2 * bet):
                player.money_in_bank = round(float(player.money_in_bank - 1.2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.2 * bet), 2)
            elif float(player.player_money) > 1.2 * bet:
                player.player_money = round(float(player.player_money - 1.2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.2 * bet), 2)
            else:
                print("Software Error")
        elif 61 <= random_integer <= 80:
            print("Sorry, {player}! You have just lost -1.5x.".format(player = player.name))
            if float(player.player_money) < 1.5 * bet and float(player.money_in_bank < 1.5 * bet):
                print("It doesn't seem like you have enough money in your purse and in your bank account. You will now be sent to jail.")
                player.casino_repay = round(float(1.5 * bet), 2)
                self.casino_jail(player)
            elif float(player.player_money) < 1.5 * bet and float(player.money_in_bank >= 1.5 * bet):
                player.money_in_bank = round(float(player.money_in_bank - 1.5 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.5 * bet), 2)
            elif float(player.player_money) > 1.5 * bet:
                player.player_money = round(float(player.player_money - 1.5 * bet), 2)
                self.casino_money = round(float(self.casino_money + 1.5 * bet), 2)
            else:
                print("Software Error")
        elif 81 <= random_integer <= 100:
            player.player_money = round(float(player.player_money - 2 * bet), 2)
            self.casino_money = round(float(self.casino_money + 2 * bet), 2)
            print("Sorry, {player}! You have just lost -2x.".format(player = player.name))
            if float(player.player_money) < 2 * bet and float(player.money_in_bank < 2 * bet):
                print("It doesn't seem like you have enough money in your purse and in your bank account. You will now be sent to jail.")
                player.casino_repay = round(float(2 * bet), 2)
                self.casino_jail(player)
            elif float(player.player_money) < 2 * bet and float(player.money_in_bank >= 2 * bet):
                player.money_in_bank = round(float(player.money_in_bank - 2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 2 * bet), 2)
            elif float(player.player_money) > 2 * bet:
                player.player_money = round(float(player.player_money - 2 * bet), 2)
                self.casino_money = round(float(self.casino_money + 2 * bet), 2)
            else:
                print("Software Error")
        else:
            print("Software Error.")

    def casino_jail(self, player):
        Bank.bank_money = round(float(Bank.bank_money + player.player_money), 2)
        player.player_money = 0
        player.money_in_bank = 0

        global Time

        if 0 < player.casino_repay <= 100:
            player.time = int(player.time + 12)
            Time = int(Time + 12)
            player.repay_countdown = int(player.repay_countdown + 12)
            player.criminal_record += "A"
            player.casino_repay = 0
        elif 100 < player.casino_repay <= 1000:
            player.time = int(player.time + 24)
            Time = int(Time + 24)
            player.repay_countdown = int(player.repay_countdown + 24)
            player.criminal_record += "B"
            player.casino_repay = 0
        elif 1000 < player.casino_repay <= 5000:
            player.time = int(player.time + 36)
            Time = int(Time + 36)
            player.repay_countdown = int(player.repay_countdown + 36)
            player.criminal_record += "C"
            player.casino_repay = 0
        elif 5000 < player.casino_repay <= 10000:
            player.time = int(player.time + 48)
            Time = int(Time + 48)
            player.repay_countdown = int(player.repay_countdown + 48)
            player.criminal_record += "D"
            player.casino_repay = 0
        elif 10000 < player.casino_repay <= 20000:
            player.time = int(player.time + 96)
            Time = int(Time + 96)
            player.repay_countdown = int(player.repay_countdown + 96)
            player.criminal_record += "E"
            player.casino_repay = 0
        elif 20000 < player.casino_repay <= 80000:
            player.time = int(player.time + 240)
            Time = int(Time + 240)
            player.repay_countdown = int(player.repay_countdown + 240)
            player.criminal_record += "F"
            player.casino_repay = 0
        elif 80000 < player.casino_repay:
            player.time = int(player.time + 480)
            Time = int(Time + 480)
            player.repay_countdown = int(player.repay_countdown + 480)
            player.criminal_record += "G"
            player.casino_repay = 0


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
""".format(player = player.name, money = self.casino_money)
        return casino_introduction