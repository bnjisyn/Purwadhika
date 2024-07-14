###### Start SQL
Server ===> Client

Kita bekerja di Client

Server :
- Server di device yg sama dg Client ==> Localhost
- Server harus ON ==> server mySQL secara default auto-run 

Client/User ==> 

Ada 3 alternatif :
Alt 1 : Menggunakan MySQL Workbench => GUI
Alt 2 : Melalui MySQL Command Line Client
Alt 3 : Melalui Command Line / Terminal


### Alt 3
Melalui cmd/terminal
- Buka cmd/terminal
- Masuk ke Path Server MySQL : C:\Program Files\MySQL\MySQL Server 8.0\bin
- Masukkan user dan password dg mengetik
mysql -u NamaUser -p (kemudian enter)

- Masukkan password

- Kalau cursor sudah berubah menjadi

mysql>_
Berarti sudah masuk sebagai client


#################################################################
## Gunakan selalu semicolon (;) untuk mengakhiri Query

## Query di SQL ==> snake casing ==> Tidak case sensitive


### Melihat database di server
show databases;


## Membuat database
Create Database namaDatabase;

create Database Marketing;

create database HR;

### Menghapus database
drop database namaDatabase;

drop database HR;

### Menggunakan atau memilih atau mengaktifkan database;

use namaDatabase;

use marketing;

use HR;


### Membuat Tabel 
- Tabel dibuat beserta struktur nya
create Table namaTabel (Kolom/Field TipeData AtributData);

create table Aset(noAset tinyInt, namaAset char(35), Stok SmallInt);

### Melihat daftar Tabel dalam Database
show tables;

### Menghapus Tabel
drop table namaTabel;

drop table Aset;

### Melihat struktur Tabel
desc namaTable;

describe namaTable;

desc Aset;

describe Aset;

#### memasukkan Data ke dalam Tabel
INSERT INTO namaTabel VALUES (data yg akan dimasukkan);
- Susunan/urutan data yg dimasukkan harus sesuai dg urutan Fields/Kolom pada Tabel

- Memasukkan 1 data 
INSERT Into Aset VALUES (12, "Pensil", 250);

- Memasukkan Beberapa data sekaligus
INSERT INTO ASET VALUES (16, "Pulpen", 150), (18, "Penggaris", 170), (10, "Buku", 60);

- Memasukkan data ke dalam tabel secara tidak berurutan atau hanya beberapa kolom
INSERT INTO namaTabel (Field1, Fields2, Fields3, dst) VALUES (value1, value2, value3, dst)

insert into aset (Stok, noAset, namaAset) Values (600, 15, "Lemari");

insert INTO ASET (namaAset) Values ("Meja");
- Kolom yg tidak diisi (noAset & Stok) akan berisi NULL atau Nilai DEFAULT
- Jika kolom yg tidak diisi memiliki atribut NOT NULL maka akan error,
Kecuali kolom tsb memiliki atribut auto_increment

#### Menampilkan data - Melihat isi tabel secara keseluruhan
SELECT * FROM namaTabel;

SELECT * FROM Aset;

#### Mengupdate Data (Baris data - value)
Update namaTable SET Fields = Value_baru; ==> akan mengubah fields tertentu untuk SELURUH DATA 

Update namaTable SET Fields = Value_baru WHERE Kondisi; ==> Hanya mengupdate data sesuai kondisi

- Update 1 Fields 
update Aset set Stok = 125 WHERE namaAset = "Meja";
- akan mengupdate stok dari meja menjadi 125

- Update beberapa fields 
update Aset SET namaAset = "Pensil Mekanik", Stok = 525 WHERE noAset = 12;
Akan mengubah/mengupdate namaAset menjadi "Pensil Mekanik" dan Stok menjadi 525 dari aset yg memiliki noAset = 12.

#### Menghapus data
DELETE from namaTable ==> akan menghapus seluruh data di Table

DELETE from NamaTable WHERE Kondisi ==> akan menghapus data sesuai kondisi.

delete from Aset WHERE namaAset = "Meja";
==> akan menghapus data aset yg memiliki namaAset Meja.

