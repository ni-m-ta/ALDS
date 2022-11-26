n = int(input())
cards_B = list(map(str,input().split()))
cards_S = cards_B[::1]

def BubbleSort(c,n):
    for i in range(n):
        for j in range(1,n):
            if int(c[n-j][1]) < int(c[n-j-1][1]):
                temp = c[n-j]
                c[n-j] = c[n-j-1]
                c[n-j-1] = temp

def SelectionSort(c,n):
    for i in range(n):
        minj = i
        for j in range(i,n):
            if int(c[j][1]) < int(c[minj][1]):
                minj = j
        temp = c[minj]
        c[minj] = c[i]
        c[i] = temp

BubbleSort(cards_B,n)
SelectionSort(cards_S,n)

for i in range(n):
    if i == n-1:
        print(cards_B[i])
    else:
        print(cards_B[i],end=' ')
print('Stable')

for i in range(n):
    if i == n-1:
        print(cards_S[i])
    else:
        print(cards_S[i],end=' ')
if cards_B == cards_S:
    print('Stable')
else:
    print('Not stable')