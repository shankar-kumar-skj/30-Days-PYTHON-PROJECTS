name=input("ENTER YOUR NAME : ").upper()
print("WELCOME",name,"TO THIS ADVENTURE !!")
answer=input("YOU ARE IN A DIRTY ROAD, IT HAS COME TO AN END AND YOU CAN GO LEFT OR RIGHT .\n WHICH WAY WOULD YOU LIKE TO GO ??").lower()
if answer=="left":
    answer=input(" CHOOSE : \n SWIM / TALK / STOP : ").lower()
    if answer=="swim":
        print("you die will swimmming")
    elif answer=="walk":
        print("your accident is on road if you not drive properly")
    elif answer=="stop":
        print("stop following me \nI SEE YOU don't lie \nI SAY STOP THERE !!")
    else:
        print("TYPE PROPERLY !!")
elif answer=="right":
    answer=input(" CHOOSE : \n LOVE / CRUSH / LIFELINE : ").lower()
    if answer=="love":
        print("khud ko badlana chalaa tha ma pur unki yaado na bapas bula leya")
    elif answer=="crush":
        print("ek baar usha deka kya dekhta he ra geya \n socha kya sochta he raha geya \n  usha dekh dekh ka tarapta he raha geya!!")
    elif answer=="lifeline":
        print("ek jhalak to dekh jaya din ban jaya \n dekh jo uski jhalak puri mafil ban jaya!!")
    else:
        print("koi na bhai mera bhe undecided ha ( E3 ) !!")

else:
    print("SORRY !! BUT YOU CAN NOT INPUT A VALID DIRECTION !!")

