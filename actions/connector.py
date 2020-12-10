import mysql.connector
import math, random 

mydb = mysql.connector.connect(
  host="localhost",
  user="prakash",
  password="",
  database = "lead_bot")

mycursor= mydb.cursor()

def user_commit(name, phone_number, email):
    mycursor.execute(f"insert into user(name,email_id,phone_number) values('{name}', '{phone_number}', '{email}')")
    mydb.commit()
