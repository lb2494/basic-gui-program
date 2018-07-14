import sqlite3
db=sqlite.connect(listofbooks.db)
cur=db.cursor()
#this will create a table 
cur.execute('''create table books (
BookId integer primary key autoincrement,
Title text(20),
Author text(30),
Price real;''')
#this will add records into the table
try:
cur.execute('''Insert into book values(3,'Think Python','Allen B. Drowney',475);''')
cur.execute('''Insert into book values(4,'C Programming','Dennis and Richie',300);''')
cur.execute('''Insert into book values(5,'Guide to network Programming','Beej',550);''')
cur.execute('''Insert into book values(1,'Git magic','Ben Lynn',500);''')
db.close()
db.commit()

