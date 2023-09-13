from messages import *
from account_session import *
from account_deposit import deposit_account
from account_withdraw import withdraw_account
from account_extract import extract_account

while True:
    option = input(menu)

    if option.lower() == 'd':
        ''
        account_movements, balance = deposit_account(option, balance)

    elif option.lower() == 's':
        ''
        account_movements, balance, user_limit_diary = withdraw_account(option=option,
                                                                        balance=balance,
                                                                        user_limit_diary=user_limit_diary)
    elif option.lower() == 'e':
        extract_account(account_movements, option=option, balance=balance)
    elif option.lower() == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente operação desejada.')
