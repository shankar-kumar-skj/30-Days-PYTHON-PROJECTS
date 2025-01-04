from playsound import playsound
import time

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"

def  alarm(seconds):
    time_elapsed=0

    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1

        time_left=seconds-time_elapsed
        minute_left=time_left//60
        seconds_left=time_left%60

        # print("TIME =",minute_left,":",seconds_left)
        print(f"{CLEAR_AND_RETURN}ALARM WILL SOUND IN {minute_left:02d}:{seconds_left:02d}")

    playsound("Anuv_Jain.mp3")

hours=int(input("HOW MANY hours TO WAIT : "))
minutes=int(input("HOW MANY MINUTES TO WAIT : "))
seconds=int(input("HOW MANY SECONDS TO WAIT : "))
total_seconds=(hours*3600)+(minutes*60)+seconds
alarm(total_seconds)
# playsound("Anuv_Jain.mp3")