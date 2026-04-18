# 🎰 Slot Machine Game

A fun casino slot machine game available in command-line interface version!

## Features

✨ **Game Features:**
- Adjustable betting system ($1-$100 per line)
- Multiple paylines (1-3 lines)
- Symbol matching winnings system
- Real-time balance tracking
- Multiple symbol types with different payouts

🎮 ** Version:**
1. **Command-Line Version** (`main.py`) - Classic terminal-based gameplay

## Requirements

- **Python 3.6 or higher**
- **No external dependencies** (uses only built-in libraries)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/slot-machine-game.git
cd slot-machine-game
```

2. Ensure Python 3.6+ is installed:
```bash
python --version

⚠️ **This is a simulation game for entertainment purposes only.** Do not use real money. The creator is not responsible for any financial losses or issues related to gambling.

🎮 How to PlayStart the game by running the main Python script from your terminal:Bashpython main.py
Step-by-Step Gameplay:Deposit: Enter the total amount of money you want to bring to the machine. (e.g., 100).Choose Paylines: Select how many lines you wish to bet on (between 1 and 3).Note: Line 1 is the top row, Line 2 is the middle, and Line 3 is the bottom.Set Your Bet: Enter the amount you want to wager per line.Example: Betting $5 on 3 lines costs a total of $15 per spin.Spin: Press Enter to pull the lever and spin the reels!Cash Out: Type q and press Enter when prompted to quit and walk away with your remaining balance.🎲 Game Mechanics & RulesWinningTo win, you must match three identical symbols across a horizontal line that you bet on. Payouts are calculated by multiplying your bet per line by the symbol's multiplier.Symbol Multipliers (Payouts)SymbolMultiplierRarity/Frequency per ReelA5xSuper Rare (2)B4xRare (4)C3xUncommon (6)D2xCommon (8)(If you bet $10 on a line and get A | A | A, you win $50 for that line!)⚙️ CustomizationThe game is designed to be easily modifiable. Open main.py in your favorite text editor to tweak the game's core parameters located at the top of the file:Python# --- GAME SETTINGS ---
MAX_LINES = 3      # Max number of lines a user can bet on
MAX_BET = 100      # Maximum allowed bet per line
MIN_BET = 1        # Minimum allowed bet per line
ROWS = 3           # Number of rows in the slot machine
COLS = 3           # Number of columns (reels)

# --- SYMBOL CONFIGURATION ---
# Change the numbers below to make symbols more or less common
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

# Change the multipliers for winning lines
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
📁 Project StructurePlaintextslot-machine-game/
├── main.py                # The core game loop, logic, and CLI interface
├── README.md              # Project documentation
├── LICENSE                # MIT License terms
└── .gitignore             # Standard Python gitignore rules

📜 License
This project is open-source and available under the MIT License. See the LICENSE file for full details.Disclaimer: This is a simulation game created for educational and entertainment purposes only. It does not involve real money gambling.
Created as a fun Python project for learning game development concepts.

---

**Enjoy your spins! 🎰**
