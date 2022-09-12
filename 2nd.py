# check wheather one is a permutation of other
a="ancd"
b="dnca"

a=sorted(a)
b=sorted(b)
# b=b.sort()
print(a,"==>",b)
if(a==b):
    print('yes')
else:
    print("NO")

# complexity = nlogn


#optimised code same as previous code