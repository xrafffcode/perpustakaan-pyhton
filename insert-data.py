import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "dbbuku"
    
)

dbcursor = con.cursor()
sql = "insert into buku (id_buku,kode_buku,judul_buku,penulis_buku,penerbit_buku,tahun_penerbit,stok) ,%svalues(%s,%s,%s,%s,%s,%s)"
data = ("0007" , "3344" , "Bintang Langit" , "Andrea Hirata" , "Gramedia" , "2010" , "12")

dbcursor.execute(sql,data)
con.commit()

print("Data berhasil disimpan")