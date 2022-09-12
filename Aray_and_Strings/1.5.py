

s1 = "palex"
s2 = "palx"

def replace(s1,s2):
    flag = 0
    for i in range(len(s1)):
        print(s1[i],s2[i])
        if s1[i] != s2[i]:
            if flag == 1:
                print('False replace')
                return False
            flag = 1
    print('True replace')
    return True



def ins_rem(s1,s2):
    i = 0
    j = 0
    while (j<len(s2) and i<len(s1)):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True

def one_edit(s1,s2):
    print(s1,s2)
    if len(s1)-len(s2) > 2:
        return False
    if len(s2)<len(s1):
        s1,s2 = s2,s1 
    i = 0
    j = 0
    if len(s1) == len(s2):
        return replace(s1,s2)
    else:
        return ins_rem(s1,s2)
    return False

print(one_edit(s1,s2))


       
