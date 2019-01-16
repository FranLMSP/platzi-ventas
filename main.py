
clients = 'pablo,ricardo,'

def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('Client is already in the client\'s list')


def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', updated_client_name + ',')
	else:
		print('Client is not in clients list')

def list_clients():
	global clients

	print(clients)

def _add_comma():
	global clients

	clients += ','


def _get_client_name():
	return input('What is the client name? ')


def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[C]reate client')
	print('[D]reate client')
	print('[U]pdate client')


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if(command == 'C'):
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'D':
		pass
	elif command == 'U':
		client_name = _get_client_name()
		new_name = input('What is the new name of the client? ')
		update_client(client_name, new_name)
		list_clients()
	else:
		print('Invalid command')