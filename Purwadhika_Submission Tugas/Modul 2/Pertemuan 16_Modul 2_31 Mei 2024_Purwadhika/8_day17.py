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
Conditional stats yg bisa digunakan => =, !=, >, <, >=, <=

### Menampilkan data dg Kondisi lebih dari 1
- Dari Kolom yg sama
Select Kolom1, Kolom2 From namaTabel  WHERE namaKolom in atau not in (Kondisi)

select Nama, Kota, Salary from employee WHERE Kota in ('Jakarta', 'Bandung');
-> menampilkan data yg Kota nya = Jakarta atau Bandung


-> Bisa menggunakan AND dan OR jika kondisi lebih dari satu

- Dari Beberapa Kolom yg berbeda (bisa juga untuk kolom yg sama)

### SEMUA KONDISI HARUS TERPENUHI ==> Menggunakan ==> AND
select Nama, Kota, Salary from employee WHERE Kota = 'Jakarta' AND Salary > 15000000;

Menampilkan data yg kotanya Jakarta DAN Salary di atas 15 Juta
(Kedua Kondisi HARUS terpenuhi)

#### SALAH SATU KONDISI Harus TERPENUHI ==> Menggunakan ==> OR
select Nama, Kota, Salary from employee WHERE Kota = 'Jakarta' OR Salary > 15000000;

Menampilkan data yg kotanya Jakarta ATAU Salary di atas 15 Juta
(SALAH SATU Kondisi HARUS terpenuhi)

## Kondisi untuk RENTANG tertentu

select Nama, Kota, Salary from employee WHERE Salary > 15000000 AND Salary < 30000000;
-> Menampilkan data yg gajinya antara 15 juta dan 30 juta, TETAPI 15 juta dan 30 juta TIDAK TERMASUK (TIDAK DITAMPILKAN)


select Nama, Kota, Salary from employee WHERE Salary >= 15000000 AND Salary <= 30000000;
-> 15 Juta dan 30 juta Termasuk (Akan ditampilkan)


select Nama, Kota, Salary from employee WHERE Salary BETWEEN 15000000 AND 30000000;
-> Menampilkan data yg gajinya antara 15 juta dan 30 juta
-> 15 Juta dan 30 juta Termasuk (Akan ditampilkan)

- BEtween selain digunakan untuk Numerik, Paling sering digunakan untuk Kolom bertipe DATE
=> Format tanggal di SQL ==> 'Tahun Bulan Tanggal' ==> 31 mei 2024 ==> '20240531'
Misal kolom tanggal
YEAR(tanggal) ==> untuk ekstrak Tahun
MONTH(tanggal) ==> Untuk ekstrak bulan
DAY(tanggal) ==> untuk ekstrak hari
DATEDIFF(tanggal1, tanggal2) ==> Untuk menghitung Selisih
Beberapa RDBMS memiliki syntax yg berbeda untuk ekstrak DATE, tapi intinya ==> Data bertipe DATE Bisa kita ekstraksi
Untuk melihat-mengetahui syntax yg digunakan bisa baca di dokumentasi masing-masing RDBMS

==> Menampilkan Data employee yg join dari tgl 1 januari 2024 s/d 31 januari 2024
Select nama, hireDate From employee Where hireDate BETWEEN '20240101 00:00:00' and '20240131 00:00:00'
Jika Jam-TIME ==> Jam : menit : detik
=> Kondisi yg digunakan di dalam BETWEEN bersifat Inclusive

### Kondisi dari kolom Sintetis
HAVING ===> Gunakan Having jika kondisi berdasarkan kolom sintetis

select nama, kota, salary, 0.15 * salary as Kenaikan from employee WHERE kota = 'Jakarta' HAVING Kenaikan > 3000000;
- WHERE digunakan untuk Kondisi berdasarkan Kolom Original => Kota 
- HAVING digunakan untuk Kondisi berdasarkan Kolom Sintetis => Kenaikan

### Mendapatkan Data yg memiliki karakter tertentu (String)

select Nama, Kota, Salary from employee WHERE Nama Like 'Andre';
=> menampilkan data yg sama dg query ==> WHERE Nama = 'Andre'

select Nama, Kota, Salary from employee WHERE Nama Like 'A%';
=> Menampilkan data yg Namanya diawali dg Karakter 'A', selanjutnya karakter bebas/random 

select Nama, Kota, Salary from employee WHERE Nama Like '%A';
=> Menampilkan data yg Namanya diakhiri dg Karakter 'A', sebelumnya karakter bebas/random 

select Nama, Kota, Salary from employee WHERE Nama Like '%A%';
=> Menampilkan data yg memiliki Nama dan dalam nama terdapat karakter A 

select Nama, Kota, Salary from employee WHERE Nama Like 'S%A';
=> Menampilkan data yg namanya diawali huruf S dan diakhiri huruf A 

## Kondisi tidak terbatas di karakter, kita bisa menggunakan Kata.

##### AGGregation #####
- Dalam SQL ==> SUM, COUNT, MIN, MA, AVG, MAX, MIN 
- Secara default hanya menampilkan 1 baris data, keculai menggunakan GROUP BY 

### Jumlah Data
SELECT COUNT(*) from Tabel;

SELECT COUNT(*) from employee;
Menampilkan Jumlah baris data (2 data atau lebih yg sama (Duplikat) akan dihitung 2 atau sesuai jumlahnya)

SELECT COUNT(DISTINCT Kota) from Employee;
Menampilkan Jumlah Kota yg Unik

### Summary data
SELECT SUM(Salary) From Employee;

## rata-rata
SELECT AVG(SALARY) FROM EMPLOYEE;

### Nilai Terendah
SELECT MIN(SALARY) FROM EMPLOYEE;


## Nilai tertinggi
SELECT MAX(SALARY) FROM EMPLOYEE;

### GROUP BY
- pengelompokkan data berdasarkan Kolom tertentu
- Biasanya dikombinasikan dg fungsi aggregat
- Ketika menampilkan data berdasarkan Kondisi Hasil dari Group By/Aggregat ==> Gunakan HAVING ==> Kolom sintetis 

SELECT Kota, AVG(Salary) From Employee GROUP BY Kota;
- menghasilkan rata-rata gaji untuk setiap Kota==> Dikelompokkan berdasarkan kota 

SELECT Kota, AVG(Salary) as RataGaji From Employee GROUP BY Kota HAVING RataGaji > 75000000;
- Menghasilkan nilai rata-rata gaji untuk setiap kota, yg rata-rata gajinya diatas 75 juta

SELECT ...... FROM .... WHERE .... GROUP BY .... HAVING .... ORDER BY .... LIMIT .....











