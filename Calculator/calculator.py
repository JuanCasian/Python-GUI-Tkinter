#!/usr/bin/env python3.7

from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.printable = StringVar()
        self.num1 = 0
        self.num2 = 0
        self.result = 0
        self.operator = "none"

        self.screen = ttk.Label(master, 
                font = ("Courier", 44), text = "0", anchor = "e")
        self.screen.grid(row  = 0, column = 0, columnspan = 5, sticky = "we")

        self.s = ttk.Style()
        self.s.configure("my.TButton", font = ("Courier", 44))
        
        self.button7 = ttk.Button(master, text = "7", style="my.TButton",
                command = self.but_7)
        self.button7.grid(row = 2, column = 0)

        self.button8 = ttk.Button(master, text = "8", style="my.TButton",
                command = self.but_8)
        self.button8.grid(row = 2, column = 1)

        self.button9 = ttk.Button(master, text = "9", style="my.TButton",
                command = self.but_9)
        self.button9.grid(row = 2, column = 2)

        self.button4 = ttk.Button(master, text = "4", style="my.TButton",
                command = self.but_4)
        self.button4.grid(row = 3, column = 0)

        self.button5 = ttk.Button(master, text = "5", style="my.TButton",
                command = self.but_5)
        self.button5.grid(row = 3, column = 1)

        self.button6 = ttk.Button(master, text = "6", style="my.TButton",
                command = self.but_6)
        self.button6.grid(row = 3, column = 2)

        self.button1 = ttk.Button(master, text = "1", style="my.TButton",
                command = self.but_1)
        self.button1.grid(row = 4, column = 0)

        self.button2 = ttk.Button(master, text = "2", style="my.TButton",
                command = self.but_2)
        self.button2.grid(row = 4, column = 1)

        self.button3 = ttk.Button(master, text = "3", style="my.TButton",
                command = self.but_3)
        self.button3.grid(row = 4, column = 2)

        self.button0 = ttk.Button(master, text = "0", style="my.TButton",
                command = self.but_0)
        self.button0.grid(row = 5, column = 1)

        self.buttondiv = ttk.Button(master, text = "/", style="my.TButton",
                command = self.but_div)
        self.buttondiv.grid(row = 1, column = 4)

        self.buttonmul = ttk.Button(master, text = "X", style="my.TButton",
                command = self.but_mul)
        self.buttonmul.grid(row = 2, column = 4)

        self.buttonmin = ttk.Button(master, text = "-", style="my.TButton",
                command = self.but_min)
        self.buttonmin.grid(row = 3, column = 4)

        self.buttonplus = ttk.Button(master, text = "+", style="my.TButton",
                command = self.but_plus)
        self.buttonplus.grid(row = 4, column = 4)

        self.buttonequ = ttk.Button(master, text = "=", style="my.TButton",
                command = self.but_equ)
        self.buttonequ.grid(row = 5, column = 4)

        self.buttonce = ttk.Button(master, text = "CE", style="my.TButton",
                command = self.but_ce)
        self.buttonce.grid(row = 1, column = 0, columnspan = 3, sticky = "we")
        
    def but_9(self):
        self.add_digit(9)
        self.update_screen()

    def but_8(self):
        self.add_digit(8)
        self.update_screen()

    def but_7(self):
        self.add_digit(7)
        self.update_screen()

    def but_6(self):
        self.add_digit(6)
        self.update_screen()

    def but_5(self):
        self.add_digit(5)
        self.update_screen()

    def but_4(self):
        self.add_digit(4)
        self.update_screen()

    def but_3(self):
        self.add_digit(3)
        self.update_screen()

    def but_2(self):
        self.add_digit(2)
        self.update_screen()

    def but_1(self):
        self.add_digit(1)
        self.update_screen()

    def but_0(self):
        self.add_digit(0)
        self.update_screen()

    def but_div(self):
        if (self.num2 != 0):
            self.but_equ("op")
        self.operator = "/"

    def but_mul(self):
        if (self.num2 != 0):
            self.but_equ("op")
        self.operator = "*"

    def but_min(self):
        if (self.num2 != 0):
            self.but_equ("op")
        self.operator = "-"

    def but_plus(self):
        if (self.num2 != 0):
            self.but_equ("op")
        self.operator = "+"

    def but_equ(self, income = "none"):
        print(self.operator)
        if (self.operator != "none"):
            if (self.operator == "/"):
                self.result = self.num1 / self.num2
            elif (self.operator == "*"):
                self.result = self.num1 * self.num2
            elif (self.operator == "+"):
                self.result = self.num1 + self.num2
            elif (self.operator == "-"):
                self.result = self.num1 - self.num2
            else :
                print("ERROR")
            self.operator = "res"
            self.update_screen()
            self.num1 = self.result
            if (income != "op"):
                self.operator = "none"
            print(self.operator)
            self.num2 = 0
            self.result = 0

    def but_ce(self):
        self.operator = "none"
        self.num1 = 0
        self.num2 = 0
        self.result = 0;
        self.update_screen()

    def add_digit(self, digit):
        if (self.operator == "none"):
            self.num1 *= 10
            self.num1 += digit
        else :
            self.num2 *= 10
            self.num2 += digit

    def update_screen(self):
        if (self.operator == "none"):
            self.screen.config(text = str(self.num1))
        elif (self.operator == "res"):
            self.screen.config(text = str(self.result))
        else :
            self.screen.config(text = str(self.num2))

def main():
    root = Tk()
    myCalculator = Calculator(root)
    root.mainloop()
        

if __name__ == "__main__":
    main()
