import mysql.connector as mycon

db=mycon.connect(
    host='localhost',user='root',password='root',database='pydb'
    )
db_curr=db.cursor()
db_curr.execute('create table dmart(no int,name varchar(20),location varchar(8))')
