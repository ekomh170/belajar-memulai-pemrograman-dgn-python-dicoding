# Tipe Data Collection = Set
# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.
# Tidak sama seperti list, dalam set kita tidak bisa melakukan indeksing karena set tidak memiliki indeks. Hal ini merujuk pada definisi nya yang menyatakan bahwa set merupakan kumpulan item tanpa urutan.

x = {1,2,7,2,3,13,3}
print(x[0])

"""
Output:
'set' object is not subscriptable
"""
# Pada kode di atas, program mengembalikan output 'set' object is not subscriptable karena setiap nilai dalam set tidak memiliki indeks sehingga tidak bisa dilakukan indexing.


x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""
# Pada kode di atas, Anda dapat melihat bahwa nilai yang diapit tanda kurawal “{}” akan dianggap sebagai set oleh program dan nilai duplikat di dalamnya akan dihapus. Pada kode di atas pun, nilai 3 dan 2 yang duplikat telah dihapus. 


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""
# Pada contoh di atas, kita melakukan operasi union atau penggabungan dua variabel bertipe data set, yakni variabel set1 dan variabel set2 dengan menggunakan method “.union()”. Hasilnya adalah tentu nilai gabungan dari kedua variabel. 
# Terakhir, kita juga melakukan intersection atau irisan yang merupakan operasi dalam matematika untuk menemukan nilai atau elemen-elemen yang sama dalam dua atau lebih himpunan. Kita menggunakan method “.intersection()” untuk menjalankan operasi ini. Hasilnya adalah nilai 4 dan 5 yang memang berada pada variabel set1 dan variabel set2.

