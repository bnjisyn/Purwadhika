## Data Analysis using Numpy - Pandas
# Numpy => Numerical Python

# import numpy 

# print('Installed')

# # python3 -m pip install numpy
# ==> Bertipe data Array
# - Vector
# - Matrix

# [1, 2, 3, 4, 5] ==> Vector
# [1,2,3,4,5, 'Malam']

# [
#     [1,2,3],
#     [4,5,6]
# ] ==> Matrix

# [5] ==> Scalar

# # Memanggil/Menggunakan Package/Library Numpy 
# List ==> Tipe/Jenis data di dalam list bisa beragam
# Array ==> Hanya 1 jenis data 

import numpy as np

## Membuat Array
a = [1,2,3,4,5] ## List Basic

# Integer, String, Float, List, Dictionary
b = np.array(a)

# print(a, 'List')
# print(b, 'Array')

# print(type(a))
# print(type(b)) ## numpy.ndarray
# n ==> Jumlah
# d ==> Dimension/Dimensi

# ## Operasi Math Basic
# C = a + [2] ## list basic - Error -> List tidak bisa dijumlahkan dg Integer
# ### Menambahkan Elemen 2 ke dalam List 1 (sama seperti Extend)
# print(C)

# D = b + 2 ## Menambahkan 2 ke setiap elemennya

# print(D)

# C = a * 3  ### isi list, akan di duplikasi sebanyak 3X
# print(C)
# D = b * 3 ## setiap elemen akan dikalikan 3
# print(D)

# Element Wise ==> Operasional Math akan dieksekusi ke setiap elemen dalam Array

### Membuat Array dengan Range
# range(10) ## range built in python
# np.arange(10) ## arange ==> Range dari Numpy


# for i in range(1, 10.7, 2):
#     print(i)

# print('=' * 50)

# for i in np.arange(1.5, 10.8, 2.5):
#     print(i)

# ## Perbedaan paling utama antara built in range() python, dg arange() numpy 
# - range hanya menerima Nilai INTEGER
# - arange dapat menerima nilai FLOAT, bukan hanya Integer

# for i in np.arange(1, 5.8, 0.7):
#     print(i)
#     arange() ==> Bisa menerima FLOAT untuk start, End maupun STEP 

# ### Membuat Array dg Linear Space 
# c =np.linspace(0, 100, 7)
# print(c)

# ### Linspace memiliki syntax
# linspace(Start, End, Jumlah)
# Start & ENd ==> Keduanya Inclusive ==> Pasti akan ditampilkan
# Start & End ==> Bisa integer maupun Float 
# Jumlah ==> Harus Integer ==> Jumlah angka yg akan digenerate oleh Numpy

## membuat array dg Logaritmik space
d = np.logspace(5, 0, 6)
print(d)

## Logspace 
logspace(Start, End, Jumlah) ## STEP nya akan menyesuaikan dengan start dan End
Start dan End menunjukkan Pangkat dari 10
np.logspace(5, 0, 6)
==> akan menghasilkan 6 angka
mulai dari 10 ** 5 hingga 10 ** 0
[10**5, 10**4, 10**3, 10**2, 10**1, 10**0]