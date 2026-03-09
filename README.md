
# Big Game (Terminal Life Simulation)

Big Game is a **terminal-based life simulation game written in Python**.  
The game allows players to create accounts, manage finances, study, work, gamble, and interact with various locations in a simulated world.  
Players progress through education levels, unlock better jobs, earn money, manage hunger and time, and aim to reach the highest achievement: **becoming President**.

The project focuses on **object-oriented design, state management, and simulation systems**, demonstrating how multiple interacting systems can be coordinated inside a single program.

---

## Features

- Account creation and persistent save system using `pickle`
- Multiple interactive locations:
  - Casino
  - Bank
  - Shop
  - Workplace
  - Restaurant
  - School
  - Prison
- Financial systems including deposits, withdrawals, loans, and interest
- Gambling mechanics with probability-based outcomes
- Education progression unlocking higher-paying jobs
- Character progression system (IQ, hunger, money, education level)
- Inventory and item purchasing system
- Crime and punishment mechanics for unpaid debts
- Terminal-based interactive gameplay

---

## Tech Stack

- **Python**
- Object-Oriented Programming
- File persistence with **pickle**
- Randomized probability systems
- Terminal-based UI

---

## Project Structure

```
Big_Game/
│
├── Big_Game.py
│
├── Big Game saving system/
│   ├── player save files
│   ├── bank save files
│   ├── casino save files
│
└── Big Game saving system account names/
    ├── stored account names
```

The game stores player progress and world state using serialized save files so players can continue their game later.

---

## Game Systems

### Character System

The `Character` class manages all player attributes including:

- Money in purse
- Bank balance
- Hunger level
- IQ level
- Education level
- Items owned
- Criminal record
- Game completion time

This class acts as the **core state container** for the entire simulation.

---

### Bank System

The bank provides financial services including:

- Depositing money
- Withdrawing money
- Borrowing money with a 24-hour repayment limit
- Interest accumulation (3% per day)
- Automatic penalties and prison time for unpaid debt

---

### Casino System

Players can gamble money using probability-based rewards and penalties:

| Outcome | Probability |
|--------|-------------|
| +2x winnings | 10% |
| +1.6x winnings | 30% |
| -1.2x loss | 20% |
| -1.5x loss | 20% |
| -2x loss | 20% |

If the player cannot repay gambling losses, they may be sent to jail.

---

### School System

Education allows players to improve IQ and unlock better jobs.

Education levels:

| Level | Required IQ |
|------|-------------|
| Primary School | 10 |
| Middle School | 20 |
| High School | 40 |
| University | 80 |
| PhD | 150 |
| Einstein | 300 |
| Above | 300+ |

Studying costs money and hunger but increases IQ.

---

### Workplace System

Players can work different jobs depending on their education level.

Examples:

| Job | Pay |
|----|----|
| McDonald Worker | $10/hr |
| Basic Programmer | $16/hr |
| Teacher | $20/hr |
| Engineer | $40/hr |
| Advanced Programmer | $60/hr |
| Scientist | $100/hr |
| Universe Cosmologist | $50/hr |
| President | $1000/hr |

Better education unlocks higher-paying jobs.

---

### Shop System

Players can purchase items such as:

- Nissan Skyline R34 GTR
- Modern House
- Rolex Watch
- Clothing items

Items can later be used to repay bank debt.

---

### Restaurant System

Food restores hunger points, allowing players to continue working or studying.

---

### Prison System

If players fail to repay debts, they receive criminal records and prison time depending on the severity of the unpaid amount.

---

## Installation

1. Install Python 3

2. Clone the repository

3. Run the game

```
python Big_Game.py
```

The game runs entirely in the **terminal**.

---

## Gameplay Overview

1. Create or load a player account.
2. Travel between locations by typing commands.
3. Study to increase IQ.
4. Unlock higher-paying jobs.
5. Earn money and manage finances.
6. Avoid prison by repaying debts.
7. Progress until reaching the highest status.

---

## What I Learned

This project helped develop experience in:

- Object-oriented programming
- Designing interacting software systems
- State management in simulations
- File persistence using serialization
- Probability systems and random events
- Command-line interface design
- Managing complex game logic across multiple subsystems

---

## Possible Improvements

Future improvements could include:

- Refactoring the codebase into multiple modules
- Adding a graphical interface
- Improving the save system
- Adding additional locations and game mechanics
- Implementing automated tests
- Improving command parsing for better UX

---

## Project Summary

Big Game is a terminal-based life simulation demonstrating **complex system interactions, object-oriented design, and persistent game state management** in Python.  
Players manage time, money, education, and risk in order to progress through society and achieve the highest possible status.

---

## License

This project is open for educational and personal use.
