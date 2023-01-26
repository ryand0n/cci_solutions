a = [1, 7, 5, 9, 2, 12, 3]
k = 2
cnt = 0

dic = {}
for i in a:
    dic[i] = i
    if i - k in dic.keys():
        cnt += 1
        print(i, i - k)
    if i + k in dic.keys():
        cnt += 1
        print(i, i + k)

print(cnt)