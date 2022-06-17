accountName = 'Ivonne'
accountBalance = 1000000
accountPassword = 'quesito'

while True:
	print()
	print('Press b to get the balance')
	print('Press d to make a deposit')
	print('Press w to make a withdraw')
	print('Press s to show the account')
	print('Press q to quit')
	print()

	action = input('This is edgar your money bot, how may i help you today?')
	action = action.lower()
	action = action[0]
	print()
	if action == 'b':
		print('Get balance')
		userPassword = input('please enter the password: ')
		if userPassword != accountPassword:
			print('incorrect password')
		else:
			print('your balance is:', accountBalance)
	elif action == 'd':
		print('deposit')
		userDepositAmount = input('Please enter amount to deposit: ')
		userDepositAmount = int(userDepositAmount)
		userPassword = input('Please enter the password: ')

		if userDepositAmount < 0:
			print('You must enter cash only accepted 100, 200, 500 0r 1000')
		elif userPassword != accountPassword:
			print('incorrect password')
		else:
			accountBalance = accountBalance + userDepositAmount
			print('Your new balance is:', accountBalance)
	elif action == 's':
		print('show:')
		print('		Name', accountName)
		print('		Balance:', accountBalance)
		print('		Password:', accountPassword)
		print()
	elif action == 'q':
		break

	elif action == 'w':
		print('withdraw')

		userWithdrawAmount = input('Please  enter the amount to Withdraw: ')
		userWithdrawAmount = int(userWithdrawAmount)
		userPassword = input('Plese enter the password: ')

		if userWithdrawAmount < 0:
			print('You cannot withdraw a negative amount')

		elif userPassword != accountPassword:
			print('incorrect password for this account')
		elif userWithdrawAmount > accountBalance:
			print('You cannot withdraw more than you have in your account')
		else:
			accountBalance = accountBalance - userWithdrawAmount
			print('Your new balance is: ', accountBalance)
	print('DONE')
