######## Menampilkan Data
SELECT ..... FROM ..... 

## Menampilkan kolom tertentu
Select Kolom1, Kolom2 From namaTabel;

 Select Nama, Usia from employee;

### Menampilkan atau membuat Kolom sintetis
Kolom sintetis => Kolom yg tidak ada di tabel original

select Nama, Salary, 0.03 * Salary AS Iuran from employee;
- 0.03 * salary ==> akan menghasilkan kolom sintetis hasil kalkulasi 0.03 * salary setiap baris 
- as Iuran ==> Alias => Kolom sintetis akan ditampilkan dan diberi nama kolom sesuai Alias
- Alias dapat digunakan untuk Kolom original

##### Mengurutkan data
Select Kolom1, Kolom2 From namaTabel ORDER BY namaKolom;

select Nama, Kota, Salary from employee Order by Salary desc;
desc => descending => data akan diurutkan dari yg terbesar ke terkecil
asc => ascending => data akan diurutkan dari kecil ke besar 
secara default order by menggunakan ascending
Sehingga ketika kita akan menggunakan asc, kita tidak perlu menuliskan syntax nya 


Pengurutan bisa dilakukan berdasarkan lebih dari 1 kolom

select Nama, Kota, Salary from employee Order by Kota, Salary;
Data akan diurutkan berdasarkan Kota 
kemudian diurutkan lagi berdasarkan salary

#### Menampilkan sejumlah data tertentu
Select Kolom1, Kolom2 From namaTabel LIMIT angka;

select nama, kota, salary from employee order by salary desc LIMIT 2;
-> akan menampilkan 2 data dg Gaji tertinggi
-> Menampilkan 2 data teratas

select nama, kota, salary from employee order by salary desc LIMIT 3, 4;
-> menampilkan 4 data teratas setelah melewatkan (skip) 3 data sebelumnya


### Menampilkan data dg Kondisi Tertentu
Select Kolom1, Kolom2 From namaTabel  WHERE Kondisi 

select Nama, Kota, Salary from employee WHERE Kota = 'Jakarta';
-> menampilkan data yg Kota nya = Jakarta
Conditional stats yg bisa digunakan => =, !=, >, <, >=, <=, in, not in 
-> Bisa menggunakan AND dan OR jika kondisi lebih dari satu

### Kondisi dari kolom Sintetis
HAVING ===> Gunakan Having jika kondisi berdasarkan kolom sintetis

select nama, kota, salary, 0.15 * salary as Kenaikan from employee HAVING Kenaikan > 3000000;