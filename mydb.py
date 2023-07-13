import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = 'kali'
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE scott")

print ("All Done!")