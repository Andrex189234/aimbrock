import aimbot
from time import sleep
import tkinter as tk

window = tk.Tk()
window.resizable(False, False)

def first_print():
    exit()


text = "Are you sure to exit?"
text2 = "Yes"
text3 = "No"

text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 16))
text_output.grid(row=0, column=1, sticky="W")

first_button = tk.Button(text=text2, command=first_print)
first_button.grid(row=0, column=0, sticky="W")




window.mainloop()
