input = "Tact Coa"


# Part 1
# Time : O(n) / space : O(1)
# Using hash map and adding to it , 
# if dictionary's keys has all even value or N - 1 even and one odd value,
# then atleast one of its permutation will be palindrome
hash = {}
input = input.lower().replace(" ","")

for i in input:
    hash[i] = hash.get(i, 0) + 1

odd = 0 
even = 0 

for i in hash.values():
    if i% 2 == 0:
        even += 1
    else:
        odd += 1

#ven , oddd = (i , j 
print(odd == 0 or odd == 1)