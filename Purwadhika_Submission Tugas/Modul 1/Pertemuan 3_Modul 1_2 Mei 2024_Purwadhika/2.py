# Kalimat = input("Masukkan Kalimat : ")
# Char = input("Masukkan Vokal : ")
# Kalimat = Kalimat.replace("a", Char.lower()).replace("i", Char.lower()).replace("u", Char.lower()).replace("e", Char.lower()).replace("o", Char.lower())
# Output = Kalimat.replace("A", Char.upper()).replace("I", Char.upper()).replace("U", Char.upper()).replace("E", Char.upper()).replace("O", Char.upper())
# print(Output)

## Additional Function yg bisa menghasilkan TRUE atau FALSE
## Fungsi pada STRING
# nama = "michael "
# usia = '25'
# # Alfabet = A-Z, a-z 
# # Numerik = 0-9
# print(nama.isalnum()) ## Melakukan pengecekan STRING seluruhnya adalah Alfabet dan Numerik
# print(nama.isdigit()) ## Melakukan pengecekan STRING seluruhnya adalah Numerik
# print(usia.isdigit())
# print(nama.isalpha()) ## Melakukan pengecekan STRING seluruhnya adalah Alfabet
# print(nama.isupper()) ## Melakukan pengecekan STRING seluruhnya adalah Uppercase atau Kapital
# print(nama.islower())# Melakukan pengecekan STRING seluruhnya adalah Lowercase
# print(len(nama)) ## menghitung jumlah karakter (spasi dihitung 1)
# Merk = "Fanta25"
# print(Merk.isalnum())


#### Operasi Gabungan ==> Numerik
# Variabel yg akan digunakan harus sudah didefinisikan terlebih dahulu (sudah memiliki value sebelumnya)
angka = 10
# angka = angka + 15
angka += 15 ### Ini sama artinya dengan angka = angka + 15

# print(angka)
number = 20
number += 10 ## sama dengan number = number + 10
# print(number)

angka -= 5 ## angka = angka - 5

angka *= 2 ## angka = angka * 2

angka /= 2 ## angka = angka / 2

angka %= 2 ## angka = angka % 2

#### Operasi perbandingan - Comparison
## Hasil dari Comparison  ==> Boolean ===> TRUE atau FALSE
## output nya ==> TRUE atau FALSE

# a == b ## a sama dengan b
# == ## 'sama dengan' seperti yg kita kenal
# = ## Assignment (memasukkan value ke dalam variabel)
# a != b ## Tidak sama dengan
a = 5
b = '5'
# print(a)
# print(b)
# print(a == b)
# print(a != b)

# Penggunaan operator '==' & '!=' bisa digunakan untuk data STring dan Numerik

# ### Operator di bawah hanya untuk Numerik
# > ==> lebih dari 
# < ==> kurang dari 
# <=  ==> kurang dari atau sama dengan 
# >= ==> Lebih dari atau sama dengan 


# ### Operator Logika ==> menghasilkan True atau False
# AND 
# OR 
# NOT ==> Negasi ==> menghasilkan kebalikannya, jika value False hasilnya jadi True begitu sebaliknya (jarang dipake)

# # a dan b berupa Value BOOLEAN (True atau False)

# # a and b ==> akan bernilai TRUE jika nilai A dan B KEDUANYA TRUE 
# # a or b ==> akan bernilai FALSE Jika nilai A dan B KEDUANYA FALSE
# a = 5
# b = 15
# c = 25
# d = 20

# print((a < b) and (c < d)) ## hasilnya False karena nilai c < d menghasilkan FALSE
# print((a < b) or (c < d)) ## hasilnya True karena nilai a < b menghasilkan TRUE

# ## Operator Membership
# # # IN dan NOT IN 
# kalimat =  'nama saya dedi dan tinggal di jakarta'
# print('Saya' in kalimat)
# print('bandung' in kalimat)
# print('tinggal' not in kalimat)

## IF statement => Conditional Statement
# pengecekan Kondisi
# Kondisi yg akan dicek adalah apakah Kondisi bernilai TRUE atau FALSE

# Basic Syntax :
# if ....Kondisi... : ##Kondisi Harus bernilai TRUE agar program dijalankan
#     program ## Program yg akan dijalankan jika Kondisi bernilai TRUE

## Jika ada 1 Ketentuan
# angka = int(input("Masukkan angka : "))
# if angka > 20:
#     print("Angka diatas 20")

# ## Jika ada 2 Ketentuan
# if ..Kondisi..: ## Jika hanya ada 2 Ketentuan gunakan if ...else....
#     program 1 ## Program 1 akan dijalankan jika Kondisi Bernilai TRUE
# else:
#     program 2 ## Program 2 akan dijalankan jika Kondisi bernilai FALSE

# if angka > 20:
#     print("Angka diatas 20")
# else:
#     print("ANGKA DIBAWAH 20")

## Jika ada Lebih dari 2 Ketentuan
# if ...kondisi 1...:
#     program 1 ==> Program 1 akan dijalankan jika Kondisi 1 bernilai TRUE
# elif ...kondisi 2 ...:
#     program 2 ==> Program 2 akan dijalankan jika Kondisi 2 bernilai TRUE
# elif ...kondisi 3 ...:
#     program 3 ==> Program 3 akan dijalankan jika Kondisi 3 bernilai TRUE
# else :
#     program 4 ==> Program 4 akan dijalankan Jika SEMUA KONDISI Bernilai FALSE

# if angka > 20:
#     print("Angka diatas 20")
# elif angka == 20:
#     print("Angka sama dengan 20")
# else:
#     print("Angka kurang dari 20")

### NESTED IF
## IF dalam IF
nilai = 85
gender = 'male'

if nilai >= 80:
    if gender == 'male':
        print("Mahasiswa Teladan")
    else:
        print("Mahasiswi Teladan")
else:
    if gender == 'male':
        print("Mahasiswa Telatan")
    else:
        print("Mahasiswi Telatan")