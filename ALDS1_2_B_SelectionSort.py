n = int(input())
a = list(map(int,input().split()))
count = 0

for i in range(n):
    minj = i
    for j in range(i,n):
        if a[j] < a[minj]:          
            minj = j
    if minj != i:
        count += 1
    temp = a[i]
    a[i] = a[minj]
    a[minj] = temp

for i in range(n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i],end=' ')
print(count)
