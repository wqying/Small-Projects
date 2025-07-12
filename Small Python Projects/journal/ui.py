"""
Handles the user interface of the project using tkinter.
"""

import tkinter as tk
from tkinter import *


main_window = tk.Tk(screenName="main")
main_window.title("Welcome to...!")
title = tk.Label(main_window, text="Ying's Game of Life xD")
title.pack()
button = tk.Button(main_window, text="CLOSE BITCH", command=main_window.destroy)
button.pack()
main_window.mainloop()