input = "Mr Jhon Smith    "
true_length = 13
# total_length = len(input)
index = true_length + (len(input.split()) - 1)*2
input = [*input]




print(index)


for i in range(true_length-1  , 0 , -1):
    if input[i] == " ":
        input[index-1] = '0'
        input[index-2]= '2'
        input[index-3] = '%'
        index -= 3
        
        
    else:
        input[index-1] = input[i]
        index-=1
        

print(input)

