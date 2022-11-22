import math
n = int(input())
nums = [int(input()) for _ in range(n)]
count = 0

for num in nums:
    flag = True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            flag = False
            break
    if flag:
        count += 1

print(count)
    