import mysql.connector

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",

)

if con.is_connected():
    print("koneksi ke server datase bebarhasil")

db = con.cursor()
db.execute("create database dbbuku")
