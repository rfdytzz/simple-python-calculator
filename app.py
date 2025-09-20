import tkinter as tk
from tkinter import ttk, messagebox

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧮 Simple Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.expression = ""

        # Entry Display
        self.display = tk.Entry(self, font=("Segoe UI", 20), justify="right")
        self.display.pack(fill="x", padx=10, pady=10, ipady=10)

        # Buttons Layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
        ]

        for row in buttons:
            frame = ttk.Frame(self)
            frame.pack(fill="x", expand=True, pady=2)
            for btn in row:
                ttk.Button(frame, text=btn, command=lambda b=btn: self.add_to_expression(b), width=5).pack(side="left", expand=True, padx=2, pady=2)

        # Control Buttons
        ctrl = ttk.Frame(self)
        ctrl.pack(fill="x", pady=5)
        ttk.Button(ctrl, text="C", command=self.clear, width=7).pack(side="left", expand=True, padx=5)
        ttk.Button(ctrl, text="⌫", command=self.backspace, width=7).pack(side="left", expand=True, padx=5)
        ttk.Button(ctrl, text="=", command=self.calculate, width=7).pack(side="left", expand=True, padx=5)

    def add_to_expression(self, char):
        self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()


if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()
