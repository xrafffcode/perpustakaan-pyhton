def fungsiview():
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

def fungsiupdate():
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

def fungsidelete():
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