from messages import *
from account_values_default import *
from account_session import session

def withdraw_value(balance, value):
    withdraw_balance = balance - value
    return withdraw_balance

def withdraw_limit_diary(*, user_limit_diary):
    return user_limit_diary < 1

def withdraw_limit_transaction(*, value):
    return value > 500

def account_limit():
    print(
        f'Limite atingido, limite diário: ({WITHDRAWAL_LIMIT}) saques, limite por saque: (500)')


def limit_target():
    print(f'limite por saque: (500)')

def withdraw_account(*, option, balance, user_limit_diary):
    account_movements_local = account_movements
    limit_transation_target = withdraw_limit_diary(
        user_limit_diary=user_limit_diary)
    balance_for_withdraw = balance

    if limit_transation_target:
        account_limit()
    else:
        operation = types_operation[option.lower()].title()
        value = message_input(operation)

        if value <= 0:
            invalid_value(operation)
        elif value > balance_for_withdraw:
            insufficient_funds(operation)
        elif balance_for_withdraw == 0:
            insufficient_funds(operation)
        elif value <= balance_for_withdraw:
            if withdraw_limit_transaction(value=value):
                limit_target()
            else:
                result, messages_system['template_extract'], balance = session(value=value,
                                                                               balance=balance_for_withdraw,
                                                                               function=withdraw_value,
                                                                               operation=operation)
                print(result)
                account_movements_local = True
                user_limit_diary -= 1

    return account_movements_local, balance, user_limit_diary
