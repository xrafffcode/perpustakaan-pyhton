    import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "dbbuku"
    
)

if con.is_connected():
    print("koneksi ke server database berhasil")
tabel = con.cursor()
tabel.execute("create table if not exist tblbook(kd_buku varchar(10),"
              "nm_buku varchar(50), satuan varchar(12), stok int(8))")