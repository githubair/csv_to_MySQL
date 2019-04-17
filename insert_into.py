import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="romanpr99",
  database="mydatabase"
)


mycursor = mydb.cursor()


sql = "INSERT INTO file (FIO,Math,Fisics,IT) VALUES (%s, %s, %s, %s)"
val = ('MalininaMaria', 47, 26, 92)
mycursor.execute(sql, val)


mydb.commit()

print(mycursor.rowcount, "record inserted.")

