from kivy.uix.screenmanager import Screen
import sqlite3

class UpScreen(Screen):
    db = sqlite3.connect("register.db")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (name TEXT, mail TEXT, login TEXT, password TEXT)""")
    db.commit()
    user_name = input("Name:")
    user_mail = input("Mail:")
    user_login = input("Login:")
    user_password = input("Password:")
    cursor.execute("SELECT mail FROM users")
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES(?,?,?,?)", (user_name, user_mail, user_login, user_password))
        db.commit()
        print("Success!")
    else:
        print ("Already exist!")
        for value in cursor.execute("SELECT * FROM users"):
            print(value[1])