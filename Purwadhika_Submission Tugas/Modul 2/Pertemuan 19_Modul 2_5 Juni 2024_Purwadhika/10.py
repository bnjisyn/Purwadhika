# - Descriptive Analysis
# Menampilkan data historis, untuk melihat tren atau current condition
# Contoh : 
#     - Report Analysis Penjualan di tahun 2023 setiap Kuartal
#     - Ditambah Report penjualan di tahun 2022 setiap kuartal
# - Menampilkan apa yg terjadi - What Happen


# - Diagnostic Analysis
# Menampilkan apa yg terjadi DAN mengapa hal itu terjadi
# Contoh :
#     - Penjualan di 2023 Lebih tinggi dibandingkan 2022 Karena ....
# - Data historis - Why Happen




# - Predictive Analysis
# Menampilkan-Memprediksi Apa yg terjadi di masa depan 
# Contoh :
#     - Penjualan di 2025 sebesar .... setiap kuartal ....
# - Menggunakan Model statistika atau Model matematika atau model ML 


# - Prescriptive Analysis
# Kombinasi dari Descriptive - Diagnostic- Predictive
# - Kita memberikan 'resep' - Rekomendasi

# Mengkoneksikan SQL dengan Python
# Package - Library 
# mysql-connector-python
# Cara Install Package via VS Code 

# Gunakan terminal VS COde 
# Ketik 
# python3 -m pip install NamaPackage 
# python3 -m pip install mysql-connector-python

import mysql.connector 
# print('Installed')

# Package Alternatif 
# - pyMySQL
# - SQLLite
# # - SQLAlchemy

# SQL
# Server ====> Client 


# - Definisikan Server 
# - Definisikan Client ==> 
#     1. Definisikan User Akses
#     2. Definisikan Database 

myDB = {
    'user' : 'Kal',
    'password' : 'admin',
    'host' : 'localhost',
    'database' : 'marketing'
}


### Definisikan Client yg akan terkoneksi ke Database
conn = mysql.connector.connect(**myDB)
# print('Connection Success')

# mysql>_
Cr = conn.cursor() ### Digunakan untuk Eksekusi Query SQL 

# ## Describe Tabel Employee
# query = 'DEscribe Employee'
# Cr.execute(query)

# for i in Cr:
#     print(i[0],' - ', i[1])

## Membuat Tabel Baru
# query = '''
# CREATE TABLE Dosen (
# NIP char(20),
# NamaDosen char(30)
# )
# '''

# Cr.execute(query)
# print('Table Created')

## Memasukkan data ke dalam Tabel
# query = "INSERT INTO dosen VALUES ('D001', 'Jenny')"
# Cr.execute(query)

# conn.commit() ## Digunakan Ketika kita melakukan Perubahan data di dalam Tabel
# ## Create - Update - Delete

# print('Data Submitted')

# query = "INSERT INTO Employee (Nama, Salary, Kota) VALUES ('Dessy', 26000000, 'Bandung')"

# Cr.execute(query)
# conn.commit()

# print('Data Submitted')

# ## Alt Insert Data
# sql = 'INSERT INTO Dosen VALUES (%s, %s)'
# val = ("D002", "Sasa")
# Cr.execute(sql, val)

# conn.commit()
# print('Data Submitted')

# sql = "INSERT INTO employee (Nama, Salary, Kota, Gender, Usia) VALUES (%s, %s, %s, %s, %s)"
# val = ("Marco", 21000000, "Jakarta", "Pria", 25)

# Cr.execute(sql, val)
# conn.commit()
# print("Data Submitted")

## Insert berdasarkan Input User
# Id = input("Masukkan NIP Dosen : ")
# Nama = input("Masukkan Nama Dosen : ")

# sql = "INSERT INTO Dosen VALUES (%s, %s)"
# val = (Id, Nama)
# Cr.execute(sql, val)
# conn.commit()
# print("Data Submitted")

### INSERT Banyak Data
# sql = 'INSERT INTO Dosen Values (%s, %s)'
# val = [
#     ('D004', 'Alfa'),
#     ('D005', 'Beta'),
#     ('D006', 'Charlie'),
#     ('D007', 'Delta')
# ]
# Cr.executemany(sql, val)
# conn.commit()
# print("Data Submitted")

### Mengakses Data

## ALt 1
# query = 'SELECT * from Karyawan'
# Cr.execute(query)
# Data_id = []
# for i in Cr:
#     Data_id.append(i[0])
# userId = int(input("Masukkan User Id : "))
# if userId in Data_id:
#     print('Data Sudah Ada')
# else:
#     print('User Bisa diRegister')

## ALt 2
# query = "SELECT * FROM Karyawan"

# Cr.execute(query)

# data = Cr.fetchall()

# for i in data:
#     print(i)

### SELECT Variation
# query = "SELECT * FROM karyawan Order by Kota Limit 3"

# Cr.execute(query)

# for i in Cr:
#     print(i)


## UPDATE Data
# query = "Update Karyawan SET Kota = 'Surabaya' WHERE Nama = 'Jack' "
# Cr.execute(query)
# conn.commit()
# print('Data Updated')

# Id = int(input("Masukkan UserId karyawan yg akan diUpdate : "))
# Kota_new = input("Masukkan Kota Baru : ")
# query = "Update Karyawan SET Kota = %s WHERE NIK = %s"
# val = (Kota_new, Id)
# Cr.execute(query, val)

# conn.commit()
# print('Data Updated')

### HAPUS Data
# query = "Delete From dosen where nip = 'D004'"
# Cr.execute(query)
# conn.commit()
# print('Data Deleted')

Id = input("Masukkan NIP Dosen : ")
query = "DELETE FROM Dosen WHERE NIP = %s"
val = (Id,)
Cr.execute(query, val)
conn.commit()
print('Data Deleted')