# n5_1
def ham_dist(num1, num2):
    hamming_distance = 0
    while num1 > 0 or num2 > 0:
        bit1 = num1 & 1
        bit2 = num2 & 1
        if bit1 != bit2:
            hamming_distance += 1
        num1 >>= 1
        num2 >>= 1
    return hamming_distance


print(ham_dist(0b1100, 0b0011))


def ham_dist2(num1, num2):
    return bin(num1 ^ num2).count('1')


print(ham_dist2(0b1100, 0b0011))


# n5_2

# n5_3
def levenshtein_distance(str1, str2):
    def helper(str1, str2, m, n):
        if m == 0:
            return n
        if n == 0:
            return m

        if str1[m - 1] == str2[n - 1]:
            return helper(str1, str2, m - 1, n - 1)

        return 1 + min(helper(str1, str2, m, n - 1),
                       helper(str1, str2, m - 1, n),
                       helper(str1, str2, m - 1, n - 1))

    return helper(str1, str2, len(str1), len(str2))


print(levenshtein_distance('столб', 'слон'))


# n5_4
def levenshtein_distance_ops(str1, str2):
    def helper(str1, str2, m, n):
        if m == 0:
            return n, ['вставка'] * n
        if n == 0:
            return m, ['удаление'] * m

        if str1[m - 1] == str2[n - 1]:
            dist, ops = helper(str1, str2, m - 1, n - 1)
            return dist, ops

        dist_insert, ops_insert = helper(str1, str2, m, n - 1)
        dist_delete, ops_delete = helper(str1, str2, m - 1, n)
        dist_replace, ops_replace = helper(str1, str2, m - 1, n - 1)

        if dist_insert <= dist_delete and dist_insert <= dist_replace:
            return dist_insert + 1, ops_insert + ['вставка']
        elif dist_delete <= dist_insert and dist_delete <= dist_replace:
            return dist_delete + 1, ops_delete + ['удаление']
        else:
            return dist_replace + 1, ops_replace + ['замена']

    distance, operations = helper(str1, str2, len(str1), len(str2))
    operations.reverse()
    return operations


print(levenshtein_distance_ops("столб", "слон"))  # Выведет: ['замена', 'удаление', 'замена']

