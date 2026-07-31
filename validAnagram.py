if len(s) != len(t):
    return False

count = {}
for char in s:
    count[char] = count.get(char, 0) + 1

for char in t:
    if char not in count:
        return False
    count[char] -= 1
    if count[char] < 0:
        return False

return True

// if they are in  the same number their differece should be 0
