import sqlite3

def connect():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,phone_number integer ,no_of_days integer ,total integer)")
    conn.commit()
    conn.close()

def insert(name,phone_number,no_of_days):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO test VALUES(NULL,?,?,?,?)",(name,phone_number,no_of_days,calculator(no_of_days)))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM test")
    row=cur.fetchall()
    conn.close()
    print(row)

def search(Name,Phone,Days):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM test WHERE name =? OR phone_number=? OR no_of_days=?",(Name,Phone,Days))
    row=cur.fetchall()
    conn.close()
    print(row)

def edit(Name,Phone,Days):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM test WHERE name =? OR phone_number=? OR no_of_days=?",(Name,Phone,Days))
    row=cur.fetchall()
    index=row[0][0]

    NEW_Name=input("ENTER YOUR NEW NAME : ")
    NEW_Phone=input("ENTER YOUR NEW NUMBER : ")
    NEW_Days=input("ENTER NUMBER NEW OF DAYS : ")

    cur.execute("UPDATE test SET name=? ,phone_number=?, no_of_days=?,total=? WHERE id=?",(NEW_Name,NEW_Phone,NEW_Days,calculator(NEW_Days),index))
    conn.commit()
    conn.close()

def delete(name="",phone_number="",no_of_days=""):
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM test WHERE name =? OR phone_number=? OR no_of_days=?",(Name,Phone,Days))
    row=cur.fetchall()
    index=row[0][0]
    cur.execute("DELETE FROM test WHERE id =?",(index,))
    conn.commit()
    conn.close()


def calculator(no_of_days):
    total=1000*no_of_days
    return total

connect()

option =int(input('''WHAT DO YOU WANT TO DO :-
1.) INSERT ENTITY
2.) VIEW ALL
3.) EDIT
4.) UPDATE
5.) DELETE
6.) SEARCH
'''))

if option ==1:
    Name=str(input("ENTER YOUR NAME : "))
    Phone=int(input("ENTER YOUR NUMBER : "))
    Days=int(input("ENTER NUMBER OF DAYS : "))
    insert(Name,Phone,Days)


if option ==2:
    view()

elif option ==6:
    Name=input("ENTER YOUR NAME : ")
    Phone=input("ENTER YOUR NUMBER : ")
    Days=input("ENTER NUMBER OF DAYS : ")
    search(Name,Phone,Days)

elif option ==3:
    Name=input("ENTER YOUR NAME : ")
    Phone=input("ENTER YOUR NUMBER : ")
    Days=input("ENTER NUMBER OF DAYS : ")
    edit(Name,Phone,Days)

elif option ==5:
    Name=input("ENTER YOUR NAME : ")
    Phone=input("ENTER YOUR NUMBER : ")
    Days=input("ENTER NUMBER OF DAYS : ")
    delete(Name,Phone,Days)
