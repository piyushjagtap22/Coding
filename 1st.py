sample = {}
demo = "qwerty"
for i in demo:
    if i in sample.keys():
        print("not a unique")
    else:
        sample[i]=1
    print(sample)


# Better method
a=[]
for i in range(0,128):
    a.append("false")

for i in demo:
    if a[ord(i)] != "True":
        a[ord(i)] = "True"
    else:
        print('NOt a unique String')

# and if we are not able to use additional space then  easily loop thorough two loops one from start another form left and boom,