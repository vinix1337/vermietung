import mysql.connector
import time
from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="main"
)


def getNowTime():
    now = datetime.now()
    current_time = time.strftime("%Y-%m-%d")
    return current_time

def createDB(name):
  mycursor = mydb.cursor()
  try:
    mycursor.execute("CREATE DATABASE " + name)
    mycursor.close()
  except Exception as e:
    print(e)
  print()
  return ""

def deleteDB(name):
    mycursor = mydb.cursor()
    try:
        mycursor.execute("DROP DATABASE " + name)
        mycursor.close()
    except Exception as e:
        pass
    print()
    return ""

def showDB(table):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall()
    mycursor.close()
    lenge = len(myresult)
    for x in myresult:
        print(x)


def getTimeOutOfDB():
    mycursor = mydb.cursor()
    mycursor.execute("")
    pass

def addWohnung(name):
    mycursor = mydb.cursor()
    time = getNowTime()
    try:
        sqlQuery = "INSERT INTO wohnungen (nachname, vertragsablauf) VALUES (%s, %s)"
        values = (name, time)
        mycursor.execute(sqlQuery, values)
        mydb.commit()
        mycursor.close()
    except Exception as e:
        print("[!] Fatal error: " + str(e))

def checkMietvertrag(name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from wohnung WHERE Name = %s", (name))

    pass


print("""
************************************************************
*  _    __                    _      __                    *
* | |  / /__  _________ ___  (_)__  / /___  ______  ____ _ *
* | | / / _ \/ ___/ __ `__ \/ / _ \/ __/ / / / __ \/ __ `/ *
* | |/ /  __/ /  / / / / / / /  __/ /_/ /_/ / / / / /_/ /  *
* |___/\___/_/  /_/ /_/ /_/_/\___/\__/\__,_/_/ /_/\__, /   *
*                                                /____/    *
*                                                          *
*                                       coded by armin     *
************************************************************                                     
""")

while True:
    print("[1] Daten anzeigen")
    print("[2] Wohnung hinzufügen")

    print("")
    auswahl = input("Auswahl: ")
    if auswahl == "1":
        table_name = input("Table-Name: ")
        showDB(table_name)
        break
    elif auswahl == "2":
        parameter = input("Wohnung hinzufügen: ")
        addWohnung(parameter)
        break