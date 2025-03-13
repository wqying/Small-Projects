"""
Handles the user interface of the project using tkinter.
"""

from tkinter import *


main_window = Tk()
main_window.title("Welcome to...!")
title = Label(main_window, text="Ying's Game of Life :3")
title.pack()
button = Button(main_window, text="CLOSE BITCH", command=main_window.destroy)
button.pack()
main_window.mainloop()