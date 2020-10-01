#!/usr/bin/python3
import random 
def pair(x):
    b=x.decode('utf-8')
    s=0
    for i in range(len(b)):
        if b[i] == "1":
           s += 1
    if (s%2) != 0:
        b = "1" + b
    else :
        b = "0" + b
    print(b)
    x=bytearray(b,'utf-8')   
    return x   
def rand_key(p): 
	key1 = "" 
 
	# of desired length 
	for i in range(p): 
		
		# randint function to generate 
		# 0, 1 randomly and converting 
		# the result into str 
		temp = str(random.randint(0, 1)) 

		# Concatenatin the random 0, 1 
		# to the final result 
		key1 += temp 
		
	return(key1) 

# Driver Code 
n = 7
str1 = rand_key(n) 
print(str1)
x=bytearray(str1,'utf-8') 
print(pair(x))
