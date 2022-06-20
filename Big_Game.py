import time

from math import floor
from classes.bank import bank
from classes.casino import Casino
from classes.character import Character
from classes.prison import Prison
from classes.restaurant import Restaurant
from classes.save_game import SaveGame
from classes.school import School
from classes.shop import Shop
from classes.workplace import Workplace
from classes.time_tracker import Time

def play_game():
    save_game = SaveGame()
    save_game.load_game()
    # Creates a default player:
    player = Character(*save_game.player_config['character'].values())
    # Creates a default timer tracker for program to use:
    time_tracker = Time(character=player)
    # Creates a default bank:
    Bank = bank(*save_game.player_config['bank'].values(), character=player)
    # Creates a default shop:
    shop = Shop(character=player)
    # Creates a default prison:
    prison = Prison()
    # Creates a default casino:
    casino = Casino(*save_game.player_config['casino'].values(), character=player, Bank=Bank, time=time_tracker)
    # Creates a default restaurant:
    restaurant = Restaurant(character=player)
    # Creates a default school:
    school = School(character=player, time=time_tracker)
    # Creates a default workplace:
    workplace = Workplace(character=player, time=time_tracker)

    # Creates a bank payback system countdown tracker:
    player.repay_countdown = player.time

    # Playing Terminal
    print("""Hello, {name}! In this vast terminal world, you can explore various locations. Here are the game instructions:
    There are multiple places: "Casino", "Bank", "Shop", "Workplace", "Restaurant", "Prison", and "School"
    You can go to any location and interact with fun events in the world by typing in the terminal the name of the place you want to go.
    Try to become president! Type in "President" to see relevant information and apply for President!
    """.format(name=player.name))

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

    # Interaction Code
    day = 0
    n = 0
    while n != 1:

        # Exit
        if answer == "Exit":
            time.sleep(1)
            n += 1

        # Character
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

        # Casino
        elif answer == "Casino":
            print(casino)
            casino_action = input("Enter 'Bet' to gamble your money. Enter 'Exit' to exit casino: ")

            if casino_action == "Bet":
                c = 0
                while c != 1:
                    bet_amount = str(input(
                        "You currently have {money}. Please enter the amount of money you want to bet: ".format(
                            money=player.player_money)))

                    # Below is for dealing with english input which can cause system shutdown when int() is used:
                    symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\",
                                   "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a",
                                   "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                                   "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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

                    # Below is for determining whether the bet is applicable:
                    if 0 < bet_amount <= player.player_money:
                        casino.bet(bet_amount)

                        time.sleep(1)
                        player.time = int(player.time + 2)
                        time_tracker.time = int(time_tracker.time + 2)
                        player.repay_countdown = int(player.repay_countdown + 2)

                        time.sleep(1)
                    elif bet_amount >= player.player_money or bet_amount <= 0:
                        print("Invalid bet entered! You currently have ${money} in your purse.".format(
                            money=player.player_money))
                    else:
                        print("Software Error")

                    d = 0
                    while d != 1:
                        exit_yes_no = input(
                            "You can exit the casino by entering 'Exit' or you can enter 'Continue' to keep betting: ")
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

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay == True:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # Bank
        elif answer == "Bank":
            time.sleep(1)

            # Bank welcome note:
            print("""
    Hello, {name}! Welcome to the bank. Here we provide the best service possible.
    Your current bank balance: ${player_bank}.
    The bank currently has: ${bank_money}.      
    """.format(name=player.name, player_bank=player.money_in_bank, bank_money=Bank.bank_money))

            # Bank Actions:
            bank_action = input("""
    Enter "Deposit" to deposit an amount of money into your bank account. We provide 3 percent interest per 24 hours.
    Enter "Withdraw" to withdraw an amount of money from your bank account.
    Enter "Borrow" to borrow an amount of money from the bank. WARNING!!! Money must be payed back under 24 hours, or you will be send to jail!
    Enter "Payback" to payback the amount of money you borrowed from the bank.
    Enter "Exit" to leave the bank.
    """)
            # Exit loop:
            a = 0
            while a != 1:

                # Deposit:
                if bank_action == "Deposit":
                    deposited_amount = str(input("Please enter the amount of money you want to deposit: "))

                    # Below is for dealing with english input which can cause system shutdown when int() is used:
                    symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\",
                                   "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a",
                                   "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                                   "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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

                    # Below is for determining whether deposit can be done
                    if deposited_amount > int(player.player_money):
                        print(
                            "Unsuccessful! It seems like there is not enough money in your purse for you to deposit. Check again! You have ${money} in your purse right now.".format(
                                money=player.player_money))
                        time.sleep(0.5)
                    elif 0 < deposited_amount <= int(player.player_money):
                        Bank.Deposit(deposited_amount)
                        print("Successful! Now you have ${money} in your bank!".format(money=player.money_in_bank))
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

                    # Below is for dealing with english input which can cause system shutdown when int() is used:
                    symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\",
                                   "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a",
                                   "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                                   "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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

                    # Below is for determining whether withdraw can be done
                    if withdrawed_amount > int(player.money_in_bank):
                        print(
                            "Unsuccessful! It seems like there is not enough money in your bank account for you to withdraw. Check again! You have ${money} in your account right now.".format(
                                money=player.money_in_bank))
                        time.sleep(0.5)
                    elif 0 < withdrawed_amount <= int(player.money_in_bank):
                        Bank.Withdraw(withdrawed_amount)
                        print("Successful! Now you have ${money} in your purse!".format(money=player.player_money))
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
                # Borrow:
                elif bank_action == "Borrow":
                    borrowed_amount = str(input("Please enter the amount of money you want to borrow: "))

                    # Below is for dealing with english input which can cause system shutdown when int() is used:
                    symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "\\",
                                   "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?", "/", "a",
                                   "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                                   "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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

                    # Below is for determining whether borrow can be done
                    if player.repay == False:
                        if player.criminal_record == "":
                            if borrowed_amount > int(Bank.bank_money):
                                print(
                                    "Unsuccessful! It seems like there is not enough money in the bank for you to borrow. Check again! There is ${money} in the bank right now.".format(
                                        money=Bank.bank_money))
                                time.sleep(0.5)
                            elif 0 < borrowed_amount <= int(Bank.bank_money):
                                Bank.Borrow(borrowed_amount)
                                print(
                                    "Successful! Now you have ${money} in your purse! You only have 24 hours to return it!".format(
                                        money=player.player_money))
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

                # Payback
                elif bank_action == "Payback":
                    payback_action = input("""
    Hello, {name}. Here we provide 2 ways of paying back the money:
    Enter "Cash" to pay with your purse.
    Enter "Item" to pay with your items.
    Enter "Exit" to exit.
    You have to payback ${money}.
    """.format(name=player.name, money=Bank.repay_amount))

                    if payback_action == "Cash":
                        amount = input("Please enter how much money you want to pay: ")

                        # Below is for dealing with english input which can cause system shutdown when int() is used:
                        symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
                                       "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?",
                                       "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                                       "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E",
                                       "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                       "V", "W", "X", "Y", "Z"]
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

                        # Below is for determining whether the amount is available:
                        if amount > player.player_money or amount > Bank.repay_amount:
                            print("Unavailable amount of money payed!")
                            time.sleep(0.5)
                        elif amount <= player.player_money and amount <= Bank.repay_amount:
                            Bank.cash_pay(amount)
                            print("Success! Now you only need to payback ${money}.".format(money=Bank.repay_amount))
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
                                Bank.item_pay(pay_item)
                                print(
                                    "Successful! Now you only need to payback ${money}".format(money=Bank.repay_amount))
                                break
                            else:
                                print("Unavailable!")
                                time.sleep(0.5)

                    elif payback_action == "Exit":
                        a += 1
                    else:
                        print("Sorry, that is not an available option, try again!")
                        time.sleep(0.5)

                # Exit
                elif bank_action == "Exit":
                    a += 1
                # Else
                else:
                    bank_action = input("It doesn't seem like you entered an available action. Try again: ")

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay == True:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # Shop
        elif answer == "Shop":
            time.sleep(1)

            # Shop welcome note:
            print(shop)

            # Below is for detecting if purchase_item is available for player:
            purchase_item = input("Please enter an item name to buy: ")
            if purchase_item == "Nissan Skyline R34 GTR":
                if float(player.player_money) >= 100000:
                    shop.purchase(purchase_item)
                    print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                     product=purchase_item))
                    time.sleep(1)
                else:
                    print("Not enough money!")
                    time.sleep(1)
            elif purchase_item == "Modern House":
                if float(player.player_money) >= 1000000:
                    shop.purchase(purchase_item)
                    print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                     product=purchase_item))
                    time.sleep(1)
                else:
                    print("Not enough money!")
                    time.sleep(1)
            elif purchase_item == "Playboy Shirt":
                if float(player.player_money) >= 1000:
                    shop.purchase(purchase_item)
                    print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                     product=purchase_item))
                    time.sleep(1)
                else:
                    print("Not enough money!")
                    time.sleep(1)
            elif purchase_item == "Nike Shoes":
                if float(player.player_money) >= 2000:
                    shop.purchase(purchase_item)
                    print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                     product=purchase_item))
                    time.sleep(1)
                else:
                    print("Not enough money!")
                    time.sleep(1)
            elif purchase_item == "Rolex Watch":
                if float(player.player_money) >= 10000:
                    shop.purchase(purchase_item)
                    print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                     product=purchase_item))
                    time.sleep(1)
                else:
                    print("Not enough money!")
                    time.sleep(1)
            else:
                print("Invalid item! You sure you typed the right thing you want to buy?")
                time.sleep(1)

            # Below is the timing system:
            player.time = int(player.time + 1)
            time_tracker.time = int(time_tracker.time + 1)
            player.repay_countdown = int(player.repay_countdown + 1)

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay == True:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # Workplace
        elif answer == "Workplace":

            print(workplace)

            g = 0
            while g != 1:
                work_action = input(
                    "Please enter 'Work' to work. Now you currently have ${money}, {hunger} hunger points, and you have graduated {grade}. Enter 'Exit' to exit. ".format(
                        grade=player.grade, money=player.player_money, hunger=player.hunger))
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
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
                                # Below is for dealing with english input which can cause system shutdown when int() is used:
                                symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
                                               "=", "+", "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">",
                                               ",", ".", "?", "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                               "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                                               "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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
                                    workplace.work(work_choice, work_hour)
                                    print("Successful!")
                                    time.sleep(1)
                                elif work_hour > maximum:
                                    workplace.work(work_choice, maximum)
                                    print(
                                        "Exceeding your working limit, automatically set to the highest time possible.")
                                    time.sleep(1)
                                else:
                                    print("software bug")
                            else:
                                print(
                                    "Sorry, but you don't fit the education requirement to do this job! Go to the 'School' and study!")
                                time.sleep(1)
                    else:
                        print("Invalid Job!")
                        time.sleep(1)

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay == True:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # Restaurant
        elif answer == "Restaurant":

            time.sleep(1)

            e = 0
            while e != 1:
                # Restaurant welcome note:
                print(restaurant)

                # Below is for detecting if purchase_item is available for player:
                print("You have currently {points} hunger points. (100 is full)".format(points=player.hunger))
                food = input("Please enter a food name to eat ('Exit' to leave): ")
                if float(player.hunger) != 100:
                    if food == "Big Mac":
                        if float(player.player_money) >= 200:
                            restaurant.purchase(food)
                            print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                             product=food))
                            time.sleep(1)
                            # Below is the timing system:
                            player.time = int(player.time + 2)
                            time_tracker.time = int(time_tracker.time + 2)
                            player.repay_countdown = int(player.repay_countdown + 2)
                        else:
                            print("Not enough money!")
                            time.sleep(1)
                    elif food == "Little Mac":
                        if float(player.player_money) >= 20:
                            restaurant.purchase(food)
                            print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                             product=food))
                            time.sleep(1)
                            # Below is the timing system:
                            player.time = int(player.time + 2)
                            time_tracker.time = int(time_tracker.time + 2)
                            player.repay_countdown = int(player.repay_countdown + 2)
                        else:
                            print("Not enough money!")
                            time.sleep(1)
                    elif food == "Chicken Nugget":
                        if float(player.player_money) >= 80:
                            restaurant.purchase(food)
                            print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                             product=food))
                            time.sleep(1)
                            # Below is the timing system:
                            player.time = int(player.time + 2)
                            time_tracker.time = int(time_tracker.time + 2)
                            player.repay_countdown = int(player.repay_countdown + 2)
                        else:
                            print("Not enough money!")
                            time.sleep(1)
                    elif food == "Golden Steak":
                        if float(player.player_money) >= 10000:
                            restaurant.purchase(food)
                            print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                             product=food))
                            time.sleep(1)
                            # Below is the timing system:
                            player.time = int(player.time + 2)
                            time_tracker.time = int(time_tracker.time + 2)
                            player.repay_countdown = int(player.repay_countdown + 2)
                        else:
                            print("Not enough money!")
                            time.sleep(1)
                    elif food == "Steak":
                        if float(player.player_money) >= 1000:
                            restaurant.purchase(food)
                            print("Success! Thank you, {name}, for buying {product}.".format(name=player.name,
                                                                                             product=food))
                            time.sleep(1)
                            # Below is the timing system:
                            player.time = int(player.time + 2)
                            time_tracker.time = int(time_tracker.time + 2)
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

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay == True:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # School
        elif answer == "School":

            print(school)

            f = 0
            while f != 1:
                school_action = input(
                    "Please enter 'Study' to study, {grade} student. Now you currently have ${money}, {iq} iq and {hunger} hunger points. Enter 'Exit' to exit. ".format(
                        grade=player.grade, money=player.player_money, iq=player.iq, hunger=player.hunger))
                if school_action == "Exit":
                    f += 1
                elif school_action == "Study":
                    # Below is for a convenient maximum algorithm
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
                        maximum = floor(min(player.player_money / 5000, player.hunger / 5)) * 10
                        print("software bug")

                    if maximum == 0:
                        print("You can't take any class right now!")
                        time.sleep(1)
                        f += 1
                    else:
                        study_hour = input("Please enter how many hours you want to study: ")
                        # Below is for dealing with english input which can cause system shutdown when int() is used:
                        symbol_list = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
                                       "\\", "|", "{", "[", "}", "]", ";", ":", "\"", "\'", "<", ">", ",", ".", "?",
                                       "/", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                                       "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E",
                                       "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                       "V", "W", "X", "Y", "Z"]
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
                            school.study(study_hour)
                            print("Successful!")
                            time.sleep(1)
                        elif study_hour > maximum:
                            school.study(maximum)
                            print("Exceeding your study limit, automatically set to the highest time possible.")
                            time.sleep(1)
                        else:
                            print("software bug")

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay == True:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # Prison
        elif answer == "Prison":
            print(prison)
            time.sleep(3)

            b = 0
            while b != 1:
                # Below is for removing criminal record:
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
    """.format(player_criminal_records=player.criminal_record))
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
                                    prison.remove_criminal_record(removing_criminal_record)
                                    print("Success! You have just removed one of your criminal records!")
                                    time.sleep(1)
                                    break
                        else:
                            t += 1
                    if t >= len(player.criminal_record) - 1:
                        print(
                            "You can't remove that criminal record! You currently have ${money} in your purse.".format(
                                money=player.player_money))
                        time.sleep(1)
                else:
                    print("Unavailable Option! Please re-enter: ")
                    time.sleep(1)

            # Bank Daily Addition and Daily Interest:
            day += floor(time_tracker.time / 24)
            if day >= 1:
                number = 1
                while number <= day:
                    Bank.Daily_Addition()
                    Bank.Daily_Interest()
                    time_tracker.time -= 24
                    number += 1
                day = 0
                number = 1
                print("The bank has just earned the daily 10%!")
                print("You have just earned your daily interest!")

            # Bank repay countdown tester:
            if int(player.repay_countdown) >= 24 and player.repay:
                print("It seems like you haven't payback the money to the bank under 24 hours.")
                Bank.bank_prison()
                time.sleep(0.5)
                print(
                    "Your money in your purse and bank account have been transfered to the bank. New criminal record has been logged into your account.")
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

        # President
        elif answer == "President":

            print("""
    In order to become president. You need to fit in the following requirements:
    You need to have at least 500 iq.
    You need to have no criminal record.
    You need to have at least $1000000 in your bank and purse total.
    You should not be in debt when applying.
    You need to have at least one of each shop items.
    """)

            apply_president = input(
                "If you are ready, type in 'Apply' to apply president and win the game, or enter 'Exit' to leave: ")

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
                        print("Congradulation {player}, you have completed the game in {hour} hours!".format(
                            hour=player.time, player=player.name))
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

        # Else
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
        save_exit = input(
            "You can enter 'Save' to save your game progress, or you can enter 'Restart' to restart everything! ")
        if save_exit == "Save":
            save_game.save_game(player, Bank, casino)
            h += 1
        elif save_exit == "Restart":
            # Saving new player informations
            save_game.fresh_load()
            h += 1
        else:
            print("Invalid Action, Try again!")


if __name__ == "__main__":
    play_game()
