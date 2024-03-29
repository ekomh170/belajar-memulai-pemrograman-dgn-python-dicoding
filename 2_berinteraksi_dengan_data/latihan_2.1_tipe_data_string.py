# Tipe Data String

# Jenis String single quote (‘’)
x = 'Dicoding'
print(type(x))

"""
Output: 
<class 'str'>
"""

# Jenis String double quote (“”)
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""

# String merupakan urutan karakter yang setiap karakternya memiliki indeks. Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing. Perlu diingat bahwa indeks selalu dimulai dari 0.
x = 'Dicoding'
print(x[0])

""" 
Output:
D
"""

# Namun, Anda tidak dapat mengubah substring di dalamnya. Ini dikarenakan string pada Python bersifat immutable.
# x = 'Dicoding'
# x[0] = 'F'

""" 
Output:
TypeError: 'str' object does not support item assignment
"""

# Anda dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing. Slicing memungkinkan Anda untuk mengakses beberapa karakter dari string. Sintaksnya adalah [start:stop:step]. Perlu diingat bahwa karakter pada indeks ke-“stop” tidak akan diikutsertakan.
x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""


# Anda dapat menampilkan teks/string berdasarkan input dari pengguna dengan berbagai cara. Perhatikan metode di bawah ini dan jalankan kodenya menggunakan IDE atau notebook Anda.
# Formatted String

name = "Eko Muchamad Haryono"
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Eko Muchamad Haryono
"""

# %-formatting
name = "Eko Muchamad Haryono"
print("Nama saya %s" % (name))
 
"""
Output: 
Nama saya Eko Muchamad Haryono
"""

# str.format()
name = "Eko Muchamad Haryono"
print("Nama saya {}".format(name))
 
"""
Output: 
Nama saya Eko Muchamad Haryono
"""
