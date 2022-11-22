n = int(input())
a = list(map(int,input().split()))

for k in range(n):
    if k == n-1:
        print(a[k])
    else:
        print(a[k],end=' ')

for i in range(1,n):
    v = a[i]
    j = i-1
    while j >= 0 and a[j] > v:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = v
    for k in range(n):
        if k == n-1:
            print(a[k])
        else:
            print(a[k],end=' ')


        