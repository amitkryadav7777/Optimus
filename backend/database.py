import sqlite3

conn = sqlite3.connect("optimus.db")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_app_command(id integer PRIMARY KEY, name varchar(100), path varchar(1000))"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS web_command(id integer PRIMARY KEY, name varchar(100), url varchar(1000))"
cursor.execute(query)

# query = "DROP TABLE web_command"
# cursor.execute(query)

# query = "DELETE FROM sys_app_command WHERE id = 3"
# cursor.execute(query)

# query = "INSERT INTO sys_app_command VALUES (NULL,'Python','C:\\Users\\HP-PC\\AppData\\Local\\Programs\\Python\\Python311\\python.exe')"
# cursor.execute(query)

query = "INSERT INTO web_command VALUES (NULL,'YouTube','https://youtube.com')"
cursor.execute(query)


conn.commit()

# C:\Users\HP-PC\AppData\Local\Programs\Python\Python311\python.exe