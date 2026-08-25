record = []
loop = len(operations)

for i in range(loop):
    if operations[i] == '+':
        temp = record[-1] + record[-2]
        record.append(int(temp))
    elif operations[i]  == 'D':
        temp = record[-1]*2
        record.append(int(temp))
    elif operations[i] =='C' :
        record.pop()
    else:
        record.append(int(operations[i]))

final_score = 0
for i in record:
    final_score += int(i)

return final_score

#pretty easy stuff just some attention tto detail would solve it
