import math
import sys


print("n1_1")
print("42")
print(ord('*'))
print(int('101010', 2))
print(sum([7, 7, 7, 7, 7, 7]))
print(len("The answer to the ultimate question of line"[:42]))
print(int(42.34))
print(21 << 1)
print(84 >> 1)
print((42, 15)[0])
print({"first": 3, "second": 42}["second"])


print("n1_2")
print(sys.float_info.max)


print("n1_3")
print(divmod(42, 2))


print("n1_4")
a = 10
while a != 0:
    a = round(a - 0.1, 1)
print(a)


print("n1_5")
z = 1
z <<= 40
try:
    var = 2.0 ** z
except Exception as e:
    print(e)  # (34, 'Result too large')


print("n1_6")
i = 0
while i < 10:
    print(i)
    i += 1


print("n1_7")
print((True * 2 + False) * - True)  # Эквивалентно (1 * 2 + 0) * -1


print("n1_8")
x = 5
print(1 < x < 10)  # True, так как 5 между 1 и 10
print(1 < (x < 10))  # False, так как x < 10 возвращает True(1), а 1 < 1 False
