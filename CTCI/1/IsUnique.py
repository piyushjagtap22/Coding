string = 'shivanshu'

def isUnique(string):
    if len(string) > 128:
        print(len(string))
        print("length is greater than 128")
        return
    array = [1]*128
    for char in string:

        array[ord(char)]-=1
        if array[ord(char)] < 0:
            return False
    # print(array)
    return True

print(isUnique(string)) 
