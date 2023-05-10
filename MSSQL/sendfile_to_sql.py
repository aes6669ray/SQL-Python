import pandas as pd
import pyodbc

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 0)
# df=pd.read_excel("111大學個人申請名額.xlsx")

###default setting
driver= "ODBC Driver 18 for SQL Server"
server = '' 
database = '' 
username = '' 
password = '' 
connection_str = f"""DRIVER={{{driver}}};
                     SERVER={server};
                     DATABASE={database};
                     uid={username};
                     pwd={password};
                     Trust_Connection=yes;
"""
###make connection
cnxn = pyodbc.connect(connection_str,charset='utf-8')
cursor = cnxn.cursor()
if cursor:
    print("成功連接")

###CREATE TABLE=====================================================
###重點筆記：IF NOT EXISTS不能用，英數字不能同時跟中文出現（也就是不能用"111大學個人申請名額"or"111年核定招生人數"），可以不指定primary key
# sql_create_table="""
# CREATE TABLE 大學個人申請名額 (
#     學校名稱 VARCHAR(75) COLLATE Chinese_Taiwan_Stroke_CI_AS,
#     系所名稱 VARCHAR(100) COLLATE Chinese_Taiwan_Stroke_CI_AS,
#     當年度核定招生名額 INT NOT NULL,
#     申請入學預計招生名額 INT NOT NULL,
#     學年度 INT NOT NULL
# );
# """

# cursor.execute(sql_create_table)
# cursor.commit()

###INSERT_DATA=========================================
# sql_insert_data='''
# INSERT INTO 大學個人申請名額 (學校名稱, 系所名稱, 當年度核定招生名額, 申請入學預計招生名額, 學年度) 
# VALUES (?,?,?,?,?);
# '''

# for row in df.itertuples():
#     cursor.execute(sql_insert_data,[row.學校名稱,row.系所名稱,row.當年度核定招生名額,row.申請入學預計招生名額,row.學年度])

cursor.commit()

###SEARCH_DATA==================================================================
sql_search_data="""SELECT * FROM 大學個人申請名額
"""

cursor.execute(sql_search_data)
data=cursor.fetchall()
desc=cursor.description


print("成功執行")
###end===============================================================================
cursor.close()
cnxn.close()

###to dataframe=======================================================
# df_columns=pd.DataFrame(desc)
# df_sql = pd.DataFrame([list(i) for i in data],columns=df_columns[0])

# print(df_sql)
