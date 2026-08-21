cms = strs[0]

for i in strs:
    tf = True 
    ind = 0
    while tf :
        if (ind < len(i) and ind < len(cms)) and i[ind] == cms[ind] :
            ind +=1
        else :
            tf = False
    cms = cms[:ind]
return cms

#reducing the common string and only running the second loop till  the smallest string
