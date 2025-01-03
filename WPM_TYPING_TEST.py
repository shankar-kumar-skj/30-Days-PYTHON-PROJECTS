import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the speed typing test!!")
    stdscr.addstr("\n PRESS ANY KEY TO BEGIN !!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,"WPM :",wpm)

    for i,char in enumerate(current):
        correct_char=target[i]
        color=curses.color_pair(1)
        if char != correct_char:
            color=curses.color_pair(2)

        stdscr.addstr(0,i,char,color)

# def load_text():
#     with open ("text.txt","r") as f:
#         lines=f.readlines()
#         return random.choice(lines).strip()
    
def wpm_test(stdscr):
    # target_text=load_text()
    target_text="Hello World this is some test text for this app! Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sit maxime, dolorem impedit officia labore error. Omnis repellat enim recusandae, eveniet laborum nihil mollitia minus odit ratione at? Cum qui nemo veniam nostrum atque tempore? Non ratione vel eum ea, iure veritatis iste quaerat alias velit impedit explicabo? Dolor, harum magnam."
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)

    # stdscr.clear()
    # stdscr.addstr(target_text)
    # stdscr.refresh()
    # stdscr.getkey()
    while True:
        time_elapsed=max(time.time()-start_time,1)
        wpm=round((len(current_text)/(time_elapsed/60))/5)

        stdscr.clear()

        display_text(stdscr,target_text,current_text,wpm)

        stdscr.refresh()

        if "".join(current_text)== target_text:
            stdscr.nodelay(False)
            break

        try:
            key=stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        # ASCII "a"=97 "A"=65
        if key in ("KEY_BACKSPACE","\b","\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
                current_text.append(key)



def main (stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
       wpm_test(stdscr)
       stdscr.addstr(2,0,"YOU COMPLETE THE TEXT!! \n PRESS ANY KEY TO CONTINUE ...")
       key=stdscr.getkey()

       if ord(key) ==27:
           break

    # stdscr.clear()
    # stdscr.addstr(0,0,"hello world!!")
    # stdscr.addstr(1,0,"hello world!!")
    # stdscr.addstr("HELLO WORLD!!")
    # stdscr.refresh()
    # key=stdscr.getkey()
    # print(key)
wrapper(main)