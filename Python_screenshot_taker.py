import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def takeScreenshot():
    myscreen = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreen.save(save_path + "_screenshot.png")


myButton = tk.Button(text="Take screenshot", command=takeScreenshot, font=10)
canvas1.create_window(150, 150, window=myButton)
root.title("S.D-Python Screenshot Taker")

root.mainloop()
