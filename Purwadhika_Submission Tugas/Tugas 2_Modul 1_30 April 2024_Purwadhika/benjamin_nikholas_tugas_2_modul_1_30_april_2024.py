# -*- coding: utf-8 -*-
"""Benjamin Nikholas_Tugas 2_Modul 1_30 April 2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RqjUQVPCLE6FTnYUgl0nNS1VjB8UNcaJ

> Benjamin Nikholas

> Data Science / JCSDOL-014

> Modul 1 - Tugas 2

> 30 April 2024
---
---

#5

> Input :

Masukkan Jumlah Hari : ....

> Output nya :

Nyatakan Jumlah hari tersebut ke dalam (Hasil dalam bentuk 2 digit)
 .... Tahun .... Bulan ... Minggu .... Hari
"""

input_hari = int(input('Masukkan jumlah hari :'))

tahun = input_hari // 365
sisa_hari = input_hari % 365
bulan = sisa_hari // 30
sisa_hari = sisa_hari % 30
minggu = sisa_hari // 7
hari = sisa_hari % 7

print(f'{tahun} Tahun {bulan} Bulan {minggu} Minggu {hari} Hari')

"""#6

Hitung BMI (Body Mass Index)

Rumus BMI = massa(Kg) / tinggi(meter) pangkat 2

> Input :

 Masukkan Tinggi Badan (dalam cm)

 Masukkan Berat Badan (dalam Kg)

> Output :

 Tinggi ... (meter), Berat ... (Kg), BMI ....(Nilai BMI) dan anda termasuk .... (Sesuai Ketentuan)

> Ketentuan :

 * BMI < 18.5 ==> Berat Badan Kurang
 * 18.5 - 24.9 ==> Berat Badan Ideal
 * 25 - 29.9 ==> Berat badan berlebih
 * 30 - 39.9 ==> Berat badan sangat berlebih
 * BMI >= 40 ==> Obesitas

> Kondisi:
 * Berat badan Maksimal 300 Kg
 * Tinggi Maksimal 250 cm

 ==> Keluar Notifikasi ==> Nilai yg anda Masukkan DiLuar Jangkauan
 * Paling Kecil 0

 ===> Kelaur Notifikasi ==> Tidak Menerima Nilai Negatif

"""

while True:
    tinggi = float(input('Masukkan Tinggi Badan (dalam cm): '))/100

    if tinggi > 2.5:
      print('Nilai yang ada masukkan diluar jangkauan')
    elif tinggi <= 0:
      print('Tidak menerima nilai negatif')
    else:
      break

while True:
    berat = float(input('Masukkan Berat Badan (dalam Kg): '))

    if berat > 300:
      print('Nilai yang ada masukkan diluar jangkauan')
    elif berat <= 0:
      print('Tidak menerima nilai negatif')
    else:
      break

bmi = berat / (tinggi ** 2)
kategori = ''
if bmi < 18.5:
    kategori = 'Berat Badan Kurang'
elif 18.5 <= bmi < 25:
    kategori = 'Berat Badan Ideal'
elif 25 <= bmi < 30:
    kategori = 'Berat Badan Berlebih'
elif 30 <= bmi < 40:
    kategori = 'Berat Badan Sangat Berlebih'
else:
    kategori = 'Obesitas'

print(f'Tinggi: {tinggi:.2f} meter, Berat: {berat} Kg, BMI: {bmi:.2f}, Anda termasuk {kategori}')

"""#7

> Input :

 Masukkan Nilai :

> Output :

 Nilai Anda ... dan Anda ... (Sesuai Ketentuan)

> Kondisi:
 * Nilai Paling tinggi 100 ==> Keluar Notifikasi : Nilai yg anda Masukkan diLuar Jangkauan
 * Nilai Paling rendah 0 ==> Kelauar Notifikasi : Tidak menerima Nilai Negatif
 * Nilai Berupa Float

> Ketentuan:
 * 90 Keatas : Grade A
 * 85 Keatas : Grade A-
 * 80 Keatas : Grade B
 * 75 Keatas : Grade B-
 * 70 Keatas : Grade C
 * 65 Keatas : Grade D
 * Dibawah 65 Tetapi Diatas 40 :Perlu Remedial
 * Dibawah 40 : Tidak Lulu
"""

nilai = float(input("Masukkan Nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai yang Anda masukkan di luar jangkauan.")
elif nilai >= 90:
    print(f"Nilai Anda {nilai} dan Anda Grade A")
elif nilai >= 85:
    print(f"Nilai Anda {nilai} dan Anda Grade A-")
elif nilai >= 80:
    print(f"Nilai Anda {nilai} dan Anda Grade B")
elif nilai >= 75:
    print(f"Nilai Anda {nilai} dan Anda Grade B-")
elif nilai >= 70:
    print(f"Nilai Anda {nilai} dan Anda Grade C")
elif nilai >= 65:
    print(f"Nilai Anda {nilai} dan Anda Grade D")
elif nilai > 40:
    print(f"Nilai Anda {nilai} dan Anda Perlu Remedial")
else:
    print(f"Nilai Anda {nilai} dan Anda Tidak Lulus")

