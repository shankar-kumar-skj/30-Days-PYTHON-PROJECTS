import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# # img=qr.make("HELLO_SKJ")
# # img.save("skj.png")
root = tk.Tk()
root.withdraw()
print("WELCOME !! \n       READY TO GENERATE CODE...!!")
data=input("ENTER THE LINK / TEXT /MESSAGE TO MAKE QR CODE : ")
COLOR1=input("ENTER THE COLOR IN WHICH YOU WANT TO SEE QR CODE \n (RED/YELLOW/GREEN/WHITE/PINK...) = ").upper()
COLOR2=input("ENTER THE BACKGROUD COLOR \n (RED/YELLOW/GREEN/WHITE/PINK..) = ").upper()
qr=qrcode.QRCode(version = 1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)

qr.add_data(data)
qr.make(fit=True)

def open_file_dialog():
    folder = filedialog.askdirectory(title="Select Folder to Save QR Code")
    if folder:
        print(f"SELECTED FOLDER: {folder}")
        return folder
save_dir = open_file_dialog()

img=qr.make_image(fill_color=COLOR1,back_color=COLOR2)

NAME=input("ENTER THE NAME WHICH YOU WANT TO SAVE OF : ")
img.save(f"{save_dir}/{NAME}.png")
