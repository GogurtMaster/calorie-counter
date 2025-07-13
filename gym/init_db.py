import sqlite3

conn = sqlite3.connect('data.db')

with open ('schema.sql', 'r') as f:
    schema = f.read()
    
conn.executescript(schema)

conn.commit()
conn.close()

print("database be working and shit")