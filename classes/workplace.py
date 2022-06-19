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