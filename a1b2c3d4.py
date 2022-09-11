def countChar(string):
    char_counts = {}
    s = ''
    res = ''
    for i in range(len(string)):
        if string[i] in char_counts:
            char_counts[string[i]] += 1
            # res = res+string[i]+str(char_counts[string[i]]
            
        else:
            if char_counts.keys():
                res = res + str(list( char_counts.keys())[0]) + str(char_counts[list(char_counts.keys())[0]])
                char_counts.clear()

            char_counts[string[i]] = 1

    if char_counts.keys():
                res = res + str(list( char_counts.keys())[0]) + str(char_counts[list(char_counts.keys())[0]])
                char_counts.clear()
    
    # for k in char_counts:
    #     res = res+k+str(char_counts[k])
    if len(res) > len(string):
        return string
    return res


if __name__ == "__main__":
    string ="aaabbbcccdgggggeee"
    # print()
    print(countChar(string))


