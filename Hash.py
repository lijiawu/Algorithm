#HashTable Size the prime number that closest to Data size (bigger tha Data.size)
NHASH = 29989 
MULT = 31

def hash(string):
	h = 0
	for char in string:
		h = MULT * h + ord(char)
	return h % NHASH

string = "helloWorld"
print("hash(%s) = %d" %(string,hash(string)))