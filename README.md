# 🎰 Slot Machine Game

A fun casino slot machine game available in both command-line and graphical user interface versions!

## Features

✨ **Game Features:**
- Adjustable betting system ($1-$100 per line)
- Multiple paylines (1-3 lines)
- Symbol matching winnings system
- Real-time balance tracking
- Multiple symbol types with different payouts

🎮 **Two Versions:**
1. **Command-Line Version** (`main.py`) - Classic terminal-based gameplay
2. **GUI Version** (`slot_machine_gui.py`) - Modern graphical interface with:
   - Visual slot machine display
   - Modern styling with neon color scheme
   - Spin animations
   - Real-time balance updates
   - User-friendly controls

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
```

## How to Run

### Command-Line Version
```bash
python main.py
```

### GUI Version (Recommended)
```bash
python slot_machine_gui.py
```

## Game Rules

### Starting the Game
1. Deposit an amount of money to start playing
2. Choose how many lines to bet on (1-3)
3. Choose your bet amount per line ($1-$100)
4. Hit the **SPIN** button and hope for matching symbols!

### Winning
- Match the same symbol across an entire line (left to right)
- Each matching line pays out based on the symbol value

### Symbol Values
| Symbol | Payout |
|--------|--------|
| A      | $5     |
| B      | $4     |
| C      | $3     |
| D      | $2     |

### Symbol Frequencies
- **A** - Rarest (appears 2 times)
- **B** - Uncommon (appears 4 times)
- **C** - Common (appears 6 times)
- **D** - Most common (appears 8 times)

## Example Gameplay

```
Current balance is $100
Press enter to play (q to quit).

Enter the number of lines to bet on (1-3)? 2
What would you like to bet on each line? $10
You are betting $10 on 2 lines. Total bet is equal to: $20.

B | C | D
A | A | C
D | C | A

You won $40.
You won on lines: 2
Current balance is $120
```

## Tips & Strategy

💡 **General Tips:**
- Start with small bets to understand the game mechanics
- The higher the symbol value, the harder it is to match
- Betting on more lines increases your chances but costs more per spin
- The game uses a fixed RTP (Return to Player) system - house advantage exists

⚠️ **Remember:**
- This is a game of chance, not skill
- Set a budget and stick to it
- Play for entertainment, not as a way to make money

## File Structure

```
slot-machine-game/
├── main.py                 # Command-line version
├── slot_machine_gui.py     # GUI version
├── README.md              # This file
├── LICENSE                # MIT License
├── .gitignore             # Git ignore file
└── requirements.txt       # Python dependencies (none)
```

## Customization

Want to customize the game? Here's what you can easily modify:

**In `main.py` or `slot_machine_gui.py`:**

```python
# Change betting limits
MAX_BET = 100      # Maximum bet per line
MIN_BET = 1        # Minimum bet per line
MAX_LINES = 3      # Maximum number of lines

# Change symbol values (payouts)
SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Change symbol frequencies
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
```

## Version Comparison

| Feature | CLI | GUI |
|---------|-----|-----|
| Gameplay | ✅ | ✅ |
| Text-based | ✅ | ❌ |
| Graphical Display | ❌ | ✅ |
| Visual Feedback | ❌ | ✅ |
| Animations | ❌ | ✅ |
| Ease of Use | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## Potential Enhancements

Future versions could include:
- [ ] Sound effects
- [ ] Progressive jackpot
- [ ] Leaderboard system
- [ ] Game statistics tracking
- [ ] Wild cards and bonus symbols
- [ ] Web version (Flask/Django)
- [ ] Mobile app version

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## Disclaimer

⚠️ **This is a simulation game for entertainment purposes only.** Do not use real money. The creator is not responsible for any financial losses or issues related to gambling.

## Author

Created as a fun Python project for learning game development concepts.

---

**Enjoy your spins! 🎰**
