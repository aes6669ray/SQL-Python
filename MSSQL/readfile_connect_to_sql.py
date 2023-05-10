import pandas as pd
import pyodbc

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 0)
# df=pd.read_excel("20230203_111交叉查榜_V1.1.xlsx",sheet_name="學測交叉查榜")


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
cnxn = pyodbc.connect(connection_str)
cursor = cnxn.cursor()
if cursor:
    print("success")

sql="""
SELECT *
FROM
(SELECT T1.*,T2.縣市別 AS 考區地點
FROM
(SELECT *,本校地點 = N'新竹市'
FROM 大學交叉查榜 
WHERE 申請年 = 111 AND 本校名 = N'國立清華大學') AS T1
LEFT JOIN(
SELECT 學校代碼,學校名稱,公私立,縣市別,學校地址
FROM 大學地址
UNION
SELECT *
FROM 高中地址) AS T2
ON T1.考區 = T2.學校名稱) AS TMP
WHERE TMP.考區地點 IS NOT NULL"""
cursor.execute(sql)
data = cursor.fetchall()
desc = cursor.description

###end
cursor.close()
cnxn.close()


###to dataframe
# df_column = pd.DataFrame(desc)

# df = pd.DataFrame([list(i) for i in data],columns=df_column[0])
