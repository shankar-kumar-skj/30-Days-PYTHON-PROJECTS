import pyautogui
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

ss=pyautogui.screenshot()
def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Folder to save the screenshot : ")
    if folder:
        print(f"SELECTED FOLDER: {folder}")
        return folder
save_dir = open_file_dialog()

NAME=input("ENTER THE NAME WHICH YOU WANT TO SAVE OF : ")
path=(f"{save_dir}/{NAME}.png")
ss.save(path)