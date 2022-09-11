# s1 = 'harsh'
# s2 = 'piyush'

# s1 = s1+s2
# print(s1,s2)
# s2 = s1[:-len(s2)]
# print(s1,s2)
# s1 = s1[len(s2):]
# print(s1,s2)

# i=5
# j=10

# i = i+j
# j = i-j
# i = i-j


# print(i,j)

# def numberOfPaths(m, n):

#     if(m == 1 or n == 1):
#         return 1
#     return numberOfPaths(m-1, n) + numberOfPaths(m, n-1)
 
# m = 3
# n = 3

# print(numberOfPaths(m, n))


arr = [0, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 0]

i = 0
j = len(arr) - 1



while i<j :
    # if arr[j] == 0:
    #     j-=1

    if arr[i] == 0:
        if arr[j] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1

        else:
            j-=1
    i+=1
    if i ==1 and j==8:
        break
    print(i,j)

print(arr)


# Meeting title: R2 On-site interview for Kirtish Barmecha, SDE I
# Personalized ID: 1480829329
# Meeting ID: 1480 82 9329
# Hosting Region: Ireland
# URL Link: https://chime.aws/1480829329
# US dial-in: +1 206-462-5569
# US toll-free dial-in: +1 855-552-4463
# International dial-in numbers: https://chime.aws/dialinnumbers/



        



