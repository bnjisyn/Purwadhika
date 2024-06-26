#### Mengupdate Struktur Tabel - Mengupdate Kolom/Fields

## Menambahkan Kolom Baru 
ALTER TABLE namaTabel ADD COLUMN namaKolom Tipedata(size) Atribut;

ALTER TABLE employee ADD COLUMN Umur tinyInt Default 23;
=> Akan menambahkan Kolom umur ke tabel employee dg tipe data TinyINT dan nilai default 23
Data yg sudah ada sebelumnya nilainya akan menggunakan nilai Default
Secara default Kolom yg ditambahkan akan berada di paling ujung kanan tabel


### Menghapus Kolom
ALTER TABLE namaTabel DROP COLUMN namaKolom;

ALTER TABLE employee DROP COLUMN Nama;

## Menambahkan Kolom di posisi Tertentu
- Sama seperti menambahkan kolom baru, tapi ada penambahan Atribut 

ALTER TABLE namaTabel ADD COLUMN namaKolom Tipedata(size) Atribut AFTER NamaKolom;

ALTER TABLE employee ADD COLUMN Umur tinyInt Default 23 AFTER Kota;
==> Menambahkan kolom Umur (Kolom baru) yg posisinya di sebelah kanan kolom Kota

### Mengubah Posisi Kolom yg sudah ada
ALTER TABLE namaTabel MODIFY namaKolom TipeData AFTER namaKolom;

ALTER TABLE Employee ModifY Kota Varchar(75) DEFAULT "Jakarta" AFTER Usia;
==> Mengubah posisi kolom Kota menjadi di sebelah kolom Usia 

#### Mengganti Tipe Data Kolom
ALTER TABLE namaTabel MODIFY namaKolom TipedataBaru;

ALTER TABLE Employee ModifY Kota Varchar(75);

### Mengubah Nama Kolom
ALTER TABLE namaTabel RENAME COLUMN namaLama TO namaBaru;

ALTER TABLE employee RENAME COLUMN Umur TO Usia;

### Mengganti nama Tabel
ALTER TABLE namaTabelLama RENAME TO namaBaru;

ALTER TABLE aset RENAME TO aset_kantor;

### Menambahkan User baru ke dalam Database
CREATE USER 'Coba'@'localhost' IDENTIFIED BY 'pwd123';

## Menambah Akses
GRANT ALL PRIVILEGES ON * . * TO 'Coba'@'localhost';

### Menambah user harus menggunakan Login root