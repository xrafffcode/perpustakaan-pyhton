import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "dbbuku"
    
)

if con.is_connected():
    print("Update Data Behasil")

dbcursor = con.cursor()
sql = "update buku set kode_buku=%s, judul_buku=%s, penulis_buku=%s, penerbit_buku=%s, tahun_penerbit=%s, stok=%s where id_buku=%s"
data = "3614" , "Rumah Hantu" , "Jojon" , "Gramedia" , "2021" , "12" , "0005"
dbcursor.execute(sql,data)

con.commit()