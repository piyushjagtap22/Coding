

str = "HeloWrd"

# Part 1 : Using Data Structure
# As we have 128 bit characters, we will use an array of 128 zeroes
# Time : O(n) / Space : O(1)

def Is_Unique1(str):
	hash_map = [0] * 128
	if len(str) > 128:
		return "False"
	for i in str:
		if hash_map[ord(i)] == 1:
			return "False"
		if hash_map[ord(i)] == 0:
			hash_map[ord(i)] = 1
	return "True"
print(Is_Unique1(str))

# Part 2 : Without Data Structure
#  Time : O(n^2) / Space : O(1)

def Is_Unique2(str):
	for i in range(len(str)):
		for j in range(i+1,len(str)-1):
			if str[i] == str[j]:
				return "False"

	return "True"

print(Is_Unique2(str))
