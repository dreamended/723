import random

class Bank:
	# Initialize the bank class, set up account data dictionaries, password dictionary, locked accounts, overdraft limit, etc.
	def __init__(self):
		self.bank_account = {}          # Dictionary to store bank account and password
		self.account_password = {}          # Dictionary to store account passwords
		self.locked_account = {}            # Dictionary to store locked accounts
		self.overdraft_limit = 1500         # Overdraft limit
		self.account = {}           # Dictionary to store all accounts' balance information

	# Convert a decimal number to 32-bit two's complement representation
	@staticmethod
	def decimal_to_twos_complement(decimal_value):
		if decimal_value < 0:
			value = (1 << 32) + decimal_value       # Negative numbers to two's complement
		else:
			value = decimal_value           # Positive numbers remain the same
		return value

	# Convert a 32-bit two's complement value to decimal
	@staticmethod
	def twos_complement_to_decimal(twos_value):
		if twos_value >= (1 << 31):
			return twos_value - (1 << 32)       # Convert two's complement to decimal for negative numbers
		else:
			return twos_value           # Positive numbers remain the same

	# Create a bank account
	def create_account(self):
		# Generate a random 8-digit account number, ensuring it's unique
		while True:
			account_name = str(random.randint(10000000, 99999999))          # Randomly generate an 8-digit account number
			if account_name not in self.account:
				break       # Ensure account name is unique

		# Password input and confirmation
		while True:
			password = input("Please enter your account password : ")        # Input password
			if not (8 <= len(password) <= 16):          # Password length should be between 8 and 16
				print(f"The password must be between 8 and 16 number. Please enter again.")
				continue

			confirm_password = input("Please enter password again : ")      # Confirm password

			if password == confirm_password:
				break           # If passwords match, break the loop
			else:
				print("Password are different, please check your password again.")       # If passwords don't match, ask to re-enter

		# Create account information, store password and balance
		self.bank_account[account_name] = password      # Store the account password
		self.account[account_name] =  {'balance': self.decimal_to_twos_complement(0.0)}     # Initial balance is 0
		print(f"Your bank account created successfully, this is your account name : {account_name}"
		      f"Your bank account password is : {password}"
		      f"Your bank account balance is {self.twos_complement_to_decimal(self.account[account_name]['balance'])} pounds.")

	# Log into an account
	def log_account(self):
		attempt = 0     # Login attempt counter
		max_attempt = 3         # Maximum attempts

		while True:
			account_name = input(f"Please enter your account name : ")       # Input account name
			password = input(f"Please enter your account password : ")      # Input password
			# Check if the account is locked
			if account_name in self.locked_account and self.locked_account[account_name]:
				print(f"You entered your password more than three times, so we have locked your account ")
				return      # If account is locked, stop

			# Check if the account name and password are correct
			if account_name in self.bank_account and self.bank_account[account_name] == password:
				print(f"Login successfully.")
				self.main_interface(account_name)           # If login is successful, go to the main interface
			else:
				attempt += 1         # If password is incorrect, increment attempt counter
				print(f"You password is incorrect, You only have {max_attempt - attempt} attempt."
				      f"If you enter incorrect password over three times, your account will be locked")
				# Lock the account after maximum failed attempts
				if attempt >= max_attempt:
					self.locked_account[account_name] = True
					print(f"Your account has been locked.")
					break

	# Main interface
	def main_interface(self, account_name):
		while True:
			print("\nMain Interface: ")
			print("1.View Balance")         # View balance
			print("2.save money")           # Deposit money
			print("3.draw money")           # Withdraw money
			print("4.transfer money")          # Transfer money

			choice = input("Please enter number(1-5): ")         # Input choice

			if choice == '1':
				self.view_balance(account_name)     # View balance
			elif choice == '2':
				self.save_money(account_name)       # Deposit money
			elif choice == '3':
				self.draw_money(account_name)       # Withdraw money
			elif choice == '4':
				self.transfer(account_name)     #Transfer money
			elif choice == '5':
				print("Logged out successfully.")       # Logout
				break
			else:
				print("Invalid option, please try again.")      # Invalid input

	# View account balance
	def view_balance(self, account_name):
		balance = self.twos_complement_to_decimal(self.account[account_name]['balance'])
		print(f"Your current balance is: {balance} pounds.")        # Display balance

	# Deposit money
	def save_money(self, account_name):
		current_balance = self.twos_complement_to_decimal(self.account[account_name]['balance'])
		print(f"Your account balance is : {current_balance} pound.")

		while True:
			click = input(f"Do you want to make a deposit, please enter '1' continue, or enter '2' back to home page.")
			# User decides whether to continue depositing
			if click == '1':
				amount = float(input(f"How much money do you want to save?"))       # Input deposit amount
				if amount <= 0:
					print(f"If you want to give we money, we will happy that.")      # Invalid deposit amount
				else:
					# Successfully deposit, update balance
					new_balance = current_balance + amount
					self.account[account_name]['balance'] = self.decimal_to_twos_complement(new_balance)
					print(f"successfully save money : {amount} pound, your account balance is : {self.twos_complement_to_decimal(self.account[account_name]['balance'])} pound.")
				break
			elif click == '2':
				print(f"back to home page.")        # Go back to the main page
				break
			else:
				print(f"Please enter '1' or '2' ")      # Invalid input

	# Withdraw money
	def draw_money(self, account_name):
		current_balance = self.twos_complement_to_decimal(self.account[account_name]['balance'])
		print(f"Your account balance is : {current_balance} pound.")
		print(f"Your overdraft limit is: {self.overdraft_limit} pounds.")       # Display overdraft limit

		while True:
			action = input(f"Do you want to withdraw, please enter '1' continue, or enter '2' back to home page.")
			# User decides whether to continue withdrawing
			if action == '1':
				number = float(input(f"How much money do you want to draw?"))       # Input withdrawal amount

				# Invalid withdrawal amount
				if number <= 0:
					print(f"Save money? You should go back to save_money.")         # Suggest going to save money
				elif number > self.account[account_name]['balance'] + self.overdraft_limit:
					# Withdrawal exceeds account balance and overdraft limit
					print(f"You withdrew too much money. Please look at your balance. We are not fools."
					      f"Your account balance and overdraft balance is {self.account[account_name]['balance'] + self.overdraft_limit} pound."
					      f"But you want to draw {number} pound.")
				else:
					# Successfully withdraw, update balance
					new_balance = current_balance - number
					self.account[account_name]['balance'] = self.decimal_to_twos_complement(new_balance)
					print(f"successfully draw money : {number} pound, your account balance is : {self.account[account_name]['balance']} pound.")
				break

			elif action == '2':
				print(f"back to home page.")         # Go back to the main page
				break
			else:
				print(f"Please enter '1' or '2' ")      # Invalid input

	# Transfer money
	def transfer(self, account_name):
		while True:
			transferred_name = input(f"Enter the account name to be transferred")       # Input the target account name
			if transferred_name not in self.account:
				print(f"Transferred account not found. Please enter a exist account.")      # Target account not found
				continue
			amount = float(input(f"Enter the amount to transfer: "))        # Input transfer amount
			if amount <= 0:
				print(f"Invalid amount. Please enter a positive number.")        # Invalid amount

				current_balance = self.twos_complement_to_decimal(self.account[account_name]['balance'])
				if amount > current_balance + self.overdraft_limit:
					# Insufficient funds
					print(
						f"Insufficient funds. Your available balance is {current_balance + self.overdraft_limit} pounds, "
						f"but you want to transfer {amount} pounds.")
				else:
					# Successfully transfer, update balance
					new_balance = current_balance - amount
					self.account[account_name]['balance'] = self.decimal_to_twos_complement(new_balance)

					transferred_balance = self.twos_complement_to_decimal(
						self.account[transferred_name]['balance']) + amount
					self.account[transferred_name]['balance'] = self.decimal_to_twos_complement(transferred_balance)

					print(f"Successfully transferred {amount} pounds to account {transferred_name}. "
					      f"Your new balance is {new_balance} pounds.")
				break

	# Start the program
	def start(self):
		while True:
			print("\nWelcome to the bank!")     # Welcome screen
			print("1.Log in account.")
			print("2.Create your account.")
			print("3.Exit.")

			choice = input("Please enter number(1-3): ")        # Input choice

			if choice == '1':
				self.log_account()      # Log in
			elif choice == '2':
				self.create_account()       # Create an account
			elif choice == '3':
				print("Thank you!")      # Exit
				break
			else:
				print("You should enter 1-3 instead of other numbers or letters.")
if __name__ == "__main__":

	bank = Bank()
	bank.start()


















