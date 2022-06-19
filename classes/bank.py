
#Below is a bank class for updating bank informations.
from classes.shop import Shop
from classes.character import Character
from classes.time_tracker import Time


class bank:
    def __init__(self, bank_money=100000, repay_amount=0, character: Character=None, shop: Shop=None, time: Time=None):
        self.bank_money = bank_money
        self.repay_amount = repay_amount
        self.player = character
        self.shop = shop
        self.time = time
    
    def Daily_Addition(self):
        self.bank_money = round(float(self.bank_money) * 1.1, 2)
    
    def Daily_Interest(self):
        self.bank_money = round(float(self.bank_money) + float(self.player.money_in_bank) * 0.03, 2)
        self.player.money_in_bank = round(float(self.player.money_in_bank) * 1.03, 2)

    def Deposit(self, deposited_money):
        self.player.money_in_bank = round(float(self.player.money_in_bank) + float(deposited_money), 2)
        self.player.player_money = round(float(self.player.player_money - deposited_money), 2)
        self.bank_money = round(float(self.bank_money + deposited_money), 2)

    def Withdraw(self, withdrawed_money):
        self.player.money_in_bank = round(float(self.player.money_in_bank - withdrawed_money), 2)
        self.player.player_money = round(float(self.player.player_money + withdrawed_money), 2)
        self.bank_money = round(float(self.bank_money - withdrawed_money), 2)
    
    def Borrow(self, borrowed_money):
        self.bank_money = round(float(self.bank_money - borrowed_money), 2)
        self.player.player_money = round(float(self.player.player_money + borrowed_money), 2)
        self.repay_amount += round(float(borrowed_money), 2)
        self.player.repay_countdown = 0
        self.player.repay = True

    def cash_pay(self, cash_payed_money):
        self.player.player_money = round(float(self.player.player_money - cash_payed_money), 2)
        self.bank_money = round(float(self.bank_money + cash_payed_money), 2)
        self.repay_amount = round(float(self.repay_amount - cash_payed_money), 2)
        if self.repay_amount == 0:
            self.player.repay = False
            self.player.repay_countdown = 0

    def item_pay(self, items):
        for item in self.shop.list:
            if items == item[0]:
                worth = round(float(item[1] * 0.75), 2)
                self.bank_money = round(float(self.bank_money + worth), 2)
                self.repay_amount = round(float(self.repay_amount - worth), 2)
                for player_item in self.player.items:
                    if items == player_item[0]:
                        player_item[1] = player_item[1] - 1
                if self.repay_amount <= 0:
                    self.player.repay = False
                    self.player.repay_countdown = 0
                    self.repay_amount = 0
    
    def bank_prison(self):
        self.bank_money = round(float(self.bank_money + self.player.player_money), 2)
        self.player.player_money = 0
        self.player.money_in_bank = 0

        if 0 < self.repay_amount <= 100:
            self.player.time = int(self.player.time + 12)
            self.time.time = int(self.time.time + 12)
            self.player.criminal_record += "A"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False
        elif 100 < self.repay_amount <= 1000:
            self.player.time = int(self.player.time + 24)
            self.time.time = int(self.time.time + 24)
            self.player.criminal_record += "B"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False
        elif 1000 < self.repay_amount <= 5000:
            self.player.time = int(self.player.time + 36)
            self.time.time = int(self.time.time + 36)
            self.player.criminal_record += "C"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False
        elif 5000 < self.repay_amount <= 10000:
            self.player.time = int(self.player.time + 48)
            self.time.time = int(self.time.time + 48)
            self.player.criminal_record += "D"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False
        elif 10000 < self.repay_amount <= 20000:
            self.player.time = int(self.player.time + 96)
            self.time.time = int(self.time.time + 96)
            self.player.criminal_record += "E"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False
        elif 20000 < self.repay_amount <= 80000:
            self.player.time = int(self.player.time + 240)
            self.time.time = int(self.time.time + 240)
            self.player.criminal_record += "F"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False
        elif 80000 < self.repay_amount:
            self.player.time = int(self.player.time + 480)
            self.time.time = int(self.time.time + 480)
            self.player.criminal_record += "G"
            self.repay_amount = 0
            self.player.repay_countdown = 0
            self.player.repay = False

    def __repr__(self):
        return "Current the bank holds ${money} and {name} is required to pay back ${amount} of money".format(money=self.bank_money, name=self.player.name, amount=self.repay_amount)
