import random
import string

def generate_password(min_length,number=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    charcters=letters
    if number:
        charcters+=digits
    if special_characters:
        charcters+=special

    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(charcters)
        pwd += new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True

        meets_criteria=True
        if number:
            meets_criteria=has_number
        if special_characters:
            meets_criteria= meets_criteria and has_special

    return pwd

min_lenght=int(input("ENTER THE MINIMUM LENGTH: "))
has_number=input("DO YOU HAVE NUMBERS (y/n)").lower()=="y"
has_special=input("DO YOU HAVE SPECIAL CHARACTERS (y/n)").lower()=="y"

password=generate_password(min_lenght,has_number,has_special)
print(password)