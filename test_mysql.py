import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="romanpr99",
  database="mydatabase"
)


mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("SHOW TABLES")

# mycursor.execute("CREATE TABLE file (FIO VARCHAR(255), Math int, Fisics int, IT int)")
# mycursor.execute("ALTER TABLE file ADD COLUMN N INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("SELECT * FROM file")

sql = "INSERT INTO file (FIO,Math,Fisics,IT) VALUES (%s, %s, %s, %s)"
val = ('MalininaMaria', 47, 26, 92)
mycursor.execute(sql, val)


mydb.commit()

print(mycursor.rowcount, "record inserted.")





# for x in mycursor:
#   print(x)

