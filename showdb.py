import pymysql
con = pymysql.connect(host="localhost", database="water", user="root", password="12345678", charset="utf8")
try:
	cur = con.cursor()
	cur.execute('SHOW DATABASES;')

	data = cur.fetchall()
	for i in data:
		print(f'{i[0]}')

except:
	print(" Have Error")

finally:
	con.close()