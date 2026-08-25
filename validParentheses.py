
stack = []
        opening = {'(':1,'{':2,'[':3}
        closing = {')':1,'}':2,']':3}

        for i in s:
            if i in opening:
                stack.append(i)
            else :
                if len(stack) != 0 and closing[i] == opening[stack[-1]]:
                    stack.pop()
                else : return False
        
        if len(stack) == 0: return True
        else: return False

#it's like using stach lifo yyeah because if the brackett which is opened last should be closed first right otherwise it should  be error
