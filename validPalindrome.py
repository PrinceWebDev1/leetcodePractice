s = s.replace(" ", "")
s = s.lower()
newS = ""
newSPalin = ""
lenS = len(s)
for i in range(0,lenS,1 ) :
    ordinal = ord(s[i])
    if ordinal in range(97, 123) or ordinal in range(48, 58):
        newS =  newS + chr(ordinal)
for i in range(-1,-len(newS)-1,-1 ) :
    newSPalin = newSPalin + newS[i]

if newSPalin == newS : return True
return False

