import os,sys,psycopg2
from utils.connDB import PostgreDB

area_name = '雅域尚座'
sql = "Select * from tbl_area where area_name = '%s'" %(area_name)
params = area_name
PostgreDB().executeSQL(sql,params)
rows = PostgreDB().get_all()
urlList = []
for row in rows:
    urlList.append(rows)
print (urlList)
PostgreDB().closeDB()
