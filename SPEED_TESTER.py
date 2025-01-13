from tkinter import *
import speedtest

def speed_check():
    sp=speedtest.Speedtest()
    sp.get_servers()
    downloading=str(round(sp.download()/(10**6),3))+"Mbps"
    uploading=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_downloading.config(text=downloading)
    lab_uploading.config(text=uploading)

sp = Tk()
sp.title("INTERNET SPEED CHECKER")
sp.geometry("500x650")
sp.config(bg="gray")

lab=Label(sp,text="INTERNET SPEED TEST",font=("Time New Roman",20,"bold"),bg="gray",fg="black")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="Downloading Speed",font=("Time New Roman",30,"bold"),bg="gray",fg="yellow")
lab.place(x=60,y=130,height=50,width=380)

lab_downloading=Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="gray",fg="white")
lab_downloading.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="Uploading Speed",font=("Time New Roman",30,"bold"),bg="gray",fg="yellow")
lab.place(x=60,y=290,height=50,width=380)

lab_uploading=Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="gray",fg="white")
lab_uploading.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="CHECK SPEED",font=("Time New Roman",30,"bold"),relief=RAISED,bg="black",fg="white",command=speed_check)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()