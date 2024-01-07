import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def createTable(mydb):
    user_table = """
        CREATE TABLE USERS(
            uid INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
    """
    cursor = mydb.cursor()
    cursor.execute(user_table)
    mydb.commit()

def connectToDB():
    mydb = mysql.connector.connect(
        host= os.getenv("HOST"),
        user= os.getenv("DB_USER"),
        passwd= os.getenv("DB_PASS"),
        database= os.getenv("DB"),    
    )

    return mydb


def get_all_data():
    mydb = connectToDB()
    cursor = mydb.cursor()
    sql = "SELECT * FROM USERS"
    cursor.execute(sql)
    res = cursor.fetchall()
    data = []
    if (len(res) > 0):
        for x in res:
            data = {
                "_id": x[0],
                "name": x[1],
                "age": int(x[2])
            }
    return data


def get_data_byid(_id):
    mydb = connectToDB()
    cursor = mydb.cursor()
    sql = "SELECT * FROM USERS WHERE uid = %s"
    val = (_id,)
    cursor.execute(sql,val)
    res = cursor.fetchall()
    data = []
    if (len(res) > 0):
        for x in res:
            data = {
                "_id": x[0],
                "name": x[1],
                "age": int(x[2])
            }
            
    return data

def inser_data(name, age):
    mydb = connectToDB()
    cursor = mydb.cursor()
    sql = "INSERT INTO USERS (name, age) VALUES (%s, %s)"
    val = (name,age)
    cursor.execute(sql,val)
    mydb.commit()
    cursor.close()
    mydb.close()
    

def update_data(_id:int, name:str, age:int):
    mydb = connectToDB()
    cursor = mydb.cursor()
    sql = "UPDATE USERS SET name=%s, age=%s WHERE uid=%s"
    val = (name, age, _id)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()

def delete_data(_id):
    mydb = connectToDB()
    cursor = mydb.cursor()
    sql = "DELETE FROM USERS WHERE uid= %s"
    val = (_id,)
    cursor.execute(sql,val)
    mydb.commit()
    cursor.close()
    mydb.close()
