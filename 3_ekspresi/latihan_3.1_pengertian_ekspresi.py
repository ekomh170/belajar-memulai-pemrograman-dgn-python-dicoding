# Pengertian Ekspresi
"""
"4x-7" merupakan ekspresi, sedangkan "4x", "7", dan "5" merupakan suku bilangan. Apabila kita mengingat kembali, operasi pada matematika ataupun pemrograman merupakan suatu proses yang dilakukan untuk mendapatkan hasil nilai tertentu. Jadi Ekspresi pada pemrograman merupakan kombinasi dari satu atau lebih variabel, konstanta, operator, dan fungsi yang bermakna untuk menghasilkan suatu nilai dalam suatu tipe tertentu.

Struktur umum ekspresi yang sering dijumpai adalah <operan1> <operator> <operan2>. Namun, perlu Anda ketahui bahwa struktur umum tersebut merupakan struktur ekspresi biner (jenis ekspresi menggunakan dua operan). Mari bedah struktur tersebut lebih dalam.

1. Operan dapat berupa nilai, variabel, konstanta, atau ekspresi lain.
2. Operator merupakan suatu fungsi standar yang disediakan dalam bahasa pemrograman untuk melakukan beberapa hal dasar, seperti perhitungan aritmetika, logika, dan relasional. Contohnya adalah penjumlahan (+), pengurangan (-), perkalian (*), modulus (%), dan sebagainya.
"""

# Di bawah ini, penerapan ekspresi pada Python.

x = 10
y = 2
result = x - y

print(result)

"""
Output:
8
"""


# Lantas, mengapa kita harus paham terlebih dahulu mengenai ekspresi? Sebab, ini merupakan dasar dalam pemrograman untuk melakukan semua perhitungan dan manipulasi data. 

# Salah satunya adalah melakukan penggabungan dan replikasi pada list.

angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf

print(gabung)

"""
Output:
[2, 4, 6, 8, 'P', 'Y', 'T', 'H', 'O', 'N']
"""

# Pada kode di atas, Anda menggabungkan dua list dengan menggunakan operator penjumlahan (+). Namun, pada kode di bawah ini, Anda mereplikasi list dengan menggunakan operator perkalian (*).

learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

print(replikasi)

"""
Output:
['P', 'Y', 'T', 'H', 'O', 'N', 'P', 'Y', 'T', 'H', 'O', 'N']
"""

# Pada kedua kode di atas, Anda telah melakukan operasi replikasi dan duplikasi pada list menggunakan ekspresi. Sekarang, mari kita pelajari lebih dalam mengenai berbagai jenis ekspresi.