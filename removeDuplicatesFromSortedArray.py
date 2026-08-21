a = None
k = 0
place = 0
for i in  range(len(nums)) :
    if a == nums[i]:
        nums[i] = '_'
    else :
        a = nums[i]
        nums[i], nums[place] = nums[place] , nums [i]
        k += 1
        place +=1
return k

#removing the common elements and swapping the unique elements with the underscore (run an example you will understand) btw did it in first try :)
