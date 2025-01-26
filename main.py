x = int(input("enter the first number"))                #enter number
y = int(input("enter the second number"))
def compute_gcd(x, y):
	gcd = False
	if x and y != 0:                    #neither number can be zero
		if x > y:                                   # compare who large
			small = y
		else:
			small = x
		for i in range(1, small + 1):               # forloop calculation get the gcd under conditions
			if (x % i == 0) and (y % i == 0):
				gcd = i
	else:                                           #x,y = 0, no answer
		print("Input can't be ZERO!!!")
	return gcd
result = compute_gcd(x, y)
print(result)