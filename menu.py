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
    data = "3684" , "Bulan" , "Andrea" , "Gramedia" , "2012" , "10" , "0006"
    dbcursor.execute(sql,data)

    con.commit()

def fungsiinsert():
    import mysql.connector

    con = mysql.connector.connect(
        host = "localhost", 
        user = "root",
        password = "",
        db = "dbbuku"
        
    )

    dbcursor = con.cursor()
    sql = "insert into buku (id_buku,kode_buku,judul_buku,penulis_buku,penerbit_buku,tahun_penerbit,stok) values(%s,%s,%s,%s,%s,%s,%s)"
    data = ("0007" , "3744" , "Mantapu Jiwa" , "Jerome Pollin" , "Gramedia" , "2018" , "30")

    dbcursor.execute(sql,data)
    con.commit()

    print("Data berhasil disimpan")

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
    sql = "delete from buku where kode_buku = '3744'"
    dbcursor.execute(sql)

    con.commit()
    


def fungsimenu():
    print("1.View Data")
    print("2.Update Data")
    print("3.Insert Data")
    print("4.Delete Data")

    pilih = int(input("Pilih Menu : "))

    if pilih == 1:
        fungsiview()

    elif pilih == 2:
        fungsiupdate()

    elif pilih == 3:
        fungsiinsert()

    elif pilih == 4:
        fungsidelete()



print("Login Databases")
password = input("Masukan Password : ")
fungsimenu()

def ulang():
    x = 0
    while x == 0:
        pilih = input("Run Lagi? (y/t) : ")
        if pilih == "y" or pilih == "Y":
            fungsimenu()
        elif pilih == "t" or pilih == "T":
            print("Prgoram Ditutup")
            break
        else:
            print("Silahkan Pilih Menu")
              
ulang()