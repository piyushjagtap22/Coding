str1 = 'hello'
str2 = 'zoehlll'

dict = {}


for char in str1:
    if char in dict:
        dict[char]+=1
    else:
        dict[char] = 1

print(dict)

for char in str2:
    
    if char not in dict.keys():
        dict[char] = 1
    else:
        dict[char] -= 1
    
    if dict[char] == 0:
        dict.pop(char)

print(len(dict) == 0)