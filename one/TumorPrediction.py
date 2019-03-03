import numpy as np

import cx_Oracle,os,sys,http.client,urllib.parse,urllib.request
words=request.post['txtWords']
conn = cx_Oracle.connect('wahaha','123456','18.97.27.6:1521/chrome')
cursor = conn.cursor()
sql = "select staff_number,cash,key_status,valid_time from staff_info where staff_number ='"+words+"'"
cursor.execute(sql)
for r in cursor.fetchall():
    print ("number: %s  cash: %s  status: %s  valid: %s " % (r[0], r[1],r[2],r[3]))
