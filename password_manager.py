# master password not work properly do it 

from cryptography.fernet import Fernet

'''def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
write_key()'''
def load_key():
    file=open("key.key","rb")
    key= file.read()
    file.close()
    return key

MASTER_pwd = input("what is you master password ?")

key=load_key() + MASTER_pwd.encode()
fer=Fernet(key)

def view():
    with open('password.txt','r') as f:
       for line in f.readlines():
        data=line.rstrip()
        user,passw=data.split(" : ")
        print("----- PASSWORD MANAGER : ------")
        print("USER : ",user,"\nPASSWORD : ",fer.decrypt(passw.encode()).decode())

def add():
    name=input("ENTER ACCOUNT NAME : ")
    pwd=input("ENTER THE PASSWORD : ")

    with open('password.txt','a') as f:
        f.write(name+" : "+fer.encrypt(pwd.encode()).decode()+" " +"\n")



while True:
    mode= input("would you like to add a new password or view existing ones(view, add) or press q to quit??").lower()
    if mode=="q":
        break
    if mode=="view":
     view()
    elif mode=="add":
     add()
    else:
     print("INVALID ONES")
     continue
