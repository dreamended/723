import random

class Bank:
	def __init__(self):
		self.bank_account = {}
		self.account_password = {}
		self.balance = .0
		self.locked_account = {}

	def create_account(self):
		account_name = random.randint(10000000,99999999)

		for i in self.bank_account:
			if account_name == self.bank_account:
				account_name = random.randint(10000000, 99999999)

		while True:
			password = input("Please enter your account password : ")
			if not (8 <= len(password) <= 16):
				print(f"The password must be between 8 and 16 number. Please enter again.")
				continue

			confirm_password = input("Please enter password again : ")

			if password == confirm_password:
				break
			else:
				print("Password are different, please check your password again.")

		self.bank_account[account_name] = password
		print(f"Your bank account created successfully, this is your account name : {account_name}"
		      f"Your bank account password is : {password}")

	def log_account(self):
		attempt = 0
		max_attempt = 3

		while True:
			account_name = input(f"Please enter your account name : ")
			password = input(f"Please enter your account password : ")
			if account_name in self.locked_account and self.locked_account[account_name]:
				print(f"You entered your password more than three times, so we have locked your account ")
				return

			if account_name in self.bank_account and self.bank_account[account_name] == password:
				print(f"Login successfully.")
			else:
				attempt += 1
				print(f"You password is incorrect, You only have {max_attempt - attempt} attempt."
				      f"If you enter incorrect password over three times, your account will be locked")
				if attempt >= max_attempt:
					self.locked_account[account_name] = True
					print(f"Your account has been locked.")
					break



	def save_money(self, amount):
		print(f"Your account balance is : {self.balance} pound.")
		while True:
			click = input(f"Do you want to make a deposit, please enter '1' continue, or enter '2' back to home page.")
			if click == '1':
				amount = float(input(f"How much money do you want to save?"))
				if amount <= 0:
					print(f"If you want to give we money, we will happy that.")
				else:
					self.balance += amount
					print(f"successfully save money : {amount} pound, your account balance is : {self.balance} pound.")
				break
			elif click == '2':
				print(f"back to home page.")
				break
			else:
				print(f"Please enter '1' or '2' ")

	def draw_money(self):
		print(f"Your account balance is : {self.balance} pound.")
		while True:
			action = input(f"Do you want to withdraw, please enter '1' continue, or enter '2' back to home page.")
			if action == '1':
				number = float(input(f"How much money do you want to draw?"))
				if number <= 0:
					print(f"Save money? You should go back to save_money.")
				elif number > self.balance:
					print(f"You withdrew too much money. Please look at your balance. We are not fools."
					      f"Your account balance is {self.balance} pound."
					      f"But you want to draw {number} pound.")
				else:
					self.balance -= number
					print(f"successfully draw money : {number} pound, your account balance is : {self.balance} pound.")
				break
			elif action == '2':
				print(f"back to home page.")
				break
			else:
				print(f"Please enter '1' or '2' ")



















