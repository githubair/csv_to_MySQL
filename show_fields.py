import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="romanpr99",
  database="mydatabase"
)


mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW TABLES")


mycursor.execute("SELECT * FROM file")


for x in mycursor:
  print(x)