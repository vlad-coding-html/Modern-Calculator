# Fully Open Sourcd Modern Calculator - Made by Vladimir (https://vladweb.xyz)

import tkinter as tk
from tkinter import ttk
import math

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("320x500")
        self.root.configure(bg="#2C3E50")
        
        # Style configuration
        style = ttk.Style()
        style.configure("Modern.TButton",
                       padding=10,
                       font=('Helvetica', 12),
                       background="#34495E",
                       foreground="white")
        
        # Display
        self.equation = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        # Create the display frame
        display_frame = tk.Frame(root, bg="#2C3E50")
        display_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.display = tk.Entry(display_frame,
                              textvariable=self.display_var,
                              font=('Helvetica', 24),
                              bd=0,
                              justify=tk.RIGHT,
                              bg="#34495E",
                              fg="white")
        self.display.pack(padx=5, pady=5, fill=tk.X)
        
        # Create the buttons frame
        buttons_frame = tk.Frame(root, bg="#2C3E50")
        buttons_frame.pack(padx=10, pady=10)
        
        # Button layout
        buttons = [
            'C', '±', '%', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 'DEL'
        ]
        
        # Create and place buttons
        row = 0
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            btn = tk.Button(buttons_frame,
                          text=button,
                          width=4,
                          height=2,
                          font=('Helvetica', 14),
                          bd=0,
                          bg="#34495E" if button in '0123456789.' else "#E74C3C",
                          fg="white",
                          activebackground="#2980B9",
                          activeforeground="white",
                          command=cmd)
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def click(self, key):
        if key == '=':
            try:
                # Replace operators with Python operators
                result = self.equation.replace('×', '*').replace('÷', '/')
                result = str(eval(result))
                self.display_var.set(result)
                self.equation = result
            except:
                self.display_var.set("Error")
                self.equation = ""
        
        elif key == 'C':
            self.equation = ""
            self.display_var.set("0")
        
        elif key == 'DEL':
            self.equation = self.equation[:-1]
            self.display_var.set(self.equation if self.equation else "0")
        
        elif key == '±':
            try:
                if self.equation and float(self.equation) != 0:
                    if self.equation[0] == '-':
                        self.equation = self.equation[1:]
                    else:
                        self.equation = '-' + self.equation
                    self.display_var.set(self.equation)
            except:
                pass
        
        elif key == '%':
            try:
                result = str(float(self.equation) / 100)
                self.equation = result
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
                self.equation = ""
        
        else:
            self.equation += key
            self.display_var.set(self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ModernCalculator(root)
    root.mainloop()