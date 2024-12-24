print(" WELCOME TO MY COMPUTER QUIZ !!")

PLAYING = input("DO YOU WANT TO PLAY ?  ")
if PLAYING.lower() != "yes":
    quit()

print("okay! let's play: ")
score =0
answer =input("Q1. WHAT DOES CPU STAND FOR ? ")
if answer.lower() =="central processing unit":
    print("CORRECT!!")
    score+=1
else:
    print("INCORRECT!!")

answer =input("Q2. WHAT DOES RAM STAND FOR ? ")
if answer.lower() =="random access memory":
    print("CORRECT!!")
    score+=1

else:
    print("INCORRECT!!")

answer =input("Q3. WHAT DOES ROM STAND FOR ? ")
if answer.lower() =="read only memory":
    print("CORRECT!!")
    score+=1

else:
    print("INCORRECT!!")

answer =input("Q4. WHAT DOES LAN STAND FOR ? ")
if answer.lower() =="local area network":
    print("CORRECT!!")
    score+=1
else:
    print("INCORRECT!!")

answer =input("Q5. WHAT DOES WAN STAND FOR ? ")
if answer.lower() =="wide area network":
    print("CORRECT!!")
    score+=1
else:
    print("INCORRECT!!")

answer =input("Q6. WHAT DOES SSD STAND FOR ? ")
if answer.lower() =="solid disk drive":
    print("CORRECT!!")
    score+=1
else:
    print("INCORRECT!!")

print("TOTAL SCORE =",score)






