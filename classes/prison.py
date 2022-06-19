#Below is a prison class for updating prison information:
from classes.character import Character


class Prison:
    def __init__(self, remove_criminal_record_payment=None, character: Character=None):
        if remove_criminal_record_payment is None:
            remove_criminal_record_payment = [["A", 1000], ["B", 10000], ["C", 50000], ["D", 100000], ["E", 200000],
                                              ["F", 800000], ["G", 2000000]]
        self.player = character
        self.remove_criminal_record_payment = remove_criminal_record_payment
    
    def remove_criminal_record(self, criminal_record):
        for i in range(len(self.player.criminal_record)):
            if criminal_record == self.player.criminal_record[i]:
                self.player.criminal_record = self.player.criminal_record[:i] + self.player.criminal_record[i+1:]
                for payments in self.remove_criminal_record_payment:
                    if payments[0] == criminal_record:
                        self.player.player_money = round(float(int(self.player.player_money) - payments[1]), 2)
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
""".format(name=self.player.name)
        return prison_description
