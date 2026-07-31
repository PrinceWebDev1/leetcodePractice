nums =[]
seen = {}
for ind,i in enumerate(nums):
    if i in seen: 
        return True
    seen[i] = ind
return False

// if i've already seen it then store it and check if i have seen it or not
