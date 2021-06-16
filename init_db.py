import sqlite3 
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('mabase.db')

with open('schema.sql') as f:

    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO user (username,email,password) VALUES (?, ?,?)",
            ('test', 'test@gmail.com',generate_password_hash('test')))


connection.commit()
connection.close() 