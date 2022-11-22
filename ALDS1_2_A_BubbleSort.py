n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    for j in range(1,n):
        if a[n-j] < a[n-j-1]:
            temp = a[n-j]
            a[n-j] = a[n-j-1]
            a[n-j-1] = temp
            count += 1

for i in range(n):
    if i == n-1:
        print(a[i])
    else:
        print(a[i],end=' ')
print(count)
