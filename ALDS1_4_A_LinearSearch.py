n = int(input())
s = list(map(int,input().split()))
q = int(input())
t = list(map(int,input().split()))
count = 0

s = list(set(s))
for i in range(len(s)):
    if s[i] in t:
        count += 1

print(count)