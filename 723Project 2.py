import random

class Bank:
	def __init__(self):
		self.bank_account = {}
		self.account_password = {}
		self.locked_account = {}
		self.overdraft_limit = 1500
		self.account = {}

	def create_account(self):
		while True:
			account_name = random.randint(10000000, 99999999)
			if account_name not in self.account:
				break

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
		self.account[account_name] = {'balance': 0.0}
		print(f"Your bank account created successfully, this is your account name : {account_name}"
		      f"Your bank account password is : {password}"
		      f"Your bank account balance is {self.account[account_name]['balance']} pounds.")

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
				self.main_interface(account_name)
			else:
				attempt += 1
				print(f"You password is incorrect, You only have {max_attempt - attempt} attempt."
				      f"If you enter incorrect password over three times, your account will be locked")
				if attempt >= max_attempt:
					self.locked_account[account_name] = True
					print(f"Your account has been locked.")
					break

	def main_interface(self, account_name):
		while True:
			print("/nMain Interface: ")
			print("1.View Balance")
			print("2.save money")
			print("3.draw money")
			print("4.transfer money")

			choice = input("Please enter number(1-5): ")

			if choice == '1':
				self.view_balance(account_name)
			elif choice == '2':
				self.save_money(account_name)
			elif choice == '3':
				self.draw_money(account_name)
			elif choice == '4':
				self.transfer(account_name)
			elif choice == '5':
				print("Logged out successfully.")
				break
			else:
				print("Invalid option, please try again.")

	def view_balance(self, account_name):
		balance = self.account[account_name]['balance']
		print(f"Your current balance is: {balance} pounds.")

	def save_money(self, account_name):
		print(f"Your account balance is : {self.account[account_name]['balance']} pound.")
		while True:
			click = input(f"Do you want to make a deposit, please enter '1' continue, or enter '2' back to home page.")
			if click == '1':
				amount = float(input(f"How much money do you want to save?"))
				if amount <= 0:
					print(f"If you want to give we money, we will happy that.")
				else:
					self.account[account_name]['balance'] += amount
					print(f"successfully save money : {amount} pound, your account balance is : {self.account[account_name]['balance']} pound.")
				break
			elif click == '2':
				print(f"back to home page.")
				break
			else:
				print(f"Please enter '1' or '2' ")

	def draw_money(self, account_name):
		print(f"Your account balance is : {self.account[account_name]['balance']} pound.")
		print(f"Your overdraft limit is: {self.overdraft_limit} pounds.")

		while True:
			action = input(f"Do you want to withdraw, please enter '1' continue, or enter '2' back to home page.")
			if action == '1':
				number = float(input(f"How much money do you want to draw?"))

				if number <= 0:
					print(f"Save money? You should go back to save_money.")
				elif number > self.account[account_name]['balance'] + self.overdraft_limit:
					print(f"You withdrew too much money. Please look at your balance. We are not fools."
					      f"Your account balance and overdraft balance is {self.account[account_name]['balance'] + self.overdraft_limit} pound."
					      f"But you want to draw {number} pound.")
				else:
					self.account[account_name]['balance'] -= number
					print(f"successfully draw money : {number} pound, your account balance is : {self.account[account_name]['balance']} pound.")
				break

			elif action == '2':
				print(f"back to home page.")
				break
			else:
				print(f"Please enter '1' or '2' ")

	def transfer(self, account_name):
		while True:
			transferred_name = input(f"Enter the account name to be transferred")
			if transferred_name not in self.account:
				print(f"Transferred account not found. Please enter a exist account.")
				continue
			amount = float(input(f"Enter the amount to transfer: "))
			if amount <= 0:
				print(f"Invalid amount. Please enter a positive number.")
			elif amount > self.account[account_name]['balance'] + self.overdraft_limit:
				print(
					f"Insufficient funds. Your available balance is {self.account[account_name]['balance'] + self.overdraft_limit} pounds, but you want to transfer {amount} pounds.")
			else:
				self.account[account_name]['balance'] -= amount
				self.account[transferred_name]['balance'] += amount
				print(
					f"Successfully transferred {amount} pounds to account {transferred_name}. Your new balance is {self.account[account_name]['balance']} pounds.")
				break

	def start(self):
		while True:
			print("/nWelcome to the bank!")
			print("1.Log in account.")
			print("2.Create your account.")
			print("3.Exit.")

			choice = input("Please enter number(1-3): ")

			if choice == '1':
				self.log_account()
			elif choice == '2':
				self.create_account()
			elif choice == '3':
				print("Thank you!")
				break
			else:
				print("You should enter 1-3 instead of other numbers or letters.")



















