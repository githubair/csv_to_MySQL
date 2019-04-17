import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="romanpr99",
  database="mydatabase"
)


mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE file (N int AUTO_INCREMENT PRIMARY KEY, FIO VARCHAR(255), Math int, Fisics int, IT int)")






