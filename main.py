def compute_gcd(x, y):
	gcd = False
	if x and y != 0:
		if x > y:                                   # compare who large
			small = y
		else:
			small = x
		for i in range(1, small + 1):               # forloop
			if (x % i == 0) and (y % i == 0):
				gcd = i
	else:
		print("Input can't be ZERO!!!")
	return gcd