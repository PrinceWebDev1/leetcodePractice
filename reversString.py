length = len(s)
for i in range(length-1, -1, -1):
    s.append(s[i])
    s.pop(i)
print(s)
