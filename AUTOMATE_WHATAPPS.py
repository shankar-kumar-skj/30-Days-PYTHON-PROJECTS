import pywhatkit as pyw
phone=input("ENTER THE PHONE NUMBER TO WHOM YOU SEND : ")
PHONE_NO=(f"+91{phone}")
MESSAGE=input("ENTER THE WHATAPPS MESSAGE : ")
HOURS=int(input("ENTER THE HOURS (if 3 pm then write 15) : "))
MINUTES=int(input("ENTER THE MINUTES : "))

pyw.sendwhatmsg(PHONE_NO,MESSAGE,HOURS,MINUTES)