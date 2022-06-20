import os
import pickle
import time


class SaveGame:
    def __init__(self):
        self.account_name = None
        self.player_config = {
            "character": {},
            "bank": {},
            "casino": {}
        }
        self.account_names_path = os.path.join(os.getcwd(), "Big Game saving system account names")
        self.path = os.path.join(os.getcwd(), "Big Game saving system")
        self.filename = None

    def load_game(self):
        # Creating a new character / account
        os.makedirs(self.account_names_path, exist_ok=True)
        os.makedirs(self.path, exist_ok=True)
        print("Welcome to the big game! You currently have the following accounts: ")
        for files in os.listdir(self.account_names_path):
            o = os.path.join(self.account_names_path, files)
            account_name = pickle.load(open(o, "rb"))
            print(account_name)

        self.account_name = input("Please enter your account name: ")
        if os.path.exists(os.path.join(self.account_names_path, f"{self.account_name}_name.py")):
            print("Detected account, loading account information...")
            time.sleep(3)
            self.player_config["character"]["player_saved_name"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_name.py"), "rb"))
            self.player_config["character"]["player_saved_player_money"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_player_money.py"), "rb"))
            self.player_config["character"]["player_saved_money_in_bank"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_money_in_bank.py"), "rb"))
            self.player_config["character"]["player_saved_time"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_time.py"), "rb"))
            self.player_config["character"]["player_saved_hunger"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_hunger.py"), "rb"))
            self.player_config["character"]["player_saved_iq"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_iq.py"), "rb"))
            self.player_config["character"]["player_saved_items"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_items.py"), "rb"))
            self.player_config["character"]["player_saved_repay_countdown"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_repay_countdown.py"), "rb"))
            self.player_config["character"]["player_saved_repay"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_repay.py"), "rb"))
            self.player_config["character"]["player_saved_criminal_record"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_criminal_record.py"), "rb"))
            self.player_config["character"]["player_saved_casino_repay"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_casino_repay.py"), "rb"))
            self.player_config["character"]["player_saved_grade"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_grade.py"), "rb"))
            self.player_config["character"]["player_saved_completed_time"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_completed_time.py"), "rb"))
            self.player_config["bank"]["bank_saved_bank_money"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_Bank_bank_money.py"), "rb"))
            self.player_config["bank"]["bank_saved_repay_amount"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_Bank_repay_amount.py"), "rb"))
            self.player_config["casino"]["casino_saved_casino_money"] = pickle.load(open(os.path.join(self.path, f"{self.account_name}_casino_casino_money.py"), "rb"))
        else:
            print("Creating a new account...")
            time.sleep(3)
            self.fresh_load()

    def save_game(self, player, Bank, casino):
        pickle.dump(player.player_money, open(os.path.join(self.path, f"{self.account_name}_player_money.py"), "wb"))
        pickle.dump(player.money_in_bank, open(os.path.join(self.path, f"{self.account_name}_money_in_bank.py"), "wb"))
        pickle.dump(player.name, open(os.path.join(self.path, f"{self.account_name}_name.py"), "wb"))
        pickle.dump(player.casino_repay, open(os.path.join(self.path, f"{self.account_name}_casino_repay.py"), "wb"))
        pickle.dump(player.completed_time, open(os.path.join(self.path, f"{self.account_name}_completed_time.py"), "wb"))
        pickle.dump(player.criminal_record, open(os.path.join(self.path, f"{self.account_name}_criminal_record.py"), "wb"))
        pickle.dump(player.grade, open(os.path.join(self.path, f"{self.account_name}_grade.py"), "wb"))
        pickle.dump(player.hunger, open(os.path.join(self.path, f"{self.account_name}_hunger.py"), "wb"))
        pickle.dump(player.iq, open(os.path.join(self.path, f"{self.account_name}_iq.py"), "wb"))
        pickle.dump(player.time, open(os.path.join(self.path, f"{self.account_name}_time.py"), "wb"))
        pickle.dump(player.repay, open(os.path.join(self.path, f"{self.account_name}_repay.py"), "wb"))
        pickle.dump(player.repay_countdown, open(os.path.join(self.path, f"{self.account_name}_repay_countdown.py"), "wb"))
        pickle.dump(player.items, open(os.path.join(self.path, f"{self.account_name}_items.py"), "wb"))
        # Saving bank information
        pickle.dump(Bank.bank_money, open(os.path.join(self.path, f"{self.account_name}_Bank_bank_money.py"), "wb"))
        pickle.dump(Bank.repay_amount, open(os.path.join(self.path, f"{self.account_name}_Bank_repay_amount.py"), "wb"))
        # Saving casino information:
        pickle.dump(casino.casino_money, open(os.path.join(self.path, f"{self.account_name}_casino_casino_money.py"), "wb"))

    def fresh_load(self):
        self.player_config = {
            "character": {},
            "bank": {},
            "casino": {}
        }
        self.player_config["character"]["player_saved_name"] = self.account_name
        pickle.dump(self.account_name, open(os.path.join(self.path, f"{self.account_name}_name.py"), "wb"))
        pickle.dump(self.account_name, open(os.path.join(self.account_names_path, f"{self.account_name}_name.py"), "wb"))
        # Saving player informations
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_player_money.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_money_in_bank.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_casino_repay.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_completed_time.py"), "wb"))
        pickle.dump("", open(os.path.join(self.path, f"{self.account_name}_criminal_record.py"), "wb"))
        pickle.dump("Primary School", open(os.path.join(self.path, f"{self.account_name}_grade.py"), "wb"))
        pickle.dump(100, open(os.path.join(self.path, f"{self.account_name}_hunger.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_iq.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_time.py"), "wb"))
        pickle.dump(False, open(os.path.join(self.path, f"{self.account_name}_repay.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_repay_countdown.py"), "wb"))
        pickle.dump([["Nissan Skyline R34 GTR", 0], ["Modern House", 0], ["Playboy Shirt", 0], ["Nike Shoes", 0],
                     ["Rolex Watch", 0]], open(os.path.join(self.path, f"{self.account_name}_items.py"), "wb"))
        # Saving bank information
        pickle.dump(100000, open(os.path.join(self.path, f"{self.account_name}_Bank_bank_money.py"), "wb"))
        pickle.dump(0, open(os.path.join(self.path, f"{self.account_name}_Bank_repay_amount.py"), "wb"))
        # Saving casino information:
        pickle.dump(100000, open(os.path.join(self.path, f"{self.account_name}_casino_casino_money.py"), "wb"))