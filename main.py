def caesar_encrypt(number, shift):          #use caesar cipher
	return (number + shift) % 256               #encryption
def caesar_decrypt(number, shift):          #decryption
	return (number - shift) % 256

x = int(input("enter the first number: "))                #enter number
y = int(input("enter the second number: "))
shift = 6           #the amount that will be displaced

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

x_encrypted = caesar_encrypt(x, shift)          #encrypt the input numbers
y_encrypted = caesar_encrypt(y, shift)

gcd_encrypted = compute_gcd(x_encrypted, y_encrypted)           #calculate the greatest common divisor after encryption

gcd_decrypted = caesar_decrypt(gcd_encrypted, shift)            #decryption the result

print(f"encrypt : {gcd_encrypted}")
print(f"decryption : {gcd_decrypted}")