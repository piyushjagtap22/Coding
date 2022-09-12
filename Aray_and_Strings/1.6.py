#String Complression

#Part 1

input = "aabcccccaaa"


hash = {}
res = input[0]
count = 1

for i in input:
    if res[-1] == i:
        count += 1
    if res[-1] != i:
        res = res + str(count) + i
        count = 1
res = res + str(count)

if len(res)<len(input):
    print(res)
else:
    print(input)



