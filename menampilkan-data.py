#menampilkan isi data dalam tabel
#fetchall () : untuk mengambil seluruh data
#fetchmany(3) : untuk mengambil beberaoa data (sesuai parameter)
#fetchome () : untuk mengambil satu data diawal
#fungsi-fungsi akan mengembalikan data list yang berisi record/tuple

import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "dbbuku"
    
)

dbcursor = con.cursor()
sql = "select * from buku"
dbcursor.execute(sql)
dt = dbcursor.fetchall()

for data in dt:
    print(data)