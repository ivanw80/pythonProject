import pymysql
conn = pymysql.connect(host='remotemysql.com', database='2hUw8NsDPe', user='2hUw8NsDPe', password='BALn3Ia43h')
cursor = conn.cursor()
#cursor.execute("SELECT * FROM 2hUw8NsDPe.dogs;")
cursor.execute("INSERT INTO `2hUw8NsDPe`.`dogs`(name,age,breed) VALUES ('Shannon',13,'Malamute')")
#cursor.execute("DELETE FROM `2hUw8NsDPe`.`dogs`")
conn.commit()
cursor.close()
conn.close()