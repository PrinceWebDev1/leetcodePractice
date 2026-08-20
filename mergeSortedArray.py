#correct
p1 = m - 1
p2 = n - 1
p = m + n - 1

while p2 >= 0:
    if p1 >= 0 and nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1
    p -= 1

#mine
mn = m + n - 1
m1 = m-1
n1 = n-1

while n1 != -1:
    if nums2[n1] < nums1[m1]:
        nums1[m1 + 1] = nums1[m1]
        nums1[m1] = nums2[n1]
        m1 -= 1
        n1 -= 1
    else  :  
        nums1[mn] = nums2[n1]
        mn -= 1
