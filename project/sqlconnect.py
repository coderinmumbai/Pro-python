
import sqlite3  
  
# create a database named backup
cnt = sqlite3.connect("backup.sqlite3") 

cnt.execute('''CREATE TABLE HARSHAD(
ID INTEGER,
NAME TEXT
); ''')





cnt.execute('''INSERT INTO HARSHAD
VALUES( 1,"DOG"),(2,"CAT"),(3,"TIGER"),(4,"LION");''')


#To delete 

cnt.execute('''delete from harshad where NAME='TIGER'; ''')


# commit changes to the database
cnt.commit()


