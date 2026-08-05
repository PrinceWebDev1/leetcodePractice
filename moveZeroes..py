insert_pos = 0
for i in range(len(nums)):
    if nums[i] !=0:
        nums[insert_pos] , nums[i] = nums[i], nums[insert_pos]
        insert_pos +=  1

// instead of removing of  addiing try swapping them
