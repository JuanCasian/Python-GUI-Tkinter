#!/usr/bin/env python3.7

from tkinter import *
from tkinter import ttk

class CounterApp:
    def __init__(self, master):
        self.counter = 0
        self.label = ttk.Label(master, text = "Counter: " + str(self.counter))
        self.label.grid(row = 0, column = 0, columnspan = 2)

        ttk.Button(master, text = "Add one",
                command = self.add_one).grid(row = 1, column = 0)
        ttk.Button(master, text = "Substract one",
                command = self.sub_one).grid(row = 1, column = 1)

    def add_one(self):
        self.counter += 1
        self.label.config(text = "Counter: " + str(self.counter))
    
    def sub_one(self):
        if (self.counter >= 1):
            self.counter -= 1
        self.label.config(text = "Counter: " + str(self.counter))

def main():
    root = Tk()
    myApp = CounterApp(root)
    root.mainloop();

if __name__ == "__main__": main()
