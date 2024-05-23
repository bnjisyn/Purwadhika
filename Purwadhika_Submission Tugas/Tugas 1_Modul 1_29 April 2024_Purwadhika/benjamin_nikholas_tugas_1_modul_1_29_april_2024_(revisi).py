# -*- coding: utf-8 -*-
"""Benjamin Nikholas_Tugas 1_Modul 1_29 April 2024 (revisi).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LvK9PeECM8GrF1MLv41CZM4paav22h00

> Benjamin Nikholas

> Data Science / JCSDOL-014

> Modul 1 - Tugas 1

> 30 April 2024
---
---

#1

Andre memelihara ayam dan kambing, jumlah ayam dan kambing andre ada 13 ekor,
Jumlah kaki ayam dan kambing andre ada 32,

Berapa jumlah masing-masing ayam andre dan kambing andre?

> Output :

Andre memiliki ayam ... ekor dan kambing ... ekor
"""

total_hewan = 13
total_kaki = 32

# x = jumlah_ayam
# y = jumlah_kambing = total_hewan - jumlah_ayam

x = 0
while x <= total_hewan:
    y = total_hewan - x

    # Fungsi
    predict = 2*x + 4*y

    if predict == total_kaki:
        break
    x += 1

print(f'Andre memiliki ayam {x} dan kambing {y} ekor')

"""#2

Jumlah usia budi dan ayahnya sekarang adalah 50 tahun.
empat tahun lalu, usia ayah budi enam kali usia budi.

Berapa usia ayah budi dan usia budi saat ini.

> Output :

Usia ayah saat ini adalah ... tahun dan usia budi saat ini adalah .. tahun
"""

total_usia = 50

# x = usia Budi saat ini
# y = usia Ayah saat ini = usia budi - total_usia

x = 0
while x <= total_usia:
    y = total_usia - x

    # Fungsi
    y_4_thn = y - 4
    x_4_thn = x - 4

    # Check
    if y_4_thn == 6 * x_4_thn:
        break
    x += 1

print(f'Usia ayah saat ini adalah {y} tahun dan usia budi saat ini adalah {x} tahun')

"""#3

> Input :

Masukkan kalimat : .....

Masukkan karakter (Huruf atau angka) : ....

> Output :

Jumlah karakter ... di dalam kalimat .... adalah ...

* Tidak case sensitive
"""

sentence = input('Masukkan kalimat: ')

char = input('Masukkan karakter (Huruf atau angka): ')

num = 0
for i in sentence.lower():
    if i == char.lower():
        num += 1

print(f'Jumlah karakter "{char}" di dalam kalimat "{sentence}" adalah {num}')

"""#4

> Input :

Masukkan kalimat : .....

Masukkan huruf vokal : …

> Output :

* semua huruf vokal menjadi sesuai input huruf vokal
* tidak case sensitive
* case disesuaikan dengan kalimat
"""

words = set('aeiouAEIOU')

def replace_words(sentence, word):
    result = ''

    for i, char in enumerate(sentence):
        if char in words:
            if sentence[i].isupper():
                result += word.upper()
            else:
                result += word
        else:
            result += char

    return result

def get_valid_word():
    while True:
        word = input('Masukkan huruf vokal: ')
        if word in words:
            return word
        else:
            print('Huruf yang dimasukkan bukan huruf vokal. Silakan coba lagi.')

# User input
sentence = input('Masukkan kalimat: ')
word = get_valid_word()

print(f'Kalimat hasil: {replace_words(sentence, word)}')

