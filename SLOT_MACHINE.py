import tkinter as tk
from tkinter import messagebox
import random

# Constants
SYMBOL_COUNT = {"A": 2, "B": 4, "C": 6, "D": 8}
SYMBOL_VALUE = {"A": 5, "B": 4, "C": 3, "D": 2}

class SlotGame:
    def __init__(self, root):
        self.root = root
        self.root.title("SLOT MACHINE")
        self.root.geometry("600x500")  # Reduced size for better visibility
        self.root.resizable(False, False)
        self.root.configure(bg="#0a0e27")
        
        self.balance = 0
        self.spinning = False
        
        self.show_deposit()
    
    def show_deposit(self):
        """Deposit screen"""
        self.clear_all()
        
        f = tk.Frame(self.root, bg="#0a0e27")
        f.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)
        
        tk.Label(f, text="SLOT MACHINE", font=("Arial", 50, "bold"),
                bg="#0a0e27", fg="#00d4ff").pack(pady=40)
        
        tk.Label(f, text="Enter deposit ($):", font=("Arial", 20),
                bg="#0a0e27", fg="white").pack(pady=20)
        
        self.dep = tk.Entry(f, font=("Arial", 18), width=15)
        self.dep.pack(pady=20, ipady=10)
        self.dep.focus()
        
        tk.Button(f, text="START", font=("Arial", 16, "bold"),
                 bg="#00d4ff", fg="#0a0e27", padx=40, pady=15,
                 command=self.start).pack(pady=30)
        
        self.dep.bind('<Return>', lambda e: self.start())
    
    def start(self):
        """Process deposit"""
        try:
            self.balance = int(self.dep.get())
            if self.balance <= 0:
                raise ValueError()
            self.show_game()
        except:
            messagebox.showerror("Error", "Enter valid amount!")
    
    def show_game(self):
        """Game screen using GRID layout"""
        self.clear_all()
        
        # Main frame
        main = tk.Frame(self.root, bg="#0a0e27")
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # CONFIGURE GRID - 10 rows
        for i in range(10):
            main.grid_rowconfigure(i, weight=0)
        
        # ===== ROW 0: TITLE =====
        tk.Label(main, text="SLOT MACHINE", font=("Arial", 40, "bold"),
                bg="#0a0e27", fg="#00d4ff").grid(row=0, column=0, columnspan=4, pady=20)
        
        # ===== ROW 1: BALANCE =====
        tk.Label(main, text="Balance:", font=("Arial", 16),
                bg="#0a0e27", fg="white").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.bal = tk.Label(main, text=f"${self.balance}", font=("Arial", 18, "bold"),
                           bg="#0a0e27", fg="#00d4ff")
        self.bal.grid(row=1, column=1, sticky=tk.W, padx=10)
        
        # ===== ROW 2: LINES =====
        tk.Label(main, text="Lines (1-3):", font=("Arial", 14),
                bg="#0a0e27", fg="white").grid(row=2, column=0, sticky=tk.W, padx=10, pady=15)
        
        self.lines = tk.Spinbox(main, from_=1, to=3, font=("Arial", 14),
                               width=5, bg="#0f3460", fg="white")
        self.lines.set(1)
        self.lines.grid(row=2, column=1, sticky=tk.W, padx=10)
        
        # ===== ROW 3: BET =====
        tk.Label(main, text="Bet per line ($):", font=("Arial", 14),
                bg="#0a0e27", fg="white").grid(row=3, column=0, sticky=tk.W, padx=10, pady=15)
        
        self.bet = tk.Spinbox(main, from_=1, to=100, font=("Arial", 14),
                             width=5, bg="#0f3460", fg="white")
        self.bet.set(10)
        self.bet.grid(row=3, column=1, sticky=tk.W, padx=10)
        
        # ===== ROWS 4-6: SLOTS =====
        slot_frame = tk.Frame(main, bg="#0a0e27")
        slot_frame.grid(row=4, column=0, columnspan=4, rowspan=3, sticky="nsew", pady=20)
        
        self.slots = []
        for r in range(3):
            for c in range(3):
                s = tk.Label(slot_frame, text="?", font=("Arial", 60, "bold"),
                           bg="#0f3460", fg="#00d4ff", width=4, height=2,
                           relief=tk.SUNKEN, bd=2)
                s.grid(row=r, column=c, padx=8, pady=8)
                self.slots.append(s)
        
        # ===== ROW 7: RESULT =====
        self.res = tk.Label(main, text="", font=("Arial", 14),
                           bg="#0a0e27", fg="white", wraplength=800, height=2)
        self.res.grid(row=7, column=0, columnspan=4, pady=15)
        
        # ===== ROW 8: BUTTONS =====
        btn_f = tk.Frame(main, bg="#0a0e27")
        btn_f.grid(row=8, column=0, columnspan=4, sticky="ew", pady=20)
        
        self.spin = tk.Button(btn_f, text="SPIN", font=("Arial", 16, "bold"),
                             bg="#00d4ff", fg="#0a0e27", padx=60, pady=20,
                             command=self.do_spin)
        self.spin.pack(side=tk.LEFT, padx=20, expand=True)
        
        tk.Button(btn_f, text="QUIT", font=("Arial", 16, "bold"),
                 bg="#ff006e", fg="white", padx=50, pady=20,
                 command=self.quit_game).pack(side=tk.LEFT, padx=20, expand=True)
    
    def do_spin(self):
        """Execute spin"""
        if self.spinning:
            return
        
        self.spinning = True
        self.spin.config(state=tk.DISABLED)
        self.res.config(text="SPINNING...", fg="#00d4ff")
        self.root.update()
        
        try:
            lines = int(self.lines.get())
            bet = int(self.bet.get())
            total = lines * bet
            
            if total > self.balance:
                messagebox.showerror("Error", f"Need ${total}, have ${self.balance}")
                self.spinning = False
                self.spin.config(state=tk.NORMAL)
                self.res.config(text="")
                return
            
            self.balance -= total
            
            cols = self.get_spin()
            self.show_spin(cols)
            self.root.update()
            self.root.after(600)
            
            wins, lines_won = self.check_wins(cols, lines, bet)
            self.balance += wins
            self.bal.config(text=f"${self.balance}")
            
            if wins > 0:
                msg = f"WON ${wins}! Lines: {', '.join(map(str, lines_won))}"
                self.res.config(text=msg, fg="#00ff41")
            else:
                msg = f"Lost ${total}"
                self.res.config(text=msg, fg="#ff006e")
            
            self.root.update()
            
            if self.balance <= 0:
                self.root.after(1500, lambda: messagebox.showinfo("Game Over", "Out of money!"))
                self.root.after(1600, self.show_deposit)
            else:
                self.root.after(2000, self.enable_spin)
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.spinning = False
            self.spin.config(state=tk.NORMAL)
    
    def get_spin(self):
        """Get random spin"""
        symbols = []
        for s, c in SYMBOL_COUNT.items():
            symbols.extend([s] * c)
        
        cols = []
        for _ in range(3):
            col = []
            sym = symbols[:]
            for _ in range(3):
                if sym:
                    s = random.choice(sym)
                    sym.remove(s)
                    col.append(s)
            cols.append(col)
        return cols
    
    def show_spin(self, cols):
        """Display spin"""
        idx = 0
        for r in range(3):
            for c in range(3):
                self.slots[idx].config(text=cols[c][r])
                idx += 1
    
    def check_wins(self, cols, lines, bet):
        """Check winners"""
        wins = 0
        lines_won = []
        for line in range(lines):
            sym = cols[0][line]
            if all(cols[c][line] == sym for c in range(3)):
                wins += SYMBOL_VALUE[sym] * bet
                lines_won.append(line + 1)
        return wins, lines_won
    
    def enable_spin(self):
        """Enable spin"""
        self.spinning = False
        self.spin.config(state=tk.NORMAL)
    
    def clear_all(self):
        """Clear all"""
        for w in self.root.winfo_children():
            w.destroy()
    
    def quit_game(self):
        """Quit"""
        messagebox.showinfo("Goodbye", f"Final: ${self.balance}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = SlotGame(root)
    root.mainloop()
