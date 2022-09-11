
str1 = "hello"

str2 = "olleho"

# Part 1
# Sorting and comparing
# Time O(n) //or depening on sorting algo  : Space : O(1)

print(sorted(str1) == sorted(str2))
 
# Part 2
# Using list
# Time : O(n) / Space : O(n)

l1 = [*str1]
for i in str2:
    if i in l1:
        l1.remove(i)
    else:
        l1.append(i)

print(len(l1) == 0)