import random
class Bank:
	def __init__(self):
		self.bank_account = {}
		self.account_password = {}

	def create_account(self):
		account_name = random.randint(10000000,99999999)

		for i in self.bank_account:
			if account_name == self.bank_account:
				account_name = random.randint(10000000, 99999999)

		while True:
			password = input("Please enter your account password : ")
			confirm_password = input("Please enter password again : ")
			if password == confirm_password:
				break
			else:
				print("Password are different, please check your password again.")











