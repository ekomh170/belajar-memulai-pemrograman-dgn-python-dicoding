# Tipe Data Collection = Tuple

# Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya, tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung “()“ dan setiap elemen di dalamnya dipisahkan dengan koma.
x = (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""


# Pada kode di atas, Anda dapat lihat bahwa nilai yang diapit tanda kurung “()” akan dianggap sebagai tuple oleh program. Anda juga dapat melakukan indexing dan slicing pada tuple sama seperti list. 
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

""" 
Output:
program
(5, 'program', (1+3j))
"""

# Pada kode di atas, Anda mengambil string “program” yang berada pada indeks 1 dan menampilkan nilai dari indeks 0 hingga indeks 2 (ingat, bersifat eksklusif).


# Tuple bersifat immutable yang artinya tidak dapat diubah.
# x = (5, 'program', 1+3j)
# x[1] = 'Dicoding'

"""
Output:
'tuple' object does not support item assignment
"""

# Pada kode di atas, Anda mencoba mengubah string “program” menjadi “Dicoding”,  tetapi menghasilkan error karena tuple bersifat immutable.

