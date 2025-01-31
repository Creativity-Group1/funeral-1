import sqlite3

connection = sqlite3.connect("contributors.db")
cursor = connection.cursor()

try:
    contributor_table = """CREATE TABLE IF NOT EXISTS contributor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
	contact TEXT NOT NULL,
	amount TEXT NOT NULL,
	beneficiary TEXT NOT NULL,
    admin_name TEXT NOT NULL
    )"""

    admin_table = """CREATE TABLE IF NOT EXISTS admin(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
	password TEXT NOT NULL
    )"""
    
    cursor.execute(admin_table)
    connection.commit()
    cursor.execute(contributor_table)
    connection.commit()
except connection.Error:
    print("debug print")
finally:
    if connection:
        connection.close()

def delete_rows(tb_name):
    connection = sqlite3.connect("contributors.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM {}".format(tb_name))
    connection.commit()
    print("done")


#delete_rows("contributor")







def insert_list_data(mlist,sql):
    connection = sqlite3.connect("contributors.db")
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, mlist)
        connection.commit()
        print("commited")
    except connection.Error as error:
        print(error)
    finally:
        connection.close()

    
admin = [("admin1", "L9jjJ7")
        #  ("admin2", "o2Wj8a"),
        #  ("admin3", "ks9S9w"),
        #  ("admin4", "nY0u4z"),
        #  ("admin5", "Suw3k5"),
        #  ("admin6", "p6LeqI"),
        #  ("admin7", "9Q8rDJ"),
        #  ("admin8", "uS878q"),
        #  ("admin9", "kFYu83"),
        #  ("admin10", "v4iLb6"),
        #  ("admin11", "2WYlPz"),
        #  ("admin12", "sR5F77"),
        #  ("master", "rn0208162005")
           ]

sql1 = """ INSERT INTO admin(name,password)VALUES(?,?)"""
insert_list_data(admin,sql1)