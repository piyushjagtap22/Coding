#URLify

str = "Mr John Smith      "
truelength = 13

#Part 1
spacecount = 0
index = 0
i = 0
for i in range(truelength):
    if str[i] == " ":
        spacecount += 1

l = [*str]

# Finding index value ( after have inserted '%20' ), 
# which will help us in inserting values from the back of the string

index = spacecount*2 + truelength

#Truncating extra spaces from the back of the string
l = l[:index]

for i in range(truelength - 1,0,-1):
    if l[i] == " ":
        #this loop willl never start at first iteration
        l[index-1] = '0'
        l[index-2] = '2'
        l[index-3] = '%'
        index -= 3
    else:
        l[index-1] = l[i]
        index -= 1
print(l)