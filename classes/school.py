#Below is a school class for updating school information:
import time

from classes.time_tracker import Time
from classes.character import Character


class School:
    def __init__(self, school_list=None, character: Character=None, time: Time=None):
        if school_list is None:
            school_list = [["Primary School", 10, 1, 0.1], ["Middle School", 15, 1, 0.2], ["High School", 40, 1, 0.4],
                           ["University", 100, 1, 0.5], ["PhD", 150, 1, 1], ["Einstein", 200, 1, 2],
                           ["Above", 5000, 5, 10]]
        self.school_list = school_list
        self.player = character
        self.time = time

    def study(self, hour):
        study_time = 1
        while study_time <= hour:
            if self.player.grade == "Primary School":
                self.player.iq = round(float(self.player.iq + 1), 2)
                self.player.player_money = round(float(self.player.player_money - 10), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 0.1), 2)
                self.time.time = self.time.time + 0.1
                self.player.repay_countdown = self.player.repay_countdown + 0.1
                study_time += 0.1
            elif self.player.grade == "Middle School":
                self.player.iq = round(float(self.player.iq + 1), 2)
                self.player.player_money = round(float(self.player.player_money - 15), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 0.2), 2)
                self.time.time = self.time.time + 0.2
                self.player.repay_countdown = self.player.repay_countdown + 0.2
                study_time += 0.2
            elif self.player.grade == "High School":
                self.player.iq = round(float(self.player.iq + 1), 2)
                self.player.player_money = round(float(self.player.player_money - 40), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 0.4), 2)
                self.time.time = self.time.time + 0.4
                self.player.repay_countdown = self.player.repay_countdown + 0.4
                study_time += 0.4
            elif self.player.grade == "University":
                self.player.iq = round(float(self.player.iq + 1), 2)
                self.player.player_money = round(float(self.player.player_money - 100), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 0.5), 2)
                self.time.time = self.time.time + 0.5
                self.player.repay_countdown = self.player.repay_countdown + 0.5
                study_time += 0.5
            elif self.player.grade == "PhD":
                self.player.iq = round(float(self.player.iq + 1), 2)
                self.player.player_money = round(float(self.player.player_money - 150), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                study_time += 1
            elif self.player.grade == "Einstein":
                self.player.iq = round(float(self.player.iq + 1), 2)
                self.player.player_money = round(float(self.player.player_money - 200), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 2), 2)
                self.time.time = self.time.time + 2
                self.player.repay_countdown = self.player.repay_countdown + 2
                study_time += 2
            elif self.player.grade == "Above":
                self.player.iq = round(float(self.player.iq + 5), 2)
                self.player.player_money = round(float(self.player.player_money - 5000), 2)
                self.player.hunger = int(self.player.hunger - 5)
                self.player.time = round(float(self.player.time + 10), 2)
                self.time.time = self.time.time + 10
                self.player.repay_countdown = self.player.repay_countdown + 10
                study_time += 10
            else:
                print("software bug")
            
            if self.player.iq < 10:
                self.player.grade = "Primary School"
            elif 10 <= self.player.iq < 20:
                self.player.grade = "Middle School"
            elif 20 <= self.player.iq < 40:
                self.player.grade = "High School"
            elif 40 <= self.player.iq < 80:
                self.player.grade = "University"
            elif 80 <= self.player.iq < 150:
                self.player.grade = "PhD"
            elif 150 <= self.player.iq < 300:
                self.player.grade = "Einstein"
            elif 300 <= self.player.iq:
                self.player.grade = "Above"
            else:
                print("software bug")
            
            if self.player.iq == 10:
                print("Congradulation! You just graduated primary school! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif self.player.iq == 20:
                print("Congradulation! You just graduated middle school! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif self.player.iq == 40:
                print("Congradulation! You just graduated high school! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif self.player.iq == 80:
                print("Congradulation! You just graduated university! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif self.player.iq == 150:
                print("Congradulation! You just graduated PhD! The rest of the money is returned to your purse.")
                time.sleep(1)
                break
            elif self.player.iq == 300:
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

Here are the payments for each stage of studying: """.format(player=self.player.name)
        for items in self.school_list:
            school_sentence += """
{School}: ${price} per {iq} iq, {time} hours per {iq} iq, -5 hunger points per hour.""".format(School = items[0], price = items[1], iq = items[2], time = items[3])
        return school_sentence