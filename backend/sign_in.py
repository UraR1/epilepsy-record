from kivy.uix.screenmanager import Screen
import sqlite3
class InScreen(Screen):
 db = sqlite3.connect("register.db")
 cursor = db.cursor()
 user_login = input("Login:")
 user_password = input("Password:")
 cursor.execute("SELECT * FROM users")
 if cursor.fetchone() is None:
  print("Register first!")
 else:
  print("Success!")