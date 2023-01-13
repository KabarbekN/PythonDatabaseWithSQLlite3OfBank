import sqlite3

data_base = sqlite3.connect("bank.db") #Connect to database


cur = data_base.cursor() #Create cursor

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""") #Creating table

data_base.commit()

def continueWorking():
    print("Do you want to continue? y/n")
    answer = input()
    if answer == 'y':
        startDataBase()
    elif answer == 'n':
        print("Goodbye")



def addClient():
    print("Input login of user")
    user_login = input()
    print("Input password of user")
    user_password = input()
    print("Input cash of user")
    user_money = int(input())
    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        cur.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, user_money))
        data_base.commit()
        print('User was added to this system')
    else:
        print("Such user already exist")
    continueWorking()



def updateClient():
    user_login = input("Input user login that you want to change: ")
    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        print("There no such users")
        updateClient()
    else:
        new_user_login = input("Input new user login: ")
        new_user_password = input("Input new user password: ")

        cur.execute(f"UPDATE users SET login = '{new_user_login}' WHERE login = '{user_login}'")
        data_base.commit()
        cur.execute(f"UPDATE users SET password = '{new_user_password}' WHERE login = '{new_user_login}'")
        data_base.commit()
        continueWorking()



def deleteClient():
    user_login = input("Input user that you want to delete: ")
    cur.execute(f"DELETE FROM users WHERE login = '{user_login}'")
    data_base.commit()

    print("Record was deleted succesfully")
    continueWorking()



def showClients():
    cur.execute("SELECT rowid, login, password, cash FROM users ")
    print(cur.fetchall())
    print("")
    for i in cur.execute("SELECT login, password, cash FROM users"):
        print(*i)
    continueWorking()



def addCash():
    user_login = input("Input your name: ")
    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        print("There no such user")
        continueWorking()
    else:
        for i in cur.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
            balance = i[0]
        money = int(input(" Input money that you want to enter: "))
        cur.execute(f"UPDATE users SET cash  = {money + balance} WHERE login = '{user_login}'")
        data_base.commit()
        continueWorking()



def takeCash():
    user_login = input("Input your user name: ")
    user_password = input("Input your user name: ")

    for i in cur.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
        balance = i[0]
    for i in cur.execute(f"SELECT password FROM users WHERE login = '{user_login}'"):
        password = i[0]
    if user_password == password:
        print("Succesfully registered")
        money = int(input("How much money do you want to take ? "))
        cur.execute(f"UPDATE users SET cash = {balance - money} WHERE login = '{user_login}'")
        data_base.commit()
        continueWorking()
    else:
        print("Something is not correct")
        continueWorking()


    continueWorking()




def startDataBase():
    print("Put '1' if you want to add Client")
    print("Put '2' if you want to update Client")
    print("Put '3' if you want to delete Client")
    print("Put '4' if you want to show Clients")
    print("Put '5' if you want to addCash")
    print("Put '6' if you want to takeCash")
    num = int(input())
    if num == 1:
        addClient()
    elif num == 2:
        updateClient()
    elif num == 3:
        deleteClient()
    elif num == 4:
        showClients()
    elif num == 5:
        addCash()
    elif num == 6:
        takeCash()
    else:
        print("There no such function, please restart")
        startDataBase()

startDataBase()




data_base.close()

