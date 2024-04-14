# Jenis-Jenis Ekspresi
# Pada dasarnya, jenis-jenis ekspresi dibagi menjadi dua. Pertama adalah menurut jumlah operan (arity) dari operator dan kedua adalah menurut tipe data yang dihasilkan.

# 1. Ekspresi Menurut Arity dari Operator
# Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), perkalian (*), pembagian (/), perpangkatan (**), lebih kecil dari (<), lebih kecil dari sama dengan (<=), lebih besar dari (>), lebih besar dari sama dengan (>=), modulus (%), sama dengan (==), dan tidak sama dengan (!=).

# Namun, ekspresi uner adalah jenis ekspresi yang memiliki bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), decrement (x-=1), dan negasi (not x).

# Anda sudah melihat penerapan ekspresi biner pada submodul sebelumnya dan berikut adalah penerapan ekspresi uner.

"""
1. Variabel a bernilai True, jika kita memberikan ekspresi "not a" yang artinya "not True", hasil yang didapat adalah False. 
2. Baik increment maupun decrement, keduanya adalah pola yang sama untuk menambahkan dan mengurangi suatu variabel dengan jumlah tetap.
        A. a += 1 memiliki tujuan yang sama dengan struktur a = a + 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi penjumlahan "1+1". Inilah alasan ia disebut dengan increment yang artinya kenaikan.
        
        B. Decrement dapat dijelaskan sebagai a -=1, memiliki tujuan yang sama dengan struktur a = a - 1. Jika diasumsikan variabel a bernilai 1, seolah-olah kita melakukan operasi pengurangan "1-1".
"""

a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1
print(c)

d = 10
print(-d)

"""
Output:
False
5
7
-10
"""


# 2. Ekspresi Menurut Tipe Data yang Dihasilkan
# Sebagaimana judulnya, jenis-jenis ini adalah ekspresi yang dikelompokkan berdasarkan tipe data yang dihasilkan. Mari kita bedah satu per satu.
"""
1. Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
2. Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
3. Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.
"""

print(2+2)
print(3<10)
print(True or False)

"""
Output:
4
True
True
"""