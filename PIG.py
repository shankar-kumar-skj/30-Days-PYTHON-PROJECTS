import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    player=input("enter the number of player (1-4) = ")
    if player.isdigit():
        players=int(players)
        if 2<=player<=4:
            break
        else:
            print("must be  between 2-4 players: ")
    else:
        print("OOPs! invalid,\n  try again")

max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores)<max_score:

    for player_index in range(players):
        print("\n NUMBER OF PLAYERS = ",player_index+1,"TURN HAS JUST STARTED !!\n")
        print("YOUR SCORE IS : ",player_scores[player_index],"\n")
        current_score=0
        
        while True:
            should_roll=input("WOULD YOU LIKE TO ROLL (y) : ").lower()
            if should_roll!="y":
             break

            value=roll()
            if value==1:
              print("YOU ROLLED A = 1! TURN DONE!")
              current_score=0
              break
            else:
              current_score+=value
              print("YOU ROLLED A : ",value)

            print("CURRENT SCORE = ",current_score)
    player_scores[player_index]+=current_score
    print("your total score is : ",player_scores[player_index])

max_score=max(player_scores)
winning_index=player_scores.index(max_score)
print("PLAYER NUMBER",winning_index +1,"IS THE WINNER WITH A SCORE OF : ",max_score)


    