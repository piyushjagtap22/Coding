string = 'namman'

dict = {}

for char in string:
    if char in dict:
        dict[char]+=1
    else:
        dict[char] = 1


print(dict)

count_even = 0
count_odd = 0

for i in dict.values():
    if i%2 != 0:
        count_odd+=1
if count_odd > 1:
    print("not permutation")
else:
    print("permutation")

        


