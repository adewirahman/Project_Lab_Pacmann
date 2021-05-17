import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os
import random

# Susenas 2012
sus12_ki = pd.read_csv('/home/ade/Documents/Project_Lab_Pacmann/susenas12/sn12_ki.csv')
sus12_kr = pd.read_csv('/home/ade/Documents/Project_Lab_Pacmann/susenas12/sn12_krt.csv')

# Susenas 2013
sus13_ki = pd.read_csv('~/Documents/Project_Lab_Pacmann/susenas13/sn13_ki.csv')
sus13_kr = pd.read_csv('~/Documents/Project_Lab_Pacmann/susenas13/sn13_krt.csv')

# Susenas Modul Konsumsi
sus13_m41 = pd.read_csv('~/Documents/Project_Lab_Pacmann/susenas13/sn13_m41.csv')
sus12_m41p1 = pd.read_csv('/home/ade/Documents/Project_Lab_Pacmann/susenas12/sn12_m41p1.csv') # part 1 susenas 2012

# Poverty Line Susenas 2013
poverty_line = pd.read_csv("~/Documents/Project_Lab_Pacmann/susenas13/pov_line.csv")
poverty = pd.read_csv("~/Documents/Project_Lab_Pacmann/susenas13/poverty.csv")

"""
Eksplor perilaku kunjungan ke nakes bila ada keluhan kesehatan

- B5R1A

Apakah dalam 1 bulan terakhir mempunyai keluhan kesehatan seperti di bawah ini? (Bacakan dari a s.d. h)
[Isikan kode 1 bila ada, kode 2 bila tidak ada]

- B5R4A
Apakah pernah mengobati sendiri dalam 1 bulan
terakhir?
1. Ya
2. Tidak  [R.5]

Jenis obat/cara pengobatan yang digunakan:
[Isikan kode 1 bila ya, kode 2 bila tidak]

- B54RB1. Tradisional
- B54RB2. Modern
- B54RB3. Lainnya
"""
print(sus12_ki['B5R1A'].value_counts())
print(sus12_ki['B5R4A'].value_counts())
print(sus12_ki['B5R4B1'].value_counts())
print(sus12_ki['B5R4B2'].value_counts())
print(sus12_ki['B5R4B3'].value_counts())

"""
Kunjungan ke Faskes

Berapa kali berobat jalan selama 1 bulan terakhir:
[Isikan frekuensi berobat jalan untuk setiap fasilitas]

- B5R6A ==	RS pemerintah
- B5R6B	==  RS Swasta
- B5R6C	==  Praktek Dokter/poliklinik
- B5R6D	==  Puskesmas/pustu
- B5R6E	==  Praktek nakes
- B5R6F	==  Praktek batra
- B5R6G	==  Dukun bersalin
- B5R6H	==  Lainnya
"""
# Jumlah berobat ke RS Pemerintah
print(sus12_ki['B5R6A'].value_counts())

# Jumlah berobat ke RS Swasta
print(sus12_ki['B5R6B'].value_counts())

# Jumlah yang pergi ke praktek dokter/poliklinik
print(sus12_ki['B5R6C'].value_counts())

"""
Perilaku Penggunaan Kontrasepsi
1. sedang menggunakan KB,
2. Tidak menggunakan KB lagi
3. Tidak pernah menggunakan KB
"""
print(sus12_ki['B5R35'].value_counts())
sus12_ki['B5R35'].describe()

# kenapa jumlah NaN lebih tinggi dibanding count ya?
print(sus12_ki['B5R35'].isna().values.sum() / sus12_ki['B5R35'].count())
print(sus12_ki['B5R35'].count() / sus12_ki['B5R35'].isna().values.sum())

"""
Butir metode penggunaan KB:

1. MOW/tubektomi
2. MOP/vasektomi
3. AKDR/IUD/spiral
4. Suntikan KB
5. Susuk KB/norplan/implanon/alwalit
6. Pil KB
7. Kondom/karet KB
8. Intravag/tisue
9. Kondom wanita / menstrual cup(?)
10. Cara tradisional
"""
sus12_ki['B5R36'].count()
sus12_ki['B5R36'].value_counts()

# Kok yang count lebih rendah dibanding NaN ya?
print(sus12_ki['B5R36'].isna().values.sum()/sus12_ki['B5R36'].count())
print(sus12_ki['B5R36'].count() / sus12_ki['B5R36'].isna().values.sum())

"""
Bagi yang tidak menggunakan KB, apa masih ingin mempunyai anak
1. Ya, segera (< 2 tahun)
2. Ya, kemudian ( ≥ 2 tahun)
3. Tidak
"""
sus12_ki['B5R37'].value_counts()

# Kenapa jumlah count lebih rendah dibanding NaN ya?
print(sus12_ki['B5R37'].count() / sus12_ki['B5R37'].isna().values.sum())
print(sus12_ki['B5R37'].isna().values.sum() / sus12_ki['B5R37'].count())

"""
Alasan utama tidak ber-KB:
1. Alasan fertilitas (mandul, menopause, puasa
kumpul, tradisi, ingin punya anak) # jujur yang ini ambigu soalnya banyak banget yang dimasukkin
2. Tidak setuju KB
3. Tidak tahu alat/cara KB
4. Takut efek samping alat/cara KB
5. Tidak tahu
6. Lainnya (................................................................)

Lucunya yang terbanyak di sini Alasan fertilitas sama Lainnya, susah dapat insight di sini.

Kalo mandul sih bisa liat umur, entahlah kalo yang lain? Still wanna give this one a go?
"""
print(sus12_ki['B5R38'].describe())
print(sus12_ki['B5R38'].value_counts())

# baru ini yang perbandingan nya NaN lebih kecil dibanding count
print(sus12_ki['B5R38'].count() / sus12_ki['B5R38'].isna().values.sum())
print(sus12_ki['B5R38'].isna().values.sum() / sus12_ki['B5R38'].count())
