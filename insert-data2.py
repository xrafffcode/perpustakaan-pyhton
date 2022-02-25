import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "dbbuku"
    
)

dbcursor = con.cursor()
sql = "insert into buku (id_buku,kode_buku,judul_buku,penulis_buku,penerbit_buku,tahun_penerbit,stok) ,%svalues(%s,%s,%s,%s,%s,%s)"
data = [("0001" , "3104" , "Laskar Pelangi" , "Andrea Hirata" , "Gramedia" , "2010" , "10"),
        ("0002" , "3204" , "Zaman Dahulu" , "Jojon Santoso" , "Gramedia" , "2012" , "12"),
        ("0003" , "3304" , "Belajar Python Pemula" , "Muhamad Rafli" , "Gramedia" , "2019" , "18"),
        ("0004" , "3404" , "G30SPKI" , "Lukman Haris" , "Gramedia" , "2000" , "12"),
        ("0005" , "3504" , "Budidaya Lele" , "Mukhlis" , "Gramedia" , "2020" , "18"),]

for val in data:
    dbcursor.execute(sql, val)
    con.commit()
print("Data berhasil disimpan")