import random

# print.randrange(-1,10) # -1 to 9 in inputs random numbers

# print.randrange(10) # 0 to 9 in inputs random numbers

# print.randint(-1,11) # -1 to 11 in inputs random numbers

top=input("TYPE THE NUMBER = ")
if top.isdigit():
    top=int(top)
    if top<=0:
        print("PLEASE ENTER THE VALUE GREATER THAN 0 NEXT TIME.")
        quit() 
else:
    print("please type a number next time")
    quit()

random_number=random.randint(0,top)
count=0
gusses=0
while True:
     gusses+=1
     user_guess=input("MAKE A GUESS : ")
     if user_guess.isdigit():
         user_guess=int(user_guess)
     else:
         print("PLEASE TYPE A NUMBER NEXT TIME.")
         count+=1
         continue
     if user_guess==random_number:
         print("YOU WIN \n YOU GUESS THE NUMBER =",user_guess,"\nNo. OF ERROR = ",count)
         break
     
     elif user_guess>random_number:
         print("YOU GOT IT WRONG !!")
         count+=1
         print("YOU ARE ABOVE THE NUMBER")
        
     else:
            print("YOU ARE BELOW THE NUMBER")


print("YOU GOT IT IN ", gusses ,"\nYOU WIN!!")













































































































