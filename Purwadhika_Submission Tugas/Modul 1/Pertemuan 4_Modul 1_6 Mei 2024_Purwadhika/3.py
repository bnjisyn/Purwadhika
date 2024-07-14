# usia = int(input("Masukkan Usia : "))
# print("Usia anda 10 tahun lagi :", usia + 10)

### Error Handling Expression
# Basic Syntax :
# try:
#     Program ==> Program yg akan diuji ketika ada error
# except:
#     Notifikasi atau program yg akan dijalankan ketika ada error 

# try:
#     usia = float(input("Masukkan usia :"))
#     print("Usia anda 10 tahun lagi :", usia + 10)
# except:
#     print("Angka yg anda masukkan salah!!!")


### Looping
### Mengeksekusi Program secara berulang kali

# - While Loop ===> Secara Natural ===> Infinite Loop 
# - For Loop ===> Secara Natural ===> Finite Loop 

# - Looping memiliki Karakter yg mirip dg IF 
# - Karena Program yg akan dijalankan membutuhkan CONDITIONAL STATEMENT Bernilai TRUE
# - Perbedaan signifikan antara IF dan LOOP, IF hanya menjalankan Program 1X, LOOP menjalankan Program beberapa Kali 
# - Membutuhkan Conditional Statement untuk diuji (Boolean - TRUE atau FALSE)
# - Sama seperti IF, Looping juga bisa dilakukan secara hirarki-bertingkat (Nested Loop)
# - IF ==> Menjalankan Program 1X Jika Kondisi TRUE 
# - Loop ==> Menjalankan program beberapa kali SELAMA kondisi TRUE 
# - Looping akan berhenti ketika Kondisi bernilai FALSE 


# ###### While Looping

# Basic Syntax :
# While ...Kondisi...: Conditional Statement (TRUE atau FALSE)
#     Program ===> Program akan dijalankan SELAMA Kondisi bernilai TRUE

# angka = 1  ### Inisiasi Kondisi yg akan dilakukan Pengecekan (Define variabel)
# while angka < 10: ### Pengecekan Kondisi Variabel
#     print(f"Angka anda : {angka}") ### Program yg akan dijalankan selama KONDISI BERNILAI TRUE
#     angka += 1 ### Increment ==> Dibutuhkan untuk membuat Kondisi FALSE/ Dibutuhkan untuk menghentikan Proses Looping

# ### Proses pada Looping dikenal dg istilah Iterasi

# ## Proses Looping
# Iterasi awal - Inisiasi Pertama
# Iterasi - 1 : angka = 1
# Dilakukan pengecekan kondisi ==> angka < 10;
# 1 < 10 ===> TRUE 
# karena TRUE program di bawah While akan dijalankan
# print(f"Angka anda : {angka}")
# saat ini angka = 1
# Angka anda : 1 ===> ditampilkan di screen
# Proses Increment Manual ==> penambahan 1
# angka += 1
# angka = angka + 1
# angka = 1 + 1
# angka = 2
# ----- Iterasi ke - 1 Selesai; Diakhir iterasi ke - 1, angka = 2


# ----- Iterasi ke - 2 : angka = 2
# Dilakukan pengecekan kondisi ==> angka < 10;
# 2 < 10 ===> TRUE 
# karena TRUE program di bawah While akan dijalankan
# print(f"Angka anda : {angka}")
# saat ini angka = 2
# Angka anda : 2 ===> ditampilkan di screen
# Proses Increment Manual ==> penambahan 1
# angka += 1
# angka = angka + 1
# angka = 2 + 1
# angka = 3
# ----- Iterasi ke - 2 Selesai; Diakhir iterasi ke - 2, angka = 3

# ---- Iterasi ke - 3: angka = 3
# Dilakukan pengecekan kondisi ==> angka < 10;
# 3 < 10 ===> TRUE 
# karena TRUE program di bawah While akan dijalankan
# print(f"Angka anda : {angka}")
# saat ini angka = 3
# Angka anda : 3 ===> ditampilkan di screen
# Proses Increment Manual ==> penambahan 1
# angka += 1
# angka = angka + 1
# angka = 3 + 1
# angka = 4
# ----- Iterasi ke - 3 Selesai; Diakhir iterasi ke - 3, angka = 4
# ......
# .....
# .....

# ----- Iterasi ke - 9: angka = 9
# Dilakukan pengecekan kondisi ==> angka < 10;
# 9 < 10 ===> TRUE 
# karena TRUE program di bawah While akan dijalankan
# print(f"Angka anda : {angka}")
# saat ini angka = 9
# Angka anda : 9 ===> ditampilkan di screen
# Proses Increment Manual ==> penambahan 1
# angka += 1
# angka = angka + 1
# angka = 9 + 1
# angka = 10
# ----- Iterasi ke - 9 Selesai; Diakhir iterasi ke - 9, angka = 10

# ---- Iterasi ke -10: angka = 10
# dilakukan pengecekan kondisi ==> angka < 10
# 10 < 10 ==> FALSE 

# Karena FALSE program di bawah While Tidak dijalankan
# Proses LOOPING BERHENTI.


# angka = 689 ### Variabel Inisiasi untuk Looping

# tebak = 5 ## Variabel inisiasi untuk Looping
# ## Isi data untuk variabel tebak, bebas, asalkan BERBEDA dengan angka
# ## agar while LOOP bekerja-running

# while tebak != angka: ## Harus menghasilkan BOOLEAN
#     tebak = int(input("Masukkan angka tebakan anda : "))
#     if tebak == angka:
#         print("Tebakan anda benar")
#     elif tebak > angka:
#         print("Angka di bawah tebakan anda")
#     else:
#         print("Angka di atas tebakan anda")

password = 'John123'
Login =" " ## Isi bebas, yg penting harus BERBEDA dg Password

coba = 1
batas_coba = 5

## coba dan batas_coba adalah BATAS PERCOBAAN User input password

# while password != Login and coba <= batas_coba:
#     if coba <= batas_coba:
#         Login = input("Masukkan Password anda : ")
#         if Login != password and coba < batas_coba:
#             coba += 1
#             print(f"Password yg anda masukkan salah, Silakan Coba Lagi. Percobaan ke - {coba}")
#         elif Login != password and coba == batas_coba:
#             coba += 1
# #             print("Password anda salah, Kesempatan Anda Habis")
# #         else:
# #             print("Password anda benar, Anda berhasil Login - SELAMAT DATANG")

# while password != Login and coba <= batas_coba:
#     # if coba <= batas_coba:
#     Login = input("Masukkan Password anda : ")
#     if Login != password and coba < batas_coba:
#         coba += 1
#         print(f"Password yg anda masukkan salah, Silakan Coba Lagi. Percobaan ke - {coba}")
#     elif Login != password and coba == batas_coba:
#         coba += 1
#         print("Password anda salah, Kesempatan Anda Habis")
#     else:
#         print("Password anda benar, Anda berhasil Login - SELAMAT DATANG")

# ###### While Loop
# - Secara natural => Infinite Loop 
# - Inisiasi awal perlu mendefine Variabel 
# - Menggunakan operator comparison (==, !=, >, <, dst) ataupun Logical Operator (and - Or)
# - Variabel yg didefine digunakan di proses comparison
# - Proses Increment/Decrement dilakukan Manual
# - Increment/Decrement dibutuhkan untuk menghentikan Looping

# ### FOR LOOP
# - Secara natural => Finite Loop 
# - Inisiasi awal, Tidak perlu men-define Variabel
# - Proses Increment/Decrement dilakukan secara Otomatis
# - Proses Decrement/Increment dibutuhkan untuk menghentikan Looping
# - Karena proses decrement/Increment Otomatis, sehingga Looping bisa berhenti secara otomatis
# - Menggunakan Operator Membership - (IN)

# Basic Syntax :
# for ....variabel.... in ..... Iterable Object :
#     Program ....

# Variabel yg digunakan Bebas, mewakili isi dari Iterable Object 
# Umumnya hanya 1 huruf : i, j, k, l, m dst 

# # for kata in kalimat:
# #     if kata in 'aiueo':
# #         kalimat = kalimat.replace(karakter, ch.lower())

# Iterable Object ==> Object/Data yg memiliki Value lebih dari satu ===> String & Data structure
# Ciri dari Iterable Object, dapat menggunakan fungsi len(data) 
# len(data) ==> menghitung isi dari data
# NON iterable Object ==> Integer, Float, Boolean
## LOOPING akan dijalankan Hingga seluruh Data iterable diakses (Kondisi bernilai TRUE)

# angka = 5
# nama = "Michael"

# # print(len(angka))  ##Akan Error karna NON ITERABLE Object tidak memiliki LEN
# # print(len(nama))

# for i in nama:
#     print(i)

######## range()
# - range()
# - range mirip dg akses indexing dan berisi angka numerik
# - angka berupa Integer
# - Membuat deret angka INTEGER

# range(start, end, step)

# range(10)  ===> Ketika angka di dalam range hanya 1 angka, Angka tersebut berarti nilai END 
### Default start ==> 0
# ### Default dar8i Step ==> 1 ==> secara default terjadi penambahan 1 ==> increment otomatis

# for i in range(10):
#     print(i)


# ##range(1, 10) ==> ketika angka di dalam range ada 2 angka, angka tsb berarti START dan END
# ## Ketika step tidak ditentukan nilainya, maka menggunakan nilai STEP default ==> 1

# START dan END mengikuti aturan
# START ==> Inclusive
# END ==> Exclusive ==> Akses - pembuatan deret akan berhenti di END - 1 (Jika menggunakan STEP Default - Increment)
# dan END + 1 ==> Jika menggunakan STEP decrement

# range(1, 21, 1) ==> akses START = 1, END = 21 - 1 (Akses berhenti di nilai 20) ==> Increment otomatis
# range(20, 1, -1) ==> akses START = 20, END = 1 + 1 (Akan berhenti di nilai 2) ==> Decrement otomatis


### Syntax Tambahan untuk Looping

# #### BREAK
# ==> Untuk menghentikan Looping secara Paksa
# ==> Secara Normal/Natural ==> Looping akan berhenti ketika Kondisi FALSE 
# ==> BREAK biasanya dipasangkan dengan IF statement

# angka = 1
# while angka < 10:
#     print(f"Angka anda : {angka}")
#     if angka == 5:
#         break ## Semua program di bawah break (dalam Looping)
#     # Tidak akan dieksekusi
#     # akan lgsg mengeksekusi semua program di luar Looping
#     # Looping dihentikan secara Paksa ketika memenuhi Kondisi (IF)
#     print("Program dalam Looping")
#     angka += 1
# print("Program di luar Looping")

# for i in range(11):
#     print(i)
#     if i == 5:
#         break

# ###### Continue
# - Menghentikan Sementara proses Looping (Iterasi - Tahapan)
# - langsung ke iterasi berikutnya
# - akan men-skip / melewatkan SEMUA PROGRAM di bawah CONTINUE, 
# - Kemudian melanjutkan ke ITERASI BERIKUTNYA
# - CONTINUE sama seperti BREAK, biasanya dipasangkan dengan IF Statement

for i in range(10):
    print(i)
    if i == 5:
        print("Looping dihentikan oleh BREAK")
        break
print("Perintah di luar LOOPING")

print("=" * 50)

for i in range(10):
    
    if i == 5:
        print("Iterasi dihentikan CONTINUE")
        continue ## Iterasi dihentikan, Perintah di bawah continue tidak akan dieksekusi 
    ## Langsung ke Iterasi berikutnmya
    ## Langsung ke i = 6
    print(f"Perintah Bagian Iterasi ke - {i}")
    print(i)

###### BREAK & CONTINUE
BREAK 
- Proses KESELURUHAN LOOPING dihentikan secara Paksa
- Semua perintah di bawah BREAK Tidak dieksekusi
- DAN langsung PINDAH ke Perintah DI LUAR LOOPING

CONTINUE 
- Tahapan - Iterasi dari LOOPING yg dihentikan
- Semua perintah di bawah CONTINUE tidak dieksekusi 
- DAN Langsung pindah ke Iterasi Berikutnya