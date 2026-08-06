left = 0
right = len(numbers) - 1
for i in range(len(numbers)) :
    if numbers[left] + numbers[right] == target : return [left + 1, right + 1]
    elif numbers[left] + numbers[right] > target : right -= 1
    else : left += 1  

// it was sorted loop so instead of using two loops why not check from start and end together cause nuumbers not gonna repeat and one pair will always pair oncce
