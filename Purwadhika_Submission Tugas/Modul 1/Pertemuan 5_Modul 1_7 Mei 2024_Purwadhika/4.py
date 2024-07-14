# masukkan range awal : 5
# masukkan range akhir : 20

# 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# 5 + 7  + 9 + 11 + 13 + 15 + 17 + 19 = ...
# 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20 = ...

# ### Data Structure
# - Data Iterables
# - Berisi Lebih dari 1 value 
# - List, Tuple, Set, Dictionary 
# - Bisa berisi data primitif (string - Integer - Float) atau data structure

# ## LIST

# menggunakan => [ ]

# List_A = [data1, data2, data3, dst]

# ## Mengubah tipe data struktur
# list(data) ==> mengubah data menjadi bertipe List 
sentence = "Hari ini hari selasa"
data = sentence.split(' ', 1)
# data = sentence.split('ini')
# print(data)
# print(type(data))
        # 0           1       2       3          4        5       6
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
#       -7         -6         -5        -4       -3    -2     -1
# CRUD => Create - Read - Update - Delete

### Cara akses data/elemen dalam List ==> READ
# - Menggunakan Indexing 
# - Indexing ==> Urutan angka ==> yg dimulai dari NOL (jika dari kiri - kanan) atau -1 (jika dari kanan - kiri)
# - Angka Berupa Integer
# - Maksimal Index adl jumlah elemen - 1
# Basic Syntax :
# NamaList[Index]

print(hari[0])
print(hari[-5])
print(hari[2])
## untuk mengetahui Jumlah elemen dalam List
print(len(hari))

## melihat isi keseluruhan List
print(hari)

# for i in hari:
#     print(i)

Text = 'selasa'

print(Text[0])
print(Text[2])

### Untuk mengetahui Index suatu elemen dalam List
# Basic Syntax :
# NamaList.index(data)
print("=" * 50)
print(hari.index("minggu"))
print(hari[6])
print(hari[2*3])
print(hari[10-4])
a = 6
print(hari[hari.index("minggu")])

print(hari[a])
### Di bagian kurung siku, bisa berisi fungsi/operasi yg menghasilkan Nilai INTEGER, selama hasil dalam Jangkauan

## Slicing
# - Akses beberapa elemen List sekaligus
# basic syntax nya:
# NamaLISt[START : END : STEP]

# STEP jika tidak ditentukan value nya maka menggunakan nilai default
# STEP deafult ==> +1

# [START : END]
# berlaku
# Start ==> Inclusive ==> Index yg ditentukan akan diakses
# End ==> Exclusive => Index yg akan diakses END - 1 (Jika Increment) & END + 1 (Jika Decrement)

print(hari[1:4])  # akan mengakses index 1 (inclusive), dan Index 4 - 1 (Karna exclusive & Increment)
print(hari[3:])  ## akan mengakses dari Index 3 hingga paling akhir
print(hari[:4])  ## akan mengakses index paling awal hingga index 4-1 (3)
print(hari[:-5: -1])
# 0 + 1
# 1 + 1
### Cara Menambahkan Data/Elemen baru ke dalam LISt ---> CREATE

# ## Append
# Basic Syntax :
# NamaList.append(data)

# ## Extend
# Basic Syntax :
# NamaList.extend(data)
print("=" * 50)
nama = ["andi", "beni", "doni"]
nilai = [88, 96, 78]
print(nama)
nama.append('fitri')
print(nama)
print("=" * 50)
nama.extend('Jeki')
print(nama)

nama.append(90)
print(nama)

# nama.extend(98)  ## Error
print(nama)
print("=" * 50)
nama.append(nilai)
print(nama)
print("=" * 50)
nama.extend(nilai)
print(nama)

# ## Extend 
# - Data yg akan ditambahkan harus berupa data iterables (string & atau data structure)
# - Akan error jika menambahkan data Non Iterables - contohnya Integer
# - Data yg ditambahkan, per ELEMEN dari data iterables
# - Data yg ditambahkan Otomatis berada di Index paling akhir (Paling kanan)

# ### Append
# - data yg ditambahkan bisa berupa data iterables maupun data non-iterables 
# - data iterables yg ditambahkan akan ditambahkan sebagai data tunggal
# - data iterables tidak ditambahkan per elemen
# - Data yg ditambahkan Otomatis berada di Index paling akhir (Paling kanan)


# ## Menambahkan data di index tertentu

# basic syntax nya
# NamaList.insert(Index, data)
print("=" * 50)
print(hari)

hari.insert(2, 'monday')
print(hari)

#### Mengupdate Elemen dalam List --- UPDATE
# basic syntax :
# NamaList[index] //--data yg akan diubah/diupdate--// = Data Baru


# Ubah -> Rabu menjadi Wednesday
print(hari.index('rabu'))
hari[3] = 'wednesday'
print(hari)

## Menghapus elemen dari List -- DELETE

## Menghapus berdasarkan data
# - Remove
# basic syntax:
# namaList.remove(data)

## menghapus monday
hari.remove('monday')
print(hari)

### Menghapus berdasarkan Index 
# - pop 
# Basic syntax :
# namaList.pop(index)
# - Jika index tidak ditentukan, menggunaklan default
# Default nya adalah Index paling akhir

## Menghapus Jumat
hari.pop(4)
print(hari)

## menghapus index terakhir
hari.pop()
print(hari)