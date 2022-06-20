#Below is a workplace class for updating workplace information:
from classes.character import Character
from classes.time_tracker import Time

class Workplace:
    def __init__(self, work_list=None, character: Character=None, time: Time=None):
        if work_list is None:
            work_list = [["McDonald Worker", 10, -10, "Primary School"], ["Basic Programmer", 16, -12, "Middle School"],
                         ["Teacher", 20, -12, "High School"], ["Engineer", 40, -20, "University"],
                         ["Advanced Programmer", 60, -20, "PhD"], ["Scientist", 100, -10, "Einstein"],
                         ["Universe Cosmologist", 50, -1, "Above"], ["President", 1000, -1, "President"]]
        self.worklist = work_list
        self.player = character
        self.time = time
    
    def work(self, work, hour):
        work_time = 1
        while work_time <= hour:
            if work == "McDonald Worker":
                self.player.player_money = round(float(self.player.player_money + 10), 2)
                self.player.hunger = int(self.player.hunger - 10)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "Basic Programmer":
                self.player.player_money = round(float(self.player.player_money + 16), 2)
                self.player.hunger = int(self.player.hunger - 12)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "Teacher":
                self.player.player_money = round(float(self.player.player_money + 20), 2)
                self.player.hunger = int(self.player.hunger - 12)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "Engineer":
                self.player.player_money = round(float(self.player.player_money + 40), 2)
                self.player.hunger = int(self.player.hunger - 20)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "Advanced Programmer":
                self.player.player_money = round(float(self.player.player_money + 60), 2)
                self.player.hunger = int(self.player.hunger - 20)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "Scientist":
                self.player.player_money = round(float(self.player.player_money + 100), 2)
                self.player.hunger = int(self.player.hunger - 10)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "Universe Cosmologist":
                self.player.player_money = round(float(self.player.player_money + 50), 2)
                self.player.hunger = int(self.player.hunger - 1)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            elif work == "President":
                self.player.player_money = round(float(self.player.player_money + 1000), 2)
                self.player.hunger = int(self.player.hunger - 1)
                self.player.time = round(float(self.player.time + 1), 2)
                self.time.time = self.time.time + 1
                self.player.repay_countdown = self.player.repay_countdown + 1
                work_time += 1
            else:
                print("software bug")

    def __repr__(self):
        workplace_introduction = """
Welcome {player}! Here you can work to earn money! We provide several different jobs.""".format(player=self.player.name)
        return workplace_introduction