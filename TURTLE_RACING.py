import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLORS=["red","yellow","green","black","pink","brown","cyan","orange","purple","blue"]

def get_number_of_racers():
    racers=0
    while True:
        racers=input("ENTER THE NUMBER OF RACERS (2 - 10) : ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("INPUT IS NOT NUMERIC ... \n     TRY AGAIN!!")
            continue
        if 2<=racers<=10:
            return racers
        else:
            print("OOPS! NUMBER IS NOT IN THE RANGE OF 2 - 10 \n     TRY AGAIN!!")

def race(colours):
    turtles=create_turtles(colours)

    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y= racer.pos()
            if y>=HEIGHT//2 -10:
                return colours[turtles.index(racer)]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("TURTLE RACING")
    # time.sleep(20)

def create_turtles(colours):
    turtles=[]
    spacing=WIDTH//(len(colours)+1)
    for i,color in enumerate(colours):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacing,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

racers=get_number_of_racers()
# print(racers)
init_turtle()

random.shuffle(COLORS)
colours=COLORS[:racers]

winner=race(colours).upper()
print(" HURRY!! \n   THE WINNER IS THE",winner,"COLOR TURTLE !!")
time.sleep(3)



































# racer=turtle.Turtle()

# racer.speed(3) #slow
# # racer.speed(1) #slowest
# # racer.speed(10) #fast
# # racer.speed(0) #fastest
# # racer.speed(6) #NORMAL 

# racer.shape("turtle")

# racer.color("cyan")

# racer.penup()

# racer.forward(100)
# racer.left(90)

# racer.pendown()

# racer.right(100)
# racer.backward(50)
# time.sleep(10)

# racer2=turtle.turtle()
# racer2.speed(5)
# racer2.shape("turtle")
# racer2.color("pink")
# racer2.penup()
# racer2.forward(10)
# racer2.left(50)
# racer2.pendown()
# racer2.right(90)
# racer2.backward(10)

# time.sleep(20)

