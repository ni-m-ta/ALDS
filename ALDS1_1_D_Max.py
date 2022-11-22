n = int(input())
r = [int(input()) for _ in range(n)]
min_r = r[0]
max_pro = -1*10**10
for i in range(1,n):
    if max_pro < r[i] - min_r:
        max_pro = r[i] - min_r
    if min_r > r[i]:
        min_r = r[i]

print(max_pro)