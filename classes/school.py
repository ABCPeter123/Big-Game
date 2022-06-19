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