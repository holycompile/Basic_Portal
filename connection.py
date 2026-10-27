import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

# 1. Connection object needs to be here so `mydb` exists
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)



def insert_user(name, address):
  mycursor=mydb.cursor()
  sql="INSERT INTO user_data(name, address) VALUES (%s, %s)"
  mycursor.execute(sql,(name,address))
  mydb.commit()