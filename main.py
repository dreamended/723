class caesargcd:
	def __init__(self, x, y, shift = 6):
		self.x = x
		self.y = y
		self.shift = shift

	def caesar_encrypt(self, number):          #use caesar cipher
		return (number + self.shift) % 256               #encryption
	def caesar_decrypt(self, number):          #decryption
		return (number - self.shift) % 256

	def compute_gcd(self, x, y):
		gcd = 1
		if x != 0 and y != 0:                    #neither number can be zero
			if x > y:                                   # compare who large
				small = y
			else:
				small = x
			for i in range(1, small + 1):               # forloop calculation get the gcd under conditions
				if (x % i == 0) and (y % i == 0):
					gcd = i
		else:                                           #x,y = 0, no answer
			print("Input can't be ZERO!!!")
			gcd = 0
		return gcd

	def encrypt_gcd(self):  # encrypt the GCD
		x_encrypted = self.caesar_encrypt(self.x)  # encrypt the input numbers
		y_encrypted = self.caesar_encrypt(self.y)
		gcd_encrypted = self.compute_gcd(x_encrypted, y_encrypted)  # compute the GCD after encryption
		return gcd_encrypted

	def decrypt_gcd(self, gcd_encrypted):
		return self.caesar_decrypt(gcd_encrypted)

def main():
	print("Welcome to the Euclidean Algorithm with Caesar Cipher!")
	try:
		x = int(input("enter the first number: "))                #enter number
		y = int(input("enter the second number: "))
	except ValueError:
		print("Invalid input! Please enter valid integers.")
		return

	shift = 6           #the amount that will be displaced

	gcd_calculator = caesargcd(x, y, shift)

	gcd_result = gcd_calculator.compute_gcd(x, y)

	gcd_encrypted = gcd_calculator.encrypt_gcd()

	gcd_decrypted = gcd_calculator.decrypt_gcd(gcd_encrypted)

	print(f"Original GCD: {gcd_result}")
	print(f"encrypt : {gcd_encrypted}")
	print(f"decryption : {gcd_decrypted}")

if __name__ == "__main__":
	main()