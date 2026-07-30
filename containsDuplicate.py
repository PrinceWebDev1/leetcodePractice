nums =[]
seen = {}
for ind,i in enumerate(nums):
    if i in seen: 
        return True
    seen[i] = ind
return False
