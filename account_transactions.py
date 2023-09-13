from messages import messages_system, formated_transaction

def account_transactions(*, value, balance, function, operation):
    balance_with_deposit = function(balance, value)
    value_formated = f'{value:.2f}'

    return balance_with_deposit, formated_transaction(operation=operation, value=value_formated)
