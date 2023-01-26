def is_unique(x):
    if len(set(x)) != len(x):
        return False
    else:
        return True

# test = 'asdd'
# print(is_unique(test))

# test_2 = 'asdqwertr'
# print(is_unique(test_2))

def check_permutation(s1, s2):
    s1_count = [0] * 26
    s2_count = [0] * 26
    for c in s1:
        s1_count[ord(c) - ord('a')] += 1
    for i in range(len(s2)):
        if i >= len(s1):
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
        s2_count[ord(s2[i]) - ord('a')] += 1
        if s1_count == s2_count:
            return True
    return False

from collections import Counter

def perm(x, y):
    x_cnt = Counter(x)

    for i in range(len(y) - len(x) + 1):
        start = i
        end = i + len(x)

        substring = y[start:end]
        y_cnt = Counter(substring)

        if x_cnt == y_cnt:
            return True

    return False
        
# x = 'adc'
# y = 'dcda'
# print(check_permutation(x, y))
# print(perm(x, y))

def urlify(x):
    return x.replace(' ', '%20')

# x = 'i love to eat burgers'
# print(urlify(x))

def palindrome(x):
    x_cnt = Counter(x.replace(' ', ''))

    odd_cnt = 0
    for value in x_cnt.values():
        if value % 2 != 0:
            odd_cnt += 1

    return odd_cnt <= 1

# x = 'taco cat'
# print(palindrome(x))

def oneAway(s1: str, s2: str) -> bool:
    # Check if the difference in length between the two strings is greater than 1
    if abs(len(s1) - len(s2)) > 1:
        return False
    # Initialize pointers to the start of each string
    i = j = 0
    # Initialize a variable to keep track of the number of edits
    edits = 0
    # Iterate through the characters of the two strings
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            # If the characters are different, increment the number of edits
            edits += 1
            if len(s1) > len(s2):
                i += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    # If the number of edits is greater than 1, return False
    if edits > 1:
        return False
    return True

def string_compression(x):
    ans = ''

    index = 1
    start = x[0]
    cnt = 1
    ans += start

    for letter in x[1:]:
        index += 1

        if letter == start:
            cnt += 1
            if index == len(x):
                ans += str(cnt)
        elif letter != start:
            ans += str(cnt)
            start = letter
            cnt = 1
            ans += start

    return ans

# x = 'aabcccccaaa'
# print(string_compression(x))

def rotate_90(matrix):
    # cyclic rotation algorithm
    N = len(matrix)
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j]
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp
        

# x = [[1, 1, 1, 1], [0, 0, 0, 0], [2, 2, 2, 2], [3, 3, 3, 3]]
# rotate_90(x)
# print(x)

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    rows = set()
    cols = set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix

# x = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 0]]
# print(zero_matrix(x))

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)


        









