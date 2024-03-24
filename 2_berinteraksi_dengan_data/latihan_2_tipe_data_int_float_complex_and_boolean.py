# Tipe Data Integer, Float, Complex, dan Boolean
# Tipe Data Integer, Float, Complex, dan Boolean
# Tipe Data Integer, Float, Complex, dan Boolean

"""
- Integer
- Float
- Complex
"""

"""
Tipe data integer merupakan bilangan bulat positif atau negatif dan tidak memiliki angka desimal. Selanjutnya, tipe data float merupakan bilangan riil yang mewakili bilangan bulat dan angka desimal. Terakhir, tipe data complex yang merupakan representasi dari bilangan kompleks dalam matematika. Tipe data complex terdiri dari bilangan riil dan imajiner dengan bentuk “x +yj”, yaitu “x” adalah bilangan riil dan “y” adalah bilangan imajiner. 

Ciri dari bilangan numbers adalah Anda dapat mengoperasikan bilangan tersebut dengan operasi matematika sederhana, seperti pertambahan (+), pengurangan (-), perkalian (*), dan operasi matematika lainnya.
"""

x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""



# Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah. Mari lihat contoh di bawah ini. Hal ini membuktikan secara natural bahwa integer atau numbers merupakan immutable. Alih-alih nilai integer di atas diperbarui, ternyata nilai tersebut masih bernilai sama karena kita masih bisa menampilkannya dengan nama variabel yang identik. 


var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>
"""

# Boolean Tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini merepresentasikan nilai kebenaran (truth values).
# Tipe data primitif kedua 

x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""

# Boolean Tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini merepresentasikan nilai kebenaran (truth values).

