import sys
input = sys.stdin.readline
n = int(input())
d = set()
i = 0
ans = []
for _ in range(n):
    instruction,string = input().split()
    if instruction == 'insert':
        d.add(string)
    else: #instruction = find
        if string in d:
            print('yes')
        else:
            print('no')
        

