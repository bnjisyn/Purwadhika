####Sub Query - Nested Query
- Jika ada query di dalam query

- Biasanya jika ada ketentuan yg nilainya fleksibel (tidak fix) dan berasal dari query result

SELECT Kota, Avg(Salary) as rataGaji FROM employee
WHERE Gaji > (Select avg(salary) From Employee) ==> Semakin bertambah employee, jumlah rata-rata gaji akan berubah sehingga kita tidak bisa menggunakan angka Fix 
GROUP BY Kota 
HAVING rataGaji > 75000000
ORDER BY Kota desc
LIMIT 3


### Primary Key
- Kolom/Fields Khusus yg memiliki Data Unik 
- Dimanfaatkan untuk / sebagai Representasi dari Baris Data 
- Identifier dari baris data 
Contoh : 
NIK KTP 
no NPWP
no SIM 
no Paspor
produt_id

- Primary Key tidak bisa NULL (Harus di isi)
- Primary Key tidak bisa duplikat (setiap baris data HARUS UNIK/Berbeda)
- Terkadang memiliki Atribut auto_increment dan NOT NULL
- Ketika ada kolom/fields memiliki atribut auto_increment ==> PrimKey
- PrimKey jika digunakan di tabel lain, istilahnya berubah menjadi Foreign Key 
- Sehingga Foreign Key bisa duplikat
- Foreign Key digunakan sebagai penghubung (Relasi) antar Tabel


TAbel A =========================================================> Tabel B 
Primkey_A -------------------------------------------------------> Primkey_A ==> menjadi Foreign Key 
- PrimKey_A menjadi penghubung antara Tabel A dan Tabel B 
- Nama Kolom dari PrimKey_A tidak harus sama ketika menjadi Foreign Key di Tabel B, tetapi isinya identik

### JOIN Table

- Menggabungkan 2 atau Lebih Tabel dan menghasilkan 1 Tabel Result

### Langkah nya 
- Lihat Hasil/Result ===> tentukan Bentuk dari Tabel result 
- Tentukan Asal Tabel dari SETIAP Kolom yg ada pada OUTPUT/Result 
- Temukan PrimKey - ForeignKey => Kolom yg menjadi Penghubung tabel - tabel tersebut
Tabel 1, Tabel 2, Tabel 3 
tabel 1 -> tabel 2 ==> tabel 4 ==> tabel 5 ==> tabel 6 ==> tabel 3

===> Kolom yg namanya SAMA atau yg ISINYA SAMA/Identik  dari 2 atau lebih tabel yg berbeda 

- Tentukan Jenis JOIN yg Digunakan 

===> Untuk menentukan Jenis JOIN, Lihat Output/Resultnya ==> Data NULL 
- Jika tidak ada Data NULL ===> INNER JOIN => JOIN 


Jika ada data NULL ==> Tidak menggunakan INNER JOIN 

Jika ada data NULL, Lihat Posisi NULL 
- Jika posisi NULL ada di Kolom dari Tabel Kanan ==> LEFT JOIN
- Jika posisi NULL ada di Kolom dari Tabel Kiri ==> RIGHT JOIN
- Jika posisi NULL ada di kolom Tabel Kanan dan Kiri ==> Gunakan UNION dari LEFT dan RIGHT JOIN 


Karyawan LEFT JOIN Jabatan
Karyawan RIGHT JOIN Jabatan


Karyawan ==> Tabel Kiri
Jabatan ==> Tabel Kanan


Jika ada Nama Kolom yg sama di 2 Tabel berbeda, ketika memanggil Kolom
harus disertakan Asal Tabel nya 

Misal =>
Dosen :
    NIP :
    nama :
    Kota : 
Mahasiswa :
    NIM :
    Nama :
    Matkul :
    NIP :

Select Mahasiswa.Nama, Dosen.Nama, Matkul, Kota  from Dosen JOIN Mahasiswa ON Dosen.NIP = Mahasiswa.NIP