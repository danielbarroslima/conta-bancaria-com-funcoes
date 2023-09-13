from messages import messages_system, types_operation, without_movements

def update_values_in_extract(*, operation, value):
    template_extract = messages_system['template_extract']
    template_extract += update_extract(operation=operation, value=value)

    return template_extract

def update_extract(*, operation, value):
    template = messages_system['template_operation'].format(operation, value)

    return template


def extract_account(account_movements, /, *, option, balance):
    operation = types_operation[option.lower()].title()
    if account_movements == False:
        without_movements()
    else:
        balance_extract = f'{balance:.2f}'
        print(messages_system['template_extract'].format(balance_extract))
        print(messages_system['message_extract'].format(operation))
