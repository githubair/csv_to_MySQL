import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="romanpr99",
  database="mydatabase"
)


mycursor = mydb.cursor()

sql = "DELETE FROM file WHERE N = 4"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
