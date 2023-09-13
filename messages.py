from account_values_default import *

menu = '''
	[d] Depositar
	[s] Sacar
	[e] Extrato
	[q] Sair
'''

messages_system = {
"template_operation": 'Valor do {} de R$: {} \n',
"message_warning": 'O valor para {} precisa ser positivo',
"message_instruction": 'Olá, qual o valor para {} ?  ',
"message_success": '{} no valor de R$: {} realizado(a) com sucesso, o que deseja fazer agora?',
"message_extract": '{} gerado com sucesso, o que deseja fazer agora?',
"template_extract": '''
=====Olá este é seu extrato =====

Saldo em conta: R$: {}

#### Movimentações da conta #####

'''
}

types_operation = { "d": ('deposito'),
					"s": ('saque'),
					"e": ('extrato'),
					"q": ('sair')
}

def message_input(operation):
	value = float(input(messages_system['message_instruction'].format(operation)))
	return value

def insufficient_funds(operation):
	print(f'Saldo insuficiente para efetuar o {operation} deste valor')

def invalid_value(operation):
	print(messages_system['message_warning'].format(operation))

def without_movements():
	print('Não foram realizadas movimentações')

def invalid_option():
	print('Operação inválida, por favor selecione novamente operação desejada.')

def formated_transaction(*, operation, value):
	return messages_system['message_success'].format(operation, value)
