#逆ポーランド記法
stack = []
for x in input().split():
    if x in '+-*':
        o2 = stack.pop()
        o1 = stack.pop()
        stack.append(str(eval(o1 + x + o2)))
    else:
        stack.append(x)
print(stack[0])

#eval()---文字列を式に変換