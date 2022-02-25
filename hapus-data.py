import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "dbbuku"
    
)

if con.is_connected():
    print("Hapus Data Berhasil")

dbcursor = con.cursor()
sql = "delete from buku where kode_buku = '3614'"
dbcursor.execute(sql)

con.commit()