from messages import *
from account_session import *
from account_values_default import *

def deposit_value(balance, value):
	balance += value
	return balance

# def validate_input(option, balance):
# 	operation = types_operation[option.lower()].title()
# 	value = message_input(operation)

# 	invalid_value(operation) if value <= 0 else transaction(value=value, operation=operation, balance=balance)

def deposit_account(*, option, balance):
	# validate_input(option, balance)
	operation = types_operation[option.lower()].title()
	value = message_input(operation)


	if value <= 0:
		invalid_value(operation)
	else:
		balance_for_deposit = balance
		result, messages_system['template_extract'], balance = session(value=value,
																	   balance=balance_for_deposit,
																	   function=deposit_value,
																	   operation=operation)
		account_movements = True
		print(result)

		return account_movements, balance

# def transaction(*, value, operation, balance):
# 	balance_for_deposit = balance
# 	result, messages_system['template_extract'], balance_for_deposit = session(value=value,
# 																   balance=balance_for_deposit,
# 																   function=deposit_value,
# 																   operation=operation)
# 	account_movements = True
# 	print(result)

# 	return account_movements, balance_for_deposit