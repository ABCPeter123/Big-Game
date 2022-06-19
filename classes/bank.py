
#Below is a bank class for updating bank informations.
class bank:
    def __init__(self, bank_money = 100000, repay_amount = 0):
        self.bank_money = bank_money
        self.repay_amount = repay_amount
    
    def Daily_Addition(self):
        self.bank_money = round(float(self.bank_money) * 1.1, 2)
    
    def Daily_Interest(self, player):
        self.bank_money = round(float(self.bank_money) + float(player.money_in_bank) * 0.03, 2)
        player.money_in_bank = round(float(player.money_in_bank) * 1.03, 2)

    def Deposit(self, player, deposited_money):
        player.money_in_bank = round(float(player.money_in_bank) + float(deposited_money), 2)
        player.player_money = round(float(player.player_money - deposited_money), 2)
        self.bank_money = round(float(self.bank_money + deposited_money), 2)

    def Withdraw(self, player, withdrawed_money):
        player.money_in_bank = round(float(player.money_in_bank - withdrawed_money), 2)
        player.player_money = round(float(player.player_money + withdrawed_money), 2)
        self.bank_money = round(float(self.bank_money - withdrawed_money), 2)
    
    def Borrow(self, player, borrowed_money):
        self.bank_money = round(float(self.bank_money - borrowed_money), 2)
        player.player_money = round(float(player.player_money + borrowed_money), 2)
        self.repay_amount += round(float(borrowed_money), 2)
        player.repay_countdown = 0
        player.repay = True

    def cash_pay(self, player, cash_payed_money):
        player.player_money = round(float(player.player_money - cash_payed_money), 2)
        self.bank_money = round(float(self.bank_money + cash_payed_money), 2)
        self.repay_amount = round(float(self.repay_amount - cash_payed_money), 2)
        if self.repay_amount == 0:
            player.repay = False
            player.repay_countdown = 0

    def item_pay(self, player, items):
        for item in shop.list:
            if items == item[0]:
                worth = round(float(item[1] * 0.75), 2)
                self.bank_money = round(float(self.bank_money + worth), 2)
                self.repay_amount = round(float(self.repay_amount - worth), 2)
                for player_item in player.items:
                    if items == player_item[0]:
                        player_item[1] = player_item[1] - 1
                if self.repay_amount <= 0:
                    player.repay = False
                    player.repay_countdown = 0
                    self.repay_amount = 0
    
    def bank_prison(self, player):
        self.bank_money = round(float(self.bank_money + player.player_money), 2)
        player.player_money = 0
        player.money_in_bank = 0

        global Time

        if 0 < self.repay_amount <= 100:
            player.time = int(player.time + 12)
            Time = int(Time + 12)
            player.criminal_record += "A"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False
        elif 100 < self.repay_amount <= 1000:
            player.time = int(player.time + 24)
            Time = int(Time + 24)
            player.criminal_record += "B"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False
        elif 1000 < self.repay_amount <= 5000:
            player.time = int(player.time + 36)
            Time = int(Time + 36)
            player.criminal_record += "C"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False
        elif 5000 < self.repay_amount <= 10000:
            player.time = int(player.time + 48)
            Time = int(Time + 48)
            player.criminal_record += "D"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False
        elif 10000 < self.repay_amount <= 20000:
            player.time = int(player.time + 96)
            Time = int(Time + 96)
            player.criminal_record += "E"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False
        elif 20000 < self.repay_amount <= 80000:
            player.time = int(player.time + 240)
            Time = int(Time + 240)
            player.criminal_record += "F"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False
        elif 80000 < self.repay_amount:
            player.time = int(player.time + 480)
            Time = int(Time + 480)
            player.criminal_record += "G"
            self.repay_amount = 0
            player.repay_countdown = 0
            player.repay = False

    def __repr__(self):
        return "Current the bank holds ${money} and {name} is required to pay back ${amount} of money".format(money = self.bank_money, name = player.name, amount = self.repay_amount)
