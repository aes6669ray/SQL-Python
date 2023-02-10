import pymysql
import pandas as pd

#資料庫連線設定
#可縮寫db = pymysql.connect("localhost","root","root","30days" )
db=pymysql.connect(host="localhost",user="root", passwd="", db="northwind", charset="utf8")   
#建立操作游標
cursor = db.cursor()
#SQL語法（查詢資料庫版本）
sql = "SELECT * FROM orders"
#執行語法
cursor.execute(sql)
result = cursor.fetchall()
#執行結果轉化為dataframe
df = pd.DataFrame(list(result))

#關閉連線
db.close()

