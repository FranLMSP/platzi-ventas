import sys

clients = ['pablo', 'ricardo']

def create_client(client_name):
	global clients

	if client_name not in clients:
		clients.append(client_name)
	else:
		print('Client is already in the client\'s list')


def delete_client():
	global clients

	if client_name not in clients:
		print('Client is not in the client\'s list')
	else:
		clients.remove(client_name)


def list_clients():
	for idx, client in enumerate(clients):
		print('{}: {}'.format(idx, client))

def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		index = clients.index(client_name)
		clients[index] = updated_client_name
	else:
		print('Client is not in clients list')


def search_client(client_name):
	for client in clients:
		if client != client_name:
			continue
		else:
			return True


def _get_client_name():
	client_name = None

	while not client_name:
		client_name = input('What is the client name? ')

		if client_name == 'exit':
			client_name = None
			break


	if not client_name:
		sys.exit()

	return client_name


def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do today?')
	print('[L]ist clients')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete client')
	print('[S]earch client')


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if(command == 'L'):
		list_clients()
	elif command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'D':
		client_name = _get_client_name()
		update_client(client_name, '')
		list_clients()
	elif command == 'U':
		client_name = _get_client_name()
		new_name = input('What is the new name of the client? ')
		update_client(client_name, new_name)
		list_clients()
	elif command == 'S':
		client_name = _get_client_name()
		found = search_client(client_name)

		if(found):
			print('The client {} is in the client\'s list'.format(client_name))
		else:
			print(f"The client {client_name} is not in the client\'s list")
	else:
		print('Invalid command')