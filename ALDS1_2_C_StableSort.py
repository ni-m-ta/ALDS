n = int(input())
cards = list(map(str,input().split()))
stabilities = []
def CheckStability(c,n,s):
    for i in range(n):
        for j in range(n):
            if int(c[i][1]) == int(c[j][1]):
                s.append([i,j])



def BubbleSort(c,n):
    for i in range(n):
        for j in range(1,n):
            if int(c[n-j][1]) < int(c[n-j-1][1]):
                temp = c[n-j]
                c[n-j] = c[n-j-1]
                c[n-j-1] = temp
            if int(c[n-j][1]) == int(c[n-j-1][1]):


CheckStability(cards,n,stabilities)
BubbleSort(cards,n)

for i in range(n):
    if i == n-1:
        print(cards[i])
    else:
        print(cards[i],end=' ')