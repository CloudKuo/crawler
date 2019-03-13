import requests
import pandas
import sqlite3
import datetime
import urllib3
import certifi

'''res = requests.get('https://www.dcard.tw/_api/posts/')
logging.info(res.url)
Data_array = []
jd = res.json()
print(jd)
df = pandas.DataFrame(jd)
#print(df)
#df.info()

Data_array.append(df)'''
url = 'http://dcard.tw/_api/forums/nccu/posts'
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
res = requests.get(url, headers=headers)
print(res)
#r = http.request('GET', url)
jd = res.json()
df = pandas.DataFrame(jd)
print(df)

'''with sqlite3.connect('test.db') as mydb:
  df.to_sql('renthouse2', con=mydb)


mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute('Show Tables')
mycursor.execute("SELECT name FROM sqlite_master WHERE type='table';")#show exist table
print(mycursor.fetchall())
#insert = ("INSERT INTO customers(name, address) VALUES (%s,%s)")
#data = ('小明', 'Taipei City')
mycursor.execute("INSERT INTO customers (name, address) VALUES ('小明', 'Taipei City')")
#mycursor.execute(insert, data)


mycursor.execute("SELECT * FROM customers")
row = mycursor.fetchone()
while row is not None:
  print(row)
  row = mycursor.fetchone()'''






