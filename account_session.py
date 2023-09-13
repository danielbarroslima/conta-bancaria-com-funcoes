from account_transactions import *
from account_extract import *

def session(*, value, balance, function, operation):
	result_balance, informer_success = account_transactions(value=value,
															balance=balance,
								                            function=function,
															operation=operation)
	template_extract = update_values_in_extract(operation=operation, value=value)

	return informer_success, template_extract, result_balance
