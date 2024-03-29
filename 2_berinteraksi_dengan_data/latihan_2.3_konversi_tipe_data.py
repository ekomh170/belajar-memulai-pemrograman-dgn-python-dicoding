# # Konversi antara Tipe Data

# Setelah mengetahui berbagai tipe data pada Python, Anda pun dapat melakukan konversi antar tipe data dengan menggunakan beberapa fungsi.
# Fungsi merupakan blok kode yang dapat dipanggil untuk melakukan tugas tertentu. Anda akan mempelajari fungsi lebih detail pada modul subprogram. Saat ini, Anda cukup memahami bahwa fungsi di bawah ini dapat melakukan operasi terhadap list, set, dan string.

# 1. Konversi Integer ke Float
print(float(5))

"""
Output:
5.0
"""
# Untuk melakukan konversi dari integer ke float cukup menggunakan fungsi float() dengan memasukkan nilai integer di dalamnya.


# 2. Konversi Float ke Integer
print(int(5.6))
print(int(-5.6)) 

""" 
Output:
5
-5
"""
# Untuk melakukan konversi dari float ke integer cukup menggunakan fungsi int() dengan memasukkan nilai float di dalamnya.


# 3. Konversi dari-dan-ke String
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""
# Kode di atas merupakan berbagai fungsi untuk mengonversi dari-dan-ke string. Jika ingin melakukan konversi ke string, Anda cukup menggunakan fungsi str().

# Kode di atas menghasilkan error karena 1p dianggap tidak valid.
print(int("1p"))

"""
Output:
ValueError: invalid literal for int() with base 10: '1p
"""
# Perlu Anda perhatikan bahwa konversi dari-dan-ke string akan melalui pengujian dan dipastikan validitasnya. Jika pengujian dan validitasnya gagal, error akan dihasilkan.


# 4. Konversi Kumpulan Data
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))

"""
Output:
{1,2,3}
(5,6,7)
['h','e','l','l','o']
"""
# Untuk melakukan konversi kumpulan data dari-dan-ke set/list/tuple, Anda cukup menggunakan fungsi dari tipe data yang diinginkan. Misalnya, set(), tuple(), dan list() seperti pada kode di atas.


# 5. Konversi ke Dictionary
print(dict([[1,2],[3,4]]))

"""
Output:
{1:2, 3:4}
"""
# Pada kode di atas terdapat list berisi dua list yang berisi pasangan nilai, yakni [1,2] dan [3,4]. Lalu, list tersebut diubah menjadi dictionary dengan nilai 1 dan 3 sebagai key serta nilai 2 dan 4 sebagai value.

# Konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary.
print(dict([(3,26),(4,44)]))

"""
Output:
{3:26, 4:44}
"""
# Pada kode di atas terdapat list yang berisi dua tuple dengan pasangan nilai, yakni (3,26) dan (4,44). Setelah diubah menjadi dictionary, nilai 3 dan 4 menjadi key, sedangkan nilai 26 dan 44 menjadi value.
