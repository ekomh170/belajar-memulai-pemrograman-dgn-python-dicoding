# Tipe Data Collection = List

# 1. List
# Melakukan inisialisasi list pada Python cukup mudah, yakni menggunakan kurung siku “[]” dan setiap elemennya dipisahkan dengan koma. Berikut adalah implementasi list pada Python.
x = [1, 2.2, 'Dicoding']
print(type(x))

"""
Output: 
<class ‘list’>
"""


# Setiap data atau elemen dalam list memiliki indeks yang selalu dimulai dari 0. Anda dapat mengakses setiap indeks pada list dengan metode indexing. 
x = [1, 'Dicoding', True, 1.0]

print(x[2])

""" 
Output:
True
"""

# List Python bersifat mutable yang artinya nilai di dalamnya dapat diubah.

x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""

# Konsep indexing merujuk kepada pengambilan data dalam Python berdasarkan indeksnya. Beberapa cara untuk melakukan indexing sebagai berikut.
# Pada dua sintaks pertama, Anda memerintahkan untuk menampilkan indeks ke-0 dan indeks ke-2. Selanjutnya, dua sintaks terakhir memerintahkan untuk menampilkan indeks terakhir dan indeks ke-3 dari terakhir. 

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


"""
Output:
laptop
mouse
microphone
keyboard
"""


# konsep slicing list
# sequence[start:stop:step]
# Berikut adalah implementasi slicing pada Python.

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""

# Pada sintaks pertama, Anda memerintahkan untuk mengambil data dari indeks ke-0 hingga indeks ke-4 dengan setiap elemen ke-2 dan kelipatannya akan dilewati. Pada sintaks kedua, Anda memerintahkan untuk menampilkan data dari indeks ke-1 hingga terakhir. Pada sintaks ketiga, Anda memerintahkan untuk menampilkan data dari indeks ke-0 hingga indeks ke-2 (ingat, bersifat eksklusif).
