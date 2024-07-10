import sqlite3

conn = sqlite3.connect("D:\\demo\\alpha.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE people 
                (first_name TEXT, last_name TEXT)""")

names_list = [
    ("Roderick", "Watson"),
    ("Roger", "Hom"),
    ("Petri", "Halonen"),
    ("Jussi", ""),
    ("James", "McMann")
]

cur.executemany("""
    INSERT INTO people (first_name, last_name) VALUES (?, ?)
""")

conn.commit()

conn.close()