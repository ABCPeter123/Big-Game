from math import floor
import pickle
from random import randint
import time
import os

# Below is a character class for updating player informations and possibly future saving system.
class Character:
    def __init__(self, name, player_money = 0, money_in_bank = 0, time = 0, hunger = 100, iq = 0, items = [["Nissan Skyline R34 GTR", 0], ["Modern House", 0], ["Playboy Shirt", 0], ["Nike Shoes", 0], ["Rolex Watch", 0]], repay_countdown = 0, repay = False, criminal_record = "", casino_repay = 0, grade = "Primary School", completed_time = 0):
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
""".format(player = self.name, money_in_bank = self.money_in_bank, money = self.player_money, time = self.time, hunger = self.hunger, iq = self.iq)

        if self.repay == True:
            representing_sentence += "{name} need to pay back his borrowed money to the bank in {hour} hours.".format(name = self.name, hour = 24 - float(self.repay_countdown))

        if self.criminal_record != "":
            representing_sentence += """
{player} has the following criminal record:
{criminal_record}
""".format(criminal_record = self.criminal_record, player = self.name)
        else:
            representing_sentence += """
{player} has no criminal record.
""".format(player = self.name)

        representing_sentence += """
{player} is currently at {grade} grade.
""".format(player = self.name, grade = self.grade)

        representing_sentence += """
{player} currently have the following items:
""".format(player = self.name)

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
            representing_sentence += "The player has completed the game in {hour} hours.".format(hour = self.completed_time)

        return representing_sentence

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

#Below is a prison class for updating prison information:
class Prison:
    def __init__(self, remove_criminal_record_payment = [["A", 1000], ["B", 10000], ["C", 50000], ["D", 100000], ["E", 200000], ["F", 800000], ["G", 2000000]]):
        self.remove_criminal_record_payment = remove_criminal_record_payment
    
    def remove_criminal_record(self, player, criminal_record):
        for i in range(len(player.criminal_record)):
            if criminal_record == player.criminal_record[i]:
                player.criminal_record = player.criminal_record[:i] + player.criminal_record[i+1:]
                for payments in self.remove_criminal_record_payment:
                    if payments[0] == criminal_record:
                        player.player_money = round(float(player.player_money - payments[1]), 2)
                break

    def __repr__(self):
        prison_description = """
Welcome, {name}! In here, we provide the harshest treatment to any criminals! Here are the punishments:
If you overdrafted less or equal to $100, you will be in prison for 12 hours and all of your money will be transfered to the bank.
If you overdrafted more than $100 and less or equal to $1000, you will be in prison for 24 hours and all of your money will be transfered to the bank.
If you overdrafted more than $1000 and less or equal to $5000, you will be in prison for 36 hours and all of your money will be transfered to the bank.
If you overdrafted more than $5000 and less or equal to $10000, you will be in prison for 48 hours and all of your money will be transfered to the bank.
If you overdrafted more than $10000 and less or equal to $20000, you will be in prison for 96 hours and all of your money will be transfered to the bank.
If you overdrafted more than $20000 and less or equal to $80000, you will be in prison for 240 hours and all of your money will be transfered to the bank.
If you overdrafted more than $80000, you will be in prison for 480 hours and all of your money will be transfered to the bank.
""".format(name = player.name)
        return prison_description

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

#Below is a restaurant class for updating restaurant information:
class Restaurant:
    def __init__(self, food_menu = [["Big Mac", 200, 20], ["Little Mac", 20, 10], ["Chicken Nugget", 80, 12], ["Golden Steak", 10000, 100], ["Steak", 1000, 50]]):
        self.food_menu = food_menu
    
    def purchase(self, player, food):
        for foods in self.food_menu:
            if food == foods[0]:
                player.player_money = round(float(player.player_money - foods[1]), 2)
                player.hunger = round(float(player.hunger + foods[2]), 2)
                if float(player.hunger) > 100:
                    player.hunger = 100
                break
            else:
                continue

    def __repr__(self):
        restaurant_introduction = """
Welcome, {player}! Here we have 5 food in our menu:
""".format(player = player.name)
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

#Below is a school class for updating school information:
class School:
    def __init__(self, school_list = [["Primary School", 10, 1, 0.1], ["Middle School", 15, 1, 0.2], ["High School", 40, 1, 0.4], ["University", 100, 1, 0.5], ["PhD", 150, 1, 1], ["Einstein", 200, 1, 2], ["Above", 5000, 5, 10]]):
        self.school_list = school_list

    def study(self, player, hour):
        study_time = 1
        global Time
        while study_time <= hour:
            if player.grade == "Primary School":
                player.iq = round(float(player.iq + 1), 2)
                player.player_money = round(float(player.player_money - 10), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 0.1), 2)
                Time = Time + 0.1
                player.repay_countdown = player.repay_countdown + 0.1
                study_time += 0.1
            elif player.grade == "Middle School":
                player.iq = round(float(player.iq + 1), 2)
                player.player_money = round(float(player.player_money - 15), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 0.2), 2)
                Time = Time + 0.2
                player.repay_countdown = player.repay_countdown + 0.2
                study_time += 0.2
            elif player.grade == "High School":
                player.iq = round(float(player.iq + 1), 2)
                player.player_money = round(float(player.player_money - 40), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 0.4), 2)
                Time = Time + 0.4
                player.repay_countdown = player.repay_countdown + 0.4
                study_time += 0.4
            elif player.grade == "University":
                player.iq = round(float(player.iq + 1), 2)
                player.player_money = round(float(player.player_money - 100), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 0.5), 2)
                Time = Time + 0.5
                player.repay_countdown = player.repay_countdown + 0.5
                study_time += 0.5
            elif player.grade == "PhD":
                player.iq = round(float(player.iq + 1), 2)
                player.player_money = round(float(player.player_money - 150), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                study_time += 1
            elif player.grade == "Einstein":
                player.iq = round(float(player.iq + 1), 2)
                player.player_money = round(float(player.player_money - 200), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 2), 2)
                Time = Time + 2
                player.repay_countdown = player.repay_countdown + 2
                study_time += 2
            elif player.grade == "Above":
                player.iq = round(float(player.iq + 5), 2)
                player.player_money = round(float(player.player_money - 5000), 2)
                player.hunger = int(player.hunger - 5)
                player.time = round(float(player.time + 10), 2)
                Time = Time + 10
                player.repay_countdown = player.repay_countdown + 10
                study_time += 10
            else:
                print("software bug")
            
            if player.iq < 10:
                player.grade = "Primary School"
            elif 10 <= player.iq < 20:
                player.grade = "Middle School"
            elif 20 <= player.iq < 40:
                player.grade = "High School"
            elif 40 <= player.iq < 80:
                player.grade = "University"
            elif 80 <= player.iq < 150:
                player.grade = "PhD"
            elif 150 <= player.iq < 300:
                player.grade = "Einstein"
            elif 300 <= player.iq:
                player.grade = "Above"
            else:
                print("software bug")
            
            if player.iq == 10:
                print("Congradulation! You just graduated primary school! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif player.iq == 20:
                print("Congradulation! You just graduated middle school! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif player.iq == 40:
                print("Congradulation! You just graduated high school! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif player.iq == 80:
                print("Congradulation! You just graduated university! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif player.iq == 150:
                print("Congradulation! You just graduated PhD! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif player.iq == 300:
                print("Congradulation! You just graduated Einstein level! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            else:
                continue

    def __repr__(self):
        school_sentence = """
Welcome, {player}! In this school, you need to study and unlock more jobs! Here are the requirements to graduate each stage:
10 iq --> Primary School
20 iq --> Middle School
40 iq -- High School
80 iq --> University
150 iq --> PhD
300 iq --> Einstein

Here are the payments for each stage of studying: """.format(player = player.name)
        for items in self.school_list:
            school_sentence += """
{School}: ${price} per {iq} iq, {time} hours per {iq} iq, -5 hunger points per hour.""".format(School = items[0], price = items[1], iq = items[2], time = items[3])
        return school_sentence

#Below is a workplace class for updating workplace information:
class Workplace:
    def __init__(self, work_list = [["McDonald Worker", 10, -10, "Primary School"], ["Basic Programmer", 16, -12, "Middle School"], ["Teacher", 20, -12, "High School"], ["Engineer", 40 , -20, "University"], ["Advanced Programmer", 60, -20, "PhD"], ["Scientist", 100, -10, "Einstein"], ["Universe Cosmologist", 50, -1, "Above"], ["President", 1000, -1, "President"]]):
        self.worklist = work_list
    
    def work(self, player, work, hour):
        work_time = 1
        global Time
        while work_time <= hour:
            if work == "McDonald Worker":
                player.player_money = round(float(player.player_money + 10), 2)
                player.hunger = int(player.hunger - 10)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "Basic Programmer":
                player.player_money = round(float(player.player_money + 16), 2)
                player.hunger = int(player.hunger - 12)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "Teacher":
                player.player_money = round(float(player.player_money + 20), 2)
                player.hunger = int(player.hunger - 12)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "Engineer":
                player.player_money = round(float(player.player_money + 40), 2)
                player.hunger = int(player.hunger - 20)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "Advanced Programmer":
                player.player_money = round(float(player.player_money + 60), 2)
                player.hunger = int(player.hunger - 20)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "Scientist":
                player.player_money = round(float(player.player_money + 100), 2)
                player.hunger = int(player.hunger - 10)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "Universe Cosmologist":
                player.player_money = round(float(player.player_money + 50), 2)
                player.hunger = int(player.hunger - 1)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            elif work == "President":
                player.player_money = round(float(player.player_money + 1000), 2)
                player.hunger = int(player.hunger - 1)
                player.time = round(float(player.time + 1), 2)
                Time = Time + 1
                player.repay_countdown = player.repay_countdown + 1
                work_time += 1
            else:
                print("software bug")

    def __repr__(self):
        workplace_introduction = """
Welcome {player}! Here you can work to earn money! We provide several different jobs.""".format(player = player.name)
        return workplace_introduction

#Creating a new character / account
print("Welcome to the big game! You currently have the following accounts: ")
for files in os.listdir("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big Game saving system account names"):
    o = os.path.join("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big Game saving system account names", files)
    account_name = pickle.load(open(o, "rb"))
    print(account_name)

x = input("Please enter your account name: ")
filename = "D:\OneDrive Folder\OneDrive\桌面\Big Game\Big Game saving system account names\{a}_name.py".format(a = x)
true_false = os.path.exists(filename)
if true_false == True:
    print("Detected account, loading account information...")
    time.sleep(3)
    player_saved_name = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_name.py".format(name = x), "rb"))
    player_saved_player_money = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_player_money.py".format(name = x), "rb"))
    player_saved_money_in_bank = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_money_in_bank.py".format(name = x), "rb"))
    player_saved_time = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_time.py".format(name = x), "rb"))
    player_saved_hunger = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_hunger.py".format(name = x), "rb"))
    player_saved_iq = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_iq.py".format(name = x), "rb"))
    player_saved_items = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_items.py".format(name = x), "rb"))
    player_saved_repay_countdown = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay_countdown.py".format(name = x), "rb"))
    player_saved_repay = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay.py".format(name = x), "rb"))
    player_saved_criminal_record = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_criminal_record.py".format(name = x), "rb"))
    player_saved_casino_repay = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_repay.py".format(name = x), "rb"))
    player_saved_grade = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_grade.py".format(name = x), "rb"))
    player_saved_completed_time = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_completed_time.py".format(name = x), "rb"))

    #Creates a default player:
    player = Character(player_saved_name, player_saved_player_money, player_saved_money_in_bank, player_saved_time, player_saved_hunger, player_saved_iq, player_saved_items, player_saved_repay_countdown, player_saved_repay, player_saved_criminal_record, player_saved_casino_repay, player_saved_grade, player_saved_completed_time)

    bank_saved_bank_money = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_bank_money.py".format(name = x), "rb"))
    bank_saved_repay_amount = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_repay_amount.py".format(name = x), "rb"))

    #Creates a default bank:
    Bank = bank(bank_saved_bank_money, bank_saved_repay_amount)

    #Creates a default shop:
    shop = Shop()

    #Creates a default prison:
    prison = Prison()

    casino_saved_casino_money = pickle.load(open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_casino_money.py".format(name = x), "rb"))

    #Creates a default casino:
    casino = Casino(casino_saved_casino_money)

    #Creates a default restaurant:
    restaurant = Restaurant()

    #Creates a defaul school:
    school = School()

    #Creates a defaul workplace:
    workplace = Workplace()

else:
    print("Creating a new account...")
    time.sleep(3)
    pickle.dump(x, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_name.py".format(name = x), "wb"))
    pickle.dump(x, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big Game saving system account names\{name}_name.py".format(name = x), "wb"))
    #Saving player informations
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_player_money.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_money_in_bank.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_repay.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_completed_time.py".format(name = x), "wb"))
    pickle.dump("", open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_criminal_record.py".format(name = x), "wb"))
    pickle.dump("Primary School", open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_grade.py".format(name = x), "wb"))
    pickle.dump(100, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_hunger.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_iq.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_time.py".format(name = x), "wb"))
    pickle.dump(False, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay_countdown.py".format(name = x), "wb"))
    pickle.dump([["Nissan Skyline R34 GTR", 0], ["Modern House", 0], ["Playboy Shirt", 0], ["Nike Shoes", 0], ["Rolex Watch", 0]], open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_items.py".format(name = x), "wb"))

    #Saving bank information
    pickle.dump(100000, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_bank_money.py".format(name = x), "wb"))
    pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_repay_amount.py".format(name = x), "wb"))

    #Saving casino information:
    pickle.dump(100000, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_casino_money.py".format(name = x), "wb"))

    #Creates a defaul player:
    player = Character(x)

    #Creates a default bank:
    Bank = bank()

    #Creates a default shop:
    shop = Shop()

    #Creates a default prison:
    prison = Prison()

    #Creates a default casino:
    casino = Casino()

    #Creates a default restaurant:
    restaurant = Restaurant()

    #Creates a defaul school:
    school = School()

    #Creates a defaul workplace:
    workplace = Workplace()
        
#Creates a default timer tracker for program to use:
Time = player.time

#Creates a bank payback system countdown tracker:
player.repay_countdown = player.time

# Playing Terminal
print("""Hello, {name}! In this vast terminal world, you can explore various locations. Here are the game instructions:
There are multiple places: "Casino", "Bank", "Shop", "Workplace", "Restaurant", "Prison", and "School"
You can go to any location and interact with fun events in the world by typing in the terminal the name of the place you want to go.
Try to become president! Type in "President" to see relevant information and apply for President!
""".format(name = player.name))

time.sleep(3)

answer = input("""
Type in any of the following location to travel there:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"

Or type in "Character" to check your account informations:

Or type in "President" to see relevant information and apply for President:

Or type in "Exit" to leave the game:
""")

#Interaction Code
day = 0
n = 0
while n != 1:

    #Exit
    if answer == "Exit":
        time.sleep(1)
        n += 1

    #Character
    elif answer == "Character":
        print(player)
        time.sleep(3)
        exit_0 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_0
    
    #Casino
    elif answer == "Casino":
        print(casino)
        casino_action = input("Enter 'Bet' to gamble your money. Enter 'Exit' to exit casino: ")

        if casino_action == "Bet":
            c = 0
            while c != 1:
                bet_amount = str(input("You currently have {money}. Please enter the amount of money you want to bet: ".format(money = player.player_money)))

                #Below is for dealing with english input which can cause system shutdown when int() is used:
                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                record = 0
                for symbols in symbol_list:
                    detector = symbols in bet_amount
                    if detector == True:
                        record += 1
                    else:
                        continue
                    
                if record > 0:
                    bet_amount = 0
                    record = 0
                else:
                    bet_amount = int(bet_amount)
                
                #Below is for determining whether the bet is applicable:
                if 0 < bet_amount <= player.player_money:
                    casino.bet(player, bet_amount)

                    time.sleep(1)
                    player.time = int(player.time + 2)
                    Time = int(Time + 2)
                    player.repay_countdown = int(player.repay_countdown + 2)

                    time.sleep(1)
                elif bet_amount >= player.player_money or bet_amount <= 0:
                    print("Invalid bet entered! You currently have ${money} in your purse.".format(money = player.player_money))
                else:
                    print("Software Error")
                
                d = 0
                while d != 1:
                    exit_yes_no = input("You can exit the casino by entering 'Exit' or you can enter 'Continue' to keep betting: ")
                    if exit_yes_no == "Exit":
                        d += 1
                        c += 1
                        casino_action == "Exit"
                    elif exit_yes_no == "Continue":
                        d += 1
                        c = 0
                    else:
                        print("Invalid option!")
                    
        elif casino_action == "Exit":
            print("Leaving Casino, have a great day!")
            time.sleep(0.5)
        else:
            print("Invalid Option!")


        time.sleep(1)

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)

        exit_1 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_1

    #Bank
    elif answer == "Bank":
        time.sleep(1)

        #Bank welcome note:
        print("""
Hello, {name}! Welcome to the bank. Here we provide the best service possible.
Your current bank balance: ${player_bank}.
The bank currently has: ${bank_money}.      
""".format(name = player.name, player_bank = player.money_in_bank, bank_money = Bank.bank_money))

        #Bank Actions:
        bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
        #Exit loop:
        a = 0
        while a != 1:

            #Deposit:
            if bank_action == "Deposit":
                deposited_amount = str(input("Please enter the amount of money you want to deposit: "))

                #Below is for dealing with english input which can cause system shutdown when int() is used:
                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                record = 0
                for symbols in symbol_list:
                    detector = symbols in deposited_amount
                    if detector == True:
                        record += 1
                    else:
                        continue
                
                if record > 0:
                    deposited_amount = 0
                    record = 0
                else:
                    deposited_amount = int(deposited_amount)

                #Below is for determining whether deposit can be done
                if deposited_amount > int(player.player_money):
                    print("Unsuccessful! It seems like there is not enough money in your purse for you to deposit. Check again! You have ${money} in your purse right now.".format(money = player.player_money))
                    time.sleep(0.5)
                elif 0 < deposited_amount <= int(player.player_money):
                    Bank.Deposit(player, deposited_amount)
                    print("Successful! Now you have ${money} in your bank!".format(money = player.money_in_bank))
                    time.sleep(0.5)
                    bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
                else: 
                    print("You can't deposit $0 or negative number or non-number!")
                    time.sleep(0.5)
                    bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
            # Withdraw:
            elif bank_action == "Withdraw":
                withdrawed_amount = str(input("Please enter the amount of money you want to withdraw: "))

                #Below is for dealing with english input which can cause system shutdown when int() is used:
                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                record = 0
                for symbols in symbol_list:
                    detector = symbols in withdrawed_amount
                    if detector == True:
                        record += 1
                    else:
                        continue
                
                if record > 0:
                    withdrawed_amount = 0
                    record = 0
                else:
                    withdrawed_amount = int(withdrawed_amount)

                #Below is for determining whether withdraw can be done
                if withdrawed_amount > int(player.money_in_bank):
                    print("Unsuccessful! It seems like there is not enough money in your bank account for you to withdraw. Check again! You have ${money} in your account right now.".format(money = player.money_in_bank))
                    time.sleep(0.5)
                elif 0 < withdrawed_amount <= int(player.money_in_bank):
                    Bank.Withdraw(player, withdrawed_amount)
                    print("Successful! Now you have ${money} in your purse!".format(money = player.player_money))
                    time.sleep(0.5)
                    bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
                else: 
                    print("You can't withdraw $0 or negative number or non-number!")
                    time.sleep(0.5)
                    bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
            #Borrow:
            elif bank_action == "Borrow":
                borrowed_amount = str(input("Please enter the amount of money you want to borrow: "))

                #Below is for dealing with english input which can cause system shutdown when int() is used:
                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                record = 0
                for symbols in symbol_list:
                    detector = symbols in borrowed_amount
                    if detector == True:
                        record += 1
                    else:
                        continue
                
                if record > 0:
                    borrowed_amount = 0
                    record = 0
                else:
                    borrowed_amount = int(borrowed_amount)

                #Below is for determining whether borrow can be done
                if player.repay == False:
                    if player.criminal_record == "":
                        if borrowed_amount > int(Bank.bank_money):
                            print("Unsuccessful! It seems like there is not enough money in the bank for you to borrow. Check again! There is ${money} in the bank right now.".format(money = Bank.bank_money))
                            time.sleep(0.5)
                        elif 0 < borrowed_amount <= int(Bank.bank_money):
                            Bank.Borrow(player, borrowed_amount)
                            print("Successful! Now you have ${money} in your purse! You only have 24 hours to return it!".format(money = player.player_money))
                            time.sleep(1)
                            bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
                        else: 
                            print("You can't borrow $0 or negative number or non-number!")
                            time.sleep(0.5)
                            bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")            
                    else:
                        print("You can't borrow money with any criminal record!")
                        bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
                        time.sleep(1)
                else:
                    print("Please payback first before borrowing again!")
                    bank_action = input("""
Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
Enter "Withdraw" to withdraw an amount of money from your bank account.
Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
Enter "Payback" to payback the amount of money you borrowed from the bank.
Enter "Exit" to leave the bank.
""")
                    time.sleep(0.5)

            #Payback
            elif bank_action == "Payback":
                payback_action = input("""
Hello, {name}. Here we provide 2 ways of paying back the money:
Enter "Cash" to pay with your purse.
Enter "Item" to pay with your items.
Enter "Exit" to exit.
You have to payback ${money}.
""".format(name = player.name, money = Bank.repay_amount))

                if payback_action == "Cash":
                    amount = input("Please enter how much money you want to pay: ")

                    #Below is for dealing with english input which can cause system shutdown when int() is used:
                    symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    record = 0
                    for symbols in symbol_list:
                        detector = symbols in amount
                        if detector == True:
                            record += 1
                        else:
                            continue
                
                    if record > 0:
                        amount = 0
                        record = 0
                    else:
                        amount = float(amount)

                    #Below is for determining whether the amount is available:
                    if amount > player.player_money or amount > Bank.repay_amount:
                        print("Unavailable amount of money payed!")
                        time.sleep(0.5)
                    elif amount <= player.player_money and amount <= Bank.repay_amount:
                        Bank.cash_pay(player, amount)
                        print("Success! Now you only need to payback ${money}.".format(money = Bank.repay_amount))
                        time.sleep(0.5)
                    elif amount <= 0:
                        print("Unsuccessful! You can't enter something like that!")
                        time.sleep(0.5)
                    
                elif payback_action == "Item":
                    item_list = """
You currently hold:
"""      
                    for items in player.items:
                        item_list += str(items[1])
                        item_list += " "
                        item_list += str(items[0])
                        item_list += """
"""
                    print(item_list)
                    pay_item = input("Please choose an item from the list to payback: (Type the item name) ")

                    for items in player.items:
                        if pay_item == items[0] and items[1] > 0:
                            Bank.item_pay(player, pay_item)
                            print("Successful! Now you only need to payback ${money}".format(money = Bank.repay_amount))
                            break
                        else:
                            print("Unavailable!")
                            time.sleep(0.5)

                elif payback_action == "Exit":
                    a += 1
                else:
                    print("Sorry, that is not an available option, try again!")
                    time.sleep(0.5)
                
            #Exit
            elif bank_action == "Exit":
                a += 1
            #Else
            else: 
                bank_action = input("It doesn't seem like you entered an available action. Try again: ")

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)        
        
        exit_2 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_2
    
    #Shop
    elif answer == "Shop":
        time.sleep(1)

        #Shop welcome note:
        print(shop)

        #Below is for detecting if purchase_item is available for player:
        purchase_item = input("Please enter an item name to buy: ")
        if purchase_item == "Nissan Skyline R34 GTR":
            if float(player.player_money) >= 100000:
                shop.purchase(player, purchase_item)
                print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = purchase_item))
                time.sleep(1)
            else:
                print("Not enough money!")
                time.sleep(1)
        elif purchase_item == "Modern House":
            if float(player.player_money) >= 1000000:
                shop.purchase(player, purchase_item)
                print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = purchase_item))
                time.sleep(1)
            else:
                print("Not enough money!")
                time.sleep(1)
        elif purchase_item == "Playboy Shirt":
            if float(player.player_money) >= 1000:
                shop.purchase(player, purchase_item)
                print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = purchase_item))
                time.sleep(1)
            else:
                print("Not enough money!")
                time.sleep(1)
        elif purchase_item == "Nike Shoes":
            if float(player.player_money) >= 2000:
                shop.purchase(player, purchase_item)
                print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = purchase_item))
                time.sleep(1)
            else:
                print("Not enough money!")
                time.sleep(1)
        elif purchase_item == "Rolex Watch":
            if float(player.player_money) >= 10000:
                shop.purchase(player, purchase_item)
                print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = purchase_item))
                time.sleep(1)
            else:
                print("Not enough money!")
                time.sleep(1)
        else:
            print("Invalid item! You sure you typed the right thing you want to buy?")
            time.sleep(1)

        #Below is the timing system:
        player.time = int(player.time + 1)
        Time = int(Time + 1)
        player.repay_countdown = int(player.repay_countdown + 1)

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)

        exit_3 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_3
    
    #Workplace
    elif answer == "Workplace":

        print(workplace)

        g = 0
        while g != 1:
            work_action = input("Please enter 'Work' to work. Now you currently have ${money}, {hunger} hunger points, and you have graduated {grade}. Enter 'Exit' to exit. ".format(grade = player.grade, money = player.player_money, hunger = player.hunger))
            if work_action == "Exit":
                g += 1
            elif work_action == "Work":
                work_choice = input("""
Enter one of the following jobs: 
McDonald Worker: $10 per hour, -10 hunger points per hour, require 'Primary School'.
Basic Programmer: $16 per hour, -12 hunger points per hour, require 'Middle School'.
Teacher: $20 per hour, -12 hunger points per hour, require 'High School'.
Engineer: $40 per hour, -20 hunger points per hour, require 'University'.
Advanced Programmer: $60 per hour, -20 hunger points per hour, require 'PhD'.
Scientist: $100 per hour, -10 hunger points per hour, require 'Einstein'.
Universe Cosmologist: $50 per hour, -1 hunger points per hour, require 'Above'.
President: $1000 per hour, -1 hunger points per hour, require 'President'.
""")
                if work_choice == "McDonald Worker":
                    maximum = floor(player.hunger / 10)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "Primary School" or player.grade == "Middle School" or player.grade == "High School" or player.grade == "University" or player.grade == "PhD" or player.grade == "Einstein" or player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)
                
                elif work_choice == "Basic Programmer":
                    maximum = floor(player.hunger / 12)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "Middle School" or player.grade == "High School" or player.grade == "University" or player.grade == "PhD" or player.grade == "Einstein" or player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)

                elif work_choice == "Teacher":
                    maximum = floor(player.hunger / 12)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "High School" or player.grade == "University" or player.grade == "PhD" or player.grade == "Einstein" or player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)
                        
                elif work_choice == "Engineer":
                    maximum = floor(player.hunger / 20)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "University" or player.grade == "PhD" or player.grade == "Einstein" or player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)

                elif work_choice == "Advanced Programmer":
                    maximum = floor(player.hunger / 20)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "PhD" or player.grade == "Einstein" or player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)

                elif work_choice == "Scientist":
                    maximum = floor(player.hunger / 10)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "Einstein" or player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)

                elif work_choice == "Universe Cosmologist":
                    maximum = floor(player.hunger / 1)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "Above" or player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)

                elif work_choice == "President":
                    maximum = floor(player.hunger / 1)
                    if maximum == 0:
                        print("You are too hungry to work right now!")
                        time.sleep(1)
                        g += 1
                    else:
                        if player.grade == "President":
                            work_hour = input("Please enter how many hours you want to work: ")
                            #Below is for dealing with english input which can cause system shutdown when int() is used:
                            symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                            record = 0
                            for symbols in symbol_list:
                                detector = symbols in work_hour
                                if detector == True:
                                    record += 1
                                else:
                                    continue
                            
                            if record > 0:
                                work_hour = 0
                                record = 0
                            else:
                                work_hour = int(work_hour)
                            
                            if work_hour <= 0:
                                print("Invalid Working Action")
                            elif 0 < work_hour <= maximum:
                                workplace.work(player, work_choice, work_hour)
                                print("Successful!")
                                time.sleep(1)
                            elif work_hour > maximum:
                                workplace.work(player, work_choice, maximum)
                                print("Exceeding your working limit, automatically set to the highest time possible.")
                                time.sleep(1)
                            else:
                                print("software bug")
                        else:
                            print("Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                            time.sleep(1)
                else:
                    print("Invalid Job!")
                    time.sleep(1)

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)
        
        exit_4 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_4
    
    #Restaurant
    elif answer == "Restaurant":

        time.sleep(1)

        e = 0
        while e != 1:
            #Restaurant welcome note:
            print(restaurant)

            #Below is for detecting if purchase_item is available for player:
            print("You have currently {points} hunger points. (100 is full)".format(points = player.hunger))
            food = input("Please enter a food name to eat ('Exit' to leave): ")
            if float(player.hunger) != 100:
                if food == "Big Mac":
                    if float(player.player_money) >= 200:
                        restaurant.purchase(player, food)
                        print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = food))
                        time.sleep(1)
                        #Below is the timing system:
                        player.time = int(player.time + 2)
                        Time = int(Time + 2)
                        player.repay_countdown = int(player.repay_countdown + 2)
                    else:
                        print("Not enough money!")
                        time.sleep(1)
                elif food == "Little Mac":
                    if float(player.player_money) >= 20:
                        restaurant.purchase(player, food)
                        print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = food))
                        time.sleep(1)
                        #Below is the timing system:
                        player.time = int(player.time + 2)
                        Time = int(Time + 2)
                        player.repay_countdown = int(player.repay_countdown + 2)
                    else:
                        print("Not enough money!")
                        time.sleep(1)
                elif food == "Chicken Nugget":
                    if float(player.player_money) >= 80:
                        restaurant.purchase(player, food)
                        print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = food))
                        time.sleep(1)
                        #Below is the timing system:
                        player.time = int(player.time + 2)
                        Time = int(Time + 2)
                        player.repay_countdown = int(player.repay_countdown + 2)
                    else:
                        print("Not enough money!")
                        time.sleep(1)
                elif food == "Golden Steak":
                    if float(player.player_money) >= 10000:
                        restaurant.purchase(player, food)
                        print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = food))
                        time.sleep(1)
                        #Below is the timing system:
                        player.time = int(player.time + 2)
                        Time = int(Time + 2)
                        player.repay_countdown = int(player.repay_countdown + 2)
                    else:
                        print("Not enough money!")
                        time.sleep(1)
                elif food == "Steak":
                    if float(player.player_money) >= 1000:
                        restaurant.purchase(player, food)
                        print("Success! Thank you, {name}, for buying {product}.".format(name = player.name, product = food))
                        time.sleep(1)
                        #Below is the timing system:
                        player.time = int(player.time + 2)
                        Time = int(Time + 2)
                        player.repay_countdown = int(player.repay_countdown + 2)
                    else:
                        print("Not enough money!")
                        time.sleep(1)
                elif food == "Exit":
                    print("Exiting Restaurant. Have a good day!")
                    time.sleep(1)
                    e += 1
                else:
                    print("Invalid food! You sure you typed the right thing you want to buy?")
                    time.sleep(1)
            elif float(player.hunger) == 100:
                print("You are full right now!")
                time.sleep(1)
                e += 1
            else:
                print("software error")
                e += 1

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)

        exit_5 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_5
    
    #School
    elif answer == "School":

        print(school)

        f = 0
        while f != 1:
            school_action = input("Please enter 'Study' to study, {grade} student. Now you currently have ${money}, {iq} iq and {hunger} hunger points. Enter 'Exit' to exit. ".format(grade = player.grade, money = player.player_money, iq = player.iq, hunger = player.hunger))
            if school_action == "Exit":
                f += 1
            elif school_action == "Study":
                #Below is for a convenient maximum algorithm
                if player.grade == "Primary School":
                    maximum = floor(min(player.player_money / 10, player.hunger / 5)) * 0.1
                elif player.grade == "Middle School":
                    maximum = floor(min(player.player_money / 15, player.hunger / 5)) * 0.2
                elif player.grade == "High School":
                    maximum = floor(min(player.player_money / 40, player.hunger / 5)) * 0.4
                elif player.grade == "University":
                    maximum = floor(min(player.player_money / 100, player.hunger / 5)) * 0.5
                elif player.grade == "PhD":
                    maximum = floor(min(player.player_money / 150, player.hunger / 5)) * 1
                elif player.grade == "Einstein":
                    maximum = floor(min(player.player_money / 200, player.hunger / 5)) * 2
                elif player.grade == "Above":
                    maximum = floor(min(player.player_money / 5000, player.hunger / 5)) * 10
                else:
                    print("software bug")

                if maximum == 0:
                    print("You can't take any class right now!")
                    time.sleep(1)
                    f += 1
                else:
                    study_hour = input("Please enter how many hours you want to study: ")
                    #Below is for dealing with english input which can cause system shutdown when int() is used:
                    symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                    record = 0
                    for symbols in symbol_list:
                        detector = symbols in study_hour
                        if detector == True:
                            record += 1
                        else:
                            continue
                    
                    if record > 0:
                        study_hour = 0
                        record = 0
                    else:
                        study_hour = float(study_hour)
                    
                    if study_hour <= 0:
                        print("Invalid Study Action")
                    elif 0 < study_hour <= maximum:
                        school.study(player, study_hour)
                        print("Successful!")
                        time.sleep(1)
                    elif study_hour > maximum:
                        school.study(player, maximum)
                        print("Exceeding your study limit, automatically set to the highest time possible.")
                        time.sleep(1)
                    else:
                        print("software bug")

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)

        exit_6 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_6
    
    #Prison
    elif answer == "Prison":
        print(prison)
        time.sleep(3)

        b = 0
        while b != 1:
            #Below is for removing criminal record:
            removing_criminal_record = input("""
You can also remove your criminal records here. Just enter the record you want to remove (One at once).
Your current criminal record: {player_criminal_records}
Here are the prices:
"A": $1000
"B": $10000
"C": $50000
"D": $100000 
"E": $200000
"F": $800000
"G": $2000000
Enter "Exit" to exit the prison.
Or enter the criminal record you want to remove: 
""".format(player_criminal_records = player.criminal_record))
            t = 0
            if removing_criminal_record == "Exit":
                print("Exiting the prison, have a great day!")
                time.sleep(1)
                b += 1
            elif removing_criminal_record == "A" or removing_criminal_record == "B" or removing_criminal_record == "C" or removing_criminal_record == "D" or removing_criminal_record == "E" or removing_criminal_record == "F" or removing_criminal_record == "G":
                for i in range(len(player.criminal_record)):
                    if removing_criminal_record == player.criminal_record[i]:
                        for items in prison.remove_criminal_record_payment:
                            if removing_criminal_record == items[0] and player.player_money >= items[1]:
                                prison.remove_criminal_record(player, removing_criminal_record)
                                print("Success! You have just removed one of your criminal records!")
                                time.sleep(1)
                                break
                    else:
                        t += 1
                if t >= len(player.criminal_record) - 1:
                    print("You can't remove that criminal record! You currently have ${money} in your purse.".format(money = player.player_money))
                    time.sleep(1)
            else:
                print("Unavailable Option! Please re-enter: ")
                time.sleep(1)

        #Bank Daily Addition and Daily Interest:
        day += floor(Time/24)
        if day >= 1:
            number = 1
            while number <= day:
                Bank.Daily_Addition()
                Bank.Daily_Interest(player)
                Time -= 24
                number += 1
            day = 0
            number = 1
            print("The bank has just earned the daily 10%!")
            print("You have just earned your daily interest!")
        
        #Bank repay countdown tester:
        if int(player.repay_countdown) >= 24 and player.repay == True:
            print("It seems like you haven't payback the money to the bank under 24 hours.")
            Bank.bank_prison(player)
            time.sleep(0.5)
            print("Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
            time.sleep(0.5)
        

        exit_7 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_7
    
    #President
    elif answer == "President":

        print("""
In order to become president. You need to fit in the following requirements:
You need to have at least 500 iq.
You need to have no criminal record.
You need to have at least $1000000 in your bank and purse total.
You should not be in debt when applying.
You need to have at least one of each shop items.
""")

        apply_president = input("If you are ready, type in 'Apply' to apply president and win the game, or enter 'Exit' to leave: ")

        if player.grade != "President":
            if apply_president == "Apply":
                apply_counter = 0
                if player.iq >= 500:
                    apply_counter = int(apply_counter + 1)
                if player.criminal_record == "":
                    apply_counter = int(apply_counter + 1)
                if float(player.money_in_bank + player.player_money) >= 1000000:
                    apply_counter = int(apply_counter + 1)
                if player.repay == False:
                    apply_counter = int(apply_counter + 1)
                for items in player.items:
                    if items[1] >= 1:
                        apply_counter = int(apply_counter + 1)
                    else:
                        continue

                if apply_counter == 9:
                    player.grade = "President"
                    player.completed_time = player.time
                    print("Congradulation {player}, you have completed the game in {hour} hours!".format(hour = player.time, player = player.name))
                    time.sleep(1)
                else:
                    print("Sorry, your application has been rejected.")
                    time.sleep(1)
            elif apply_president == "Exit":
                time.sleep(0.5)
            else:
                print("Invalid Action")
                time.sleep(1)
        else:
            print("You are already a president!")


        exit_8 = input("""
If you want to leave, enter "Exit", if you want to check your informations, enter "Character", if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"Prison"
"President"
""")
        answer = exit_8

    #Else
    else:
        time.sleep(1)

        exit = input("""
It doesn't seem like you entered a sufficient location, try it again.
If you want to leave, enter 'Exit', if you want to travel to somewhere, please enter the following locations:
"Casino"
"Bank"
"Shop"
"Workplace"
"Restaurant"
"School"
"President"
""")
        answer = exit

h = 0
while h != 1:
    save_exit = input("You can enter 'Save' to save your game progress, or you can enter 'Restart' to restart everything! ")

    if save_exit == "Save":
        #Saving player informations
        pickle.dump(player.player_money, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_player_money.py".format(name = x), "wb"))
        pickle.dump(player.money_in_bank, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_money_in_bank.py".format(name = x), "wb"))
        pickle.dump(player.name, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_name.py".format(name = x), "wb"))
        pickle.dump(player.casino_repay, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_repay.py".format(name = x), "wb"))
        pickle.dump(player.completed_time, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_completed_time.py".format(name = x), "wb"))
        pickle.dump(player.criminal_record, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_criminal_record.py".format(name = x), "wb"))
        pickle.dump(player.grade, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_grade.py".format(name = x), "wb"))
        pickle.dump(player.hunger, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_hunger.py".format(name = x), "wb"))
        pickle.dump(player.iq, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_iq.py".format(name = x), "wb"))
        pickle.dump(player.time, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_time.py".format(name = x), "wb"))
        pickle.dump(player.repay, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay.py".format(name = x), "wb"))
        pickle.dump(player.repay_countdown, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay_countdown.py".format(name = x), "wb"))
        pickle.dump(player.items, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_items.py".format(name = x), "wb"))

        #Saving bank information
        pickle.dump(Bank.bank_money, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_bank_money.py".format(name = x), "wb"))
        pickle.dump(Bank.repay_amount, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_repay_amount.py".format(name = x), "wb"))

        #Saving casino information:
        pickle.dump(casino.casino_money, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_casino_money.py".format(name = x), "wb"))
        h += 1
    elif save_exit == "Restart":
        #Saving player informations
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_player_money.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_money_in_bank.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_repay.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_completed_time.py".format(name = x), "wb"))
        pickle.dump("", open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_criminal_record.py".format(name = x), "wb"))
        pickle.dump("Primary School", open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_grade.py".format(name = x), "wb"))
        pickle.dump(100, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_hunger.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_iq.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_time.py".format(name = x), "wb"))
        pickle.dump(False, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_repay_countdown.py".format(name = x), "wb"))
        pickle.dump([["Nissan Skyline R34 GTR", 0], ["Modern House", 0], ["Playboy Shirt", 0], ["Nike Shoes", 0], ["Rolex Watch", 0]], open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_items.py".format(name = x), "wb"))

        #Saving bank information
        pickle.dump(100000, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_bank_money.py".format(name = x), "wb"))
        pickle.dump(0, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_Bank_repay_amount.py".format(name = x), "wb"))

        #Saving casino information:
        pickle.dump(100000, open("D:\OneDrive Folder\OneDrive\桌面\Big Game\Big_Game saving system\{name}_casino_casino_money.py".format(name = x), "wb"))
        h += 1
    else:
        print("Invalid Action, Try again!")