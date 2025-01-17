import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

dim=(width,height)

f=cv2.VideoWriter_fourcc(*"XVID")

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Folder to save recording")
    if folder:
        print(f"SELECTED FOLDER: {folder}")
        return folder
save_dir = open_file_dialog()

NAME=input("ENTER THE NAME WHICH YOU WANT TO SAVE OF : ")
path=(f"{save_dir}/{NAME}.mp4")
output=cv2.VideoWriter(path,f,30.0,dim)

now_time=time.time()
dur=int(input("ENTER THE TIME TO STOP RECORDING (in sec.) : "))

end_time=now_time + dur

while True:
    image=pyautogui.screenshot()
    frame_1=np.array(image)
    frame=cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(frame)
    c_time=time.time()

    if c_time>end_time:
        break

output.release()
print("-----END----")