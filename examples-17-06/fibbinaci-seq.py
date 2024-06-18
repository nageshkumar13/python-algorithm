n = 8

res = [0, 1]

for i in range(n-2):
    new_num = res[-1] + res[-2]
    res.append(new_num)

print(res)
