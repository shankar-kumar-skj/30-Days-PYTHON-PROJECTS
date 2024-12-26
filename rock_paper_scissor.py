import random

user_wins=0
computer_wins=0
options=["rock","paper","scissor","test"]

while True:
    user_input=input('Type Rock/Paper/Scissors or Q to quit : ').lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    # rock: 0, paper: 1 , scissors : 2
    computer_pick=options[random_number]
    print("COMPUTER PICKED : ",computer_pick ,"")

    if user_input=="rock" and computer_pick=="scissor":
        print("YOU WIN !!")
        user_wins+=1
        continue
    elif user_input=="paper" and computer_pick=="rock":
        print("YOU WIN !!")
        user_wins+=1
        continue
    elif user_input=="scissor" and computer_pick=="paper":
        print("YOU WIN !!")
        user_wins+=1
        continue
    else :
        print("SORRY !! YOU LOSE THISTIME BETTER TRY NEXT TIME !!")
        computer_wins+=1

print("YOU WINS = ",user_wins,"\nCOMPUTER WINS = ",computer_wins)
print("GOODBYE !!\n HAVE A NICE DAY!!\n   AND COME AGAIN !!")






