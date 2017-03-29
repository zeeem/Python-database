#python34
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb


localhost = 'server address'
user = 'root'
password = None
database= 'databaseName'
db_port = '3306'
#db = MySQLdb.connect(localhost , user , password, database)

#connection initiating
conn = pymysql.connect(localhost , user , password, database)
cur = conn.cursor()

#executing query
cur.execute("INSERT INTO `news` (`ID`, `TITLE`, `BODY`, `IMAGE`) VALUES ('','test title', 'test description', 'image link for test')")
cur.execute("SELECT * FROM `news`")

#fetching all data
row = cur.fetchall()

cur.close()
conn.close()

#printing result data
print (row)