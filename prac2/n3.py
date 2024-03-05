# n3_1
s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(list(map(int, s)))

# n3_2
print(len(set(s)))

# n3_3
print(s[::-1])

# n3_4
x = '1'
print([i for i, elem in enumerate(s) if elem == x])

# n3_5
print(sum(list(map(int, s))[::2]))
print(sum([int(i) for i in s[::2]]))

# n3_6
print(max(s, key=len))

# n3_7
import random
a = [random.randint(0, 1000) for _ in range(10)]
print([el for el in a if el % sum(map(int, list(str(el)))) == 0])

# n3_8
max_len = 100
print(''.join([chr(random.randint(97, 122)) for _ in range(max_len)]))


# n3_9
def rle_encode(s: str) -> list:
    return [(i, s.count(i)) for i in set(s)]


print(rle_encode('ABBCCCDEF'))
