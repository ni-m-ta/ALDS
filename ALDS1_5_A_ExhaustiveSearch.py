def solve(i,m,n,lists):
    if m==0:
        return True
    if i>=n:
        return False
    res = solve(i+1,m,n,lists) or solve(i+1,m-lists[i],n,lists) #boolean
    return res

n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

for i in range(q):
    j = 0
    if solve(j,m[i],n,a):
        print('yes')
    else:
        print('no')


