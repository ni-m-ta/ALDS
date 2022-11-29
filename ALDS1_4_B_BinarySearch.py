n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))
count = 0

for i in range(q):
    left = 0
    right = len(s)-1
    mid = (left + right)//2
    while left <= right:
        if s[mid] > t[i]:
            right = mid-1
        elif s[mid] < t[i]:
            left = mid+1
        else:
            count += 1
            break
        mid = (left + right)//2

print(count)
        
