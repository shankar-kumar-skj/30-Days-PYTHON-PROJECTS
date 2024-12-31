import random 
import time
OPERATOR =["+","-","*"]

MIN_OPERAND=3
MAX_OPERAND=12
total_problems=int(input("ENTER THE QUESTION WHICH YOU WANT TO SOLVE : "))

def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATOR)

    expression=str(left)+" "+operator+" "+str(right)
    answer=eval(expression)
    return expression,answer

wrong=0

input("PRESS ANY KEY TO START : ")
print("-----------------------------------------")
print("QUIZ START : \n    LET'S GO !!!")

start_time=time.time()

for i in range(total_problems):
    expression,answer=generate_problem()
    while True:
        guess=input("PROBLEM # "+ str(i+1)+" : "+expression+" = ")
        if guess==str(answer):
            break
        wrong+=1

end_time=time.time()
total_time=round(end_time - start_time,2)
print("-------------------------------------------")
print("NICE JOB!! \n YOU FINISHED THE",total_problems,"PROBLEMS IN",total_time,"SECONDS !!")

