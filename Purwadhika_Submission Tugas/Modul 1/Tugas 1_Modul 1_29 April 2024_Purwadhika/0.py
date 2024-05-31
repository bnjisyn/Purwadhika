# ## Python
# # - High End Prog. Language
# # - Interpreter Language
# # - Case sensitive : A dan a itu beda
# # - Tidak membutuhkan semicolon (;)
# # - Tabulasi - Indentasi : memiliki fungsi sebagai penanda suatu Blok Kode 
# # Comment => agar Code tidak di eksekusi atau di run ==> menambahkan tanda # di depan kode
# ## Ini Comment

# ### Untuk Menampilkan / Mengeluarkan Hasil Code ke layar/screen
# ## Gunakan perintah
# print("Hello World")

# ## Cara Running - Eksekusi Code
# # - Button Run Code (Bentuk segitiga di pojok Kanan Atas)
# # - Via terminal (Pastikan Path terminal sudah tertuju di FIle yg akan di Run)
# # pyhton3 namaFile.py

# print(6)
# print(7+8)

# # Tipe Data di Python
# # ### Tipe data Primitif
# # - Tipe/Jenis Data dasar :

# # - String : alfanumerik
# # - Integer : Bilangan Bulat
# # - Float : Bilangan desimal
# # - Boolean : True dan False

# # #### String
# # - Ditandai dengan tanda kutip, ==> diapit oleh tanda kutip
# print("Halo")
# print('Selamat')
# print('''Malam''')

# # print('Selamat malam, hari ini hari jum'at')

# # Alt 1
# print('Selamat malam, hari ini hari jum"at')

# ## Alt 2
# print("Selamat malam, hari ini hari jum'at")

# ## Alt 3
# print('Selamat malam, hari ini hari jum\'at') ## Gunakan backslash sebagai penanda escape char
# # print("Selamat malam, 
# #       hari ini hari jum'at")
# # print('Selamat malam, 
# #       hari ini hari jum"at')

# print('''Selamat malam, 
#       hari ini hari jum"at''')

# print("""Selamat malam, 
#       hari ini hari jum'at""")

# ### Tipe data Numerik (Float - Integer) ==> Operasi Matematis
# print(9)

# print(9*8)

# print(type(9))  ## mengetahui tipe data
# ## Untuk mengetahui tipe data, gunakan fungsi 
# # type(data)
# ## Float - Bil. desimal
# print(9.5)

# ### Boolean
# print(True)
# print(False)

# # ## Variabel
# # - Suatu tempat untuk menyimpan data dan diberi nama 
# # - Case sensitive : Variabel kopi berbeda dengan variabel Kopi 
# # - Tidak bisa diawali dengan angka ==> 21nama, nama21
# # - Tidak bisa menggunakan karakter spesial (@$%^&*(), dll)
# # - Tidak bisa ada spasi 
# # - Tidak bisa menggunakan reserved words (kata kunci yg dipakai python)
# # - Tidak perlu mendefinisikan tipe data untuk variabel
# # - Pemberian nama bisa menggunakan kombinasi huruf kapital (A-Z), huruf kecil (a-z), angka (0-9) dan underscore(_)
# # Nama_siswa21
# # PRODI_s1
# # - pemberian nama variabel bebas, selama mengikuti aturan yg berlaku.

# # # Menggunakan Operator Assignment (=)

# nilai_SEMESTER1 = 20
# name = "Jack"
# sisi = 50

# luaspersegi = sisi * sisi 

# print(nilai_SEMESTER1)
# print(sisi)
# print(luaspersegi)
# sisi = 'Jakarta'
# print(sisi)

# Andre memelihara ayam dan kambing, jumlah ayam dan kambing andre ada 13 ekor,
# Jumlah kaki ayam dan kambing andre ada 32,
# Berapa jumlah masing-masing ayam andre dan kambing andre?
# Output :
# Andre memiliki ayam ... ekor dan kambing ... ekor

# x adalah ayam
# y adalah kambing 

# x + y = 13
# 2*x + 4*y = 32

# x = 13 - y

# 2 * (13 - y) + 4 * y = 32
# (2 * 13) - (2 * y) + (4 * y) = 32
# - (2 * y) + (4 * y) = 32 - (2 * 13)
# (-2 + 4) * y = 32 - (2 * 13)
# (4 - 2) * y = 32 - (2 * 13)
y = (32 - (2 * 13)) / (4 - 2)

JumlahKaki = 32
JumlahTernak = 15
KakiAyam = 2
KakiKambing = 4

Kambing = (JumlahKaki - (KakiAyam * JumlahTernak)) / (KakiKambing - KakiAyam)
Ayam = JumlahTernak - Kambing

print(Kambing)
print(Ayam)