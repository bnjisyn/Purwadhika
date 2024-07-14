#### Data Analysis

- EDA => Exploratory Data Analysis
- EDA => Explanatory Data Analysis 


### Data Collection

### Data Analytics & Data Visualization
Data Analytics ==> Bisa Berupa Tabel ==> Tabular
- Basic Statistics ==> Descriptive Stats

- Menggunakan Beberapa Package di Python untuk Analisis :
- Numpy 
- Scipy
- Pandas

Data Visualization ==> Grafik 
- Matplotlib
- Seaborn 
- Pandas


### Explanatory Data ==> Dashboard ==> Dalam 1 halaman ada lebih dari 1 Analisis (Analisis bisa berupa tabel atau Grafik) yg related

- Tableau


##### Data Collection
- Data Sources 

Internal 
==> Data berasal dari dalam perusahaan (bisa dari divisi/Bag. sendiri atau div. bagian lain)
- ERP ==> Enterprise Resources Planning ==> Software yg mengintegrasi seluruh data di perusahaan
- Melalui Sistem - Aplikasi - ERP 
- Menggunakan softcopy 

==> Database ==> CRUD 
- Kita melalukan CRUD ke database melalui Aplikasi (in general)
- YG bisa langsung melakukan CRUD ke database ==> Super Admin ==> All Access 
- Read ==> Dibatasi ==> Hanya bisa "membaca" data yg dibutuhkan




External
- Data dari cutomer - Supplier 
- atau sumber lain yg Legal
- Melalui Internet ==> Web Publik



==================================================================================
Database ===> Basis data ==> u/ Menyimpan data, organize data, retrieve data 
ETL ==> Extract, Transform, Load 
CRUD ==> Create Read Update Delete


DBMS ==> Database Management System ==> Software yg digunakan untuk memaintain Database

RDBMS ==> Relational Database Management System 
==> Database Berbasis Relasi 
==> Tabel ==> Menyimpan data di RDBMS 
==> Setiap Tabel saling berhubungan - saling berelasi 
Contoh RDBMS : PostgreSQL, Oracle, Ms. Access, Athena, Ms SQL Server, MySQL, BigQuery 
Bahasa yg digunakan - Query : Secara defacto ==> SQL ==> Structured Query Language
'20240527'
'2024-05-27'

NoSQL => Not Only SQL ==> Unstructured Data ==> Document store, Graph Based, Column Based 
Contoh : MongoDB, Cassandra, Hbase, Neo4J 

- Database architect/Modeller
- Data Engineer
- DB administrator

- Apps Transaksional ==> Ada transaksi di Apps ==> CRUD

RDBMS ==> Relational DBMS ==> SQL 
DDL ==> Data Definition Language ==> Memanipulasi Struktur Database
DML ==> Data Manipulation Language ==> Memanipulasi Struktur Data

SQL ==> Snake casing ==> Tidak pengaruh besar-kecil untuk Syntax

root ==> Akses paling tinggi ===> Super Admin ==> Administrator
Kita bisa membuat user dg Privilege yg sama dg root 


### Work with SQL
Database - Server ======== Network / Jaringan ==========> Client / User (Melalui Aplikasi)

- Server MySQL ==> secara default sudah berjalan auto-run (Windows services)
Biasanya di perusahaan server punya nama tersendiri ==> Jktsvr01
- Server MySQL yg auto-run ==> localhost 
- Create User 
- Login ke dalam sistem - server - DB 
- Create Database 
- use database 
- Create Table ==> Membuat Tabel sekaligus struktur tabel (Nama Kolom dan tipe data tiap kolom)
- Insert data sesuai dg struktur tabel 
- Bisa melakukan DML 


======================================================
SQL ==> Data ==> Rows (Baris => Tuple), Columns (Kolom => Field)

Tipe data dalam SQL 
- Numerik
- String 
- Date 
- Text 

###################################################################
Numerik 
- Integer 
- Fixed Point 
- Floating Point 

###### Integer ==> Bilangan Bulat (Bukan desimal)
- tinyInt ==> Tiny Integer ==> -128 s/d 127
- smallInt ==> - 32.768 s/d 32.767
- MediumInt ==> - 8.3juta s/d 8.3 juta
- INT ==> -2.1milyar s/d 2.1Milyar
- BigINT ==> paling luas jangkauannya ==> paling banyak lah

Paket Internet ==> ISP ==> 500 GB per Bulan 
2 GB 
5 GB 
4 GB

Paket internet ==> 10 GB 
12 GB 

Contoh :
No Antrian daily Dokter gigi ==> Ga mungkin nyampe jutaan ==> Pake TinyInt

#### Fixed Point ==> Bilangan desimal/pecahan
Bil. Desimal yg jumlah angka di belakang komanya dan jumlah digit angkanya sudah ditentukan dari awal 

Define menggunakan 2 angka ==> DECIMAL(Angka1, Angka2)
- Angka1 ==> Menunjukkan jumlah seluruh digit angka (Maksimal)
- Angka2 ==> Menunjukkan jumlah angka di belakang koma

DECIMAL(4, 2) ==> Total digit angka => 4, Total angka di belakang koma => 2
Range ==> -99.99 s/d 99.99

DECIMAL(4, 1) ==> -999.9 s/d 999.9
DECIMAL(3, 2) ==> -9.99 s/d 9.99
DECIMAL(3, 1) ==> -99.9 s/d 99.9

Angka1 ==> Maksimal 65
Angka2 ==> Maksimal 30

Maksimal ==> DECIMAL(65, 30)


############################### Floating point
# Angka desimal/pecahan yg digit dan angkanya tidak dibatasi
- Float 
- Double ==> 2x range dari float ==> size nya 2x lebih besar dari float 

#####################################
STRING 
- Char ==> Jumlah maksimal 255 karakter 
- Varchar ==> Jumlah maksimal 65.535 karakter

Char(20)
Varchar(25)
Varchar(20)

