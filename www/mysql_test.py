import mysql.connector

conn = mysql.connector.connect(user='admin',password='admin123',db='gaoyu_test',host='192.168.0.145',port=3306)
cursor = conn.cursor()
cursor.execute('select * from users where id = %s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()