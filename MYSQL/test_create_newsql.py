import pymysql
import pandas as pd
import numpy as np

df=pd.read_excel("456.xlsx")

#資料庫連線設定
db=pymysql.connect(host="localhost",user="root", passwd="", db="classwork", charset="utf8")   
#建立操作游標
cursor = db.cursor()
#SQL語法（查詢資料庫版本）

#執行語法
cursor.execute('''	CREATE TABLE IF NOT EXISTS companylist ( 
            id int primary key,
			company char(100),
			address char(100),
            item char(100),
            CEO char(50)
			)
       ''')
k=[]
for i in df.itertuples(index=False,name=None):
   k.append(i)

df2=pd.DataFrame(k,columns=["id","company","address","item","CEO"])
df2.dropna(inplace=True)
#print(df2)

sql='''INSERT INTO companylist (id, company, address,item,CEO) VALUES (%s,%s,%s,%s,%s)'''


for row in df2.itertuples():
    cursor.execute(sql,[row.id,row.company,row.address,row.item,row.CEO])


#cursor.executemany(sql, k)
db.commit()

#關閉連線
db.close()




