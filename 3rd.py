a="Mr John smith    "
truelength = 13
index = 0
counter = 0
for i in range(truelength):
    if a[i] == " ":
        counter +=1
    
index = counter*2+truelength
l=[*a]

for i in range(truelength -1,0,-1):
    if l[i] == " ":
        l[index -1] = "0"
        l[index-2] = '2'
        l[index-3] = '%'
        index = index-3
    else:
        l[index-1] = l[i]
        index -=1

print(l)



# a=''.join([str(elem) for elem in temp])

# print("final string",a)

#optimised code