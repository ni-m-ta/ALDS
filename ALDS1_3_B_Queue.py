from collections import deque

deq = deque()
ans = []
fin_time = 0

n,q = map(int,input().split())
for i in range(n):
    name,time = input().split()
    time = int(time)
    deq.append((name,time))

while deq:
    name,time = deq.popleft()
    if time <= q:
        fin_time += time
        ans.append(name+' '+str(fin_time))
    else:
        fin_time += q
        deq.append((name,time-q))

for a in ans:
    print(a)




