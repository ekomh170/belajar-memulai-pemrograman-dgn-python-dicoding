# Tipe Data Collection = Dictionary
# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut.
"""
1. Setiap elemen pasangan key-value dipisahkan dengan koma (,).
2. Key dan value dipisahkan dengan titik dua (:).
3. Key dan value dapat berupa tipe variabel/objek apa pun.
"""


# x = { 'name': 'Eko Muchamad Haryono', 'age': 20, 'isMarried': False }

# print(type(x))

"""
Output:
<class 'dict'>
"""
# Pada kode di atas, sintaks yang diapit tanda kurawal “{}” dan memiliki pasangan key-value akan dianggap sebagai data bertipe dictionary oleh program.

x = { 'name': 'Eko Muchamad Haryono', 'age': 20, 'isMarried': False }

print(x ['name'])

""" 
Output:
Eko Muchamad Haryono
"""
# Dalam kode di atas, Anda mengambil data pada dictionary dengan memanggil key yang ada.

# Beberapa hal lain terkait dictionary dapat dilihat pada poin-poin berikut.
# 1. Menambah Data pada Dictionary
x = { 'name': 'Eko Muchamad Haryono', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"

print(x)

"""
Output:
{'name': 'Eko Muchamad Haryono', 'age': 20, 'isMarried': False, 'Job': 'Web Developer'}
"""
# Untuk menambahkan data pada Dictionary, Anda cukup memasukkan key dan value-nya seperti pada contoh kode di atas, yakni “x[‘Job’] = ‘Web Developer’”.


# 2. Menghapus Data pada Dictionary
x = { 'name': 'Eko Muchamad Haryono', 'age': 20, 'isMarried': False }
del x['isMarried']

print(x)

"""
Output:
{'name': 'Eko Muchamad Haryono', 'age': 20}
"""
# Anda dapat menghapus data pada Dictionary dengan menggunakan sintaks “del”. Pada kode di atas, data “isMarried” dihapus.


# 3. Mengubah Data pada Dictionary
x = { 'name': 'Eko Muchamad Haryono', 'age': 20, 'isMarried': False }
x ['name'] = "Dicoding"

print(x)

"""
Output:
{'name': 'Dicoding', 'age': 20, 'isMarried': False}
"""
# Untuk mengubah value pada Dictionary, Anda dapat melakukannya dengan mengakses key-nya dan lakukan inisialisasi variabel dengan nilai baru. Pada kode di atas, data “name” diubah dari “Eko Muchamad Haryono” menjadi “Dicoding”.
