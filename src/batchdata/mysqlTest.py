import mysql.connector

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="root",database="customerdb")
cur=myconn.cursor()
try:
	cur.execute("create database pythonDB2")
	dbs = cur.execute("show databases")

except:
	myconn.rollback()
for x in cur:
	print(x)
myconn.close()
# printing the connection object
# print(myconn)
