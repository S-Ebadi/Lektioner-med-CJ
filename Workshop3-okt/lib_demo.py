from random import random, randint, choice, shuffle
import time
import json
import tkinter as tk

'''
dice_cast = randint(1, 6)
print(dice_cast)

names = ["Alice", "Bob", "Charlie", "Diana"]
random_name = choice(names)
print(random_name)

shuffle(names)


for name in names:
    print("Getting name...")
    time.sleep(2)
    print(f"Name: {name}")

'''

root = tk.Tk()
root.title("Demo")

def hello():
    print("Hello, Tkinter!")

btn = tk.Button(root, text="Sahand va snygg....", command=hello)
btn.pack()

root.mainloop()
