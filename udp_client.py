import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 4096
print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'1 Hey!', server_address)
client.sendto(b'2 Hey!', server_address)
client.sendto(b'3 Hey!', server_address)
client.sendto(b'4 Hey!', server_address)
client.sendto(b'5 Hey!', server_address)
client.sendto(b'6 Hey!', server_address)
client.sendto(b'7 Hey!', server_address)
client.sendto(b'8 Hey!', server_address)
client.sendto(b'9 Hey!', server_address)
client.sendto(b'10 Hey!', server_address)
client.sendto(b'11 Hey!', server_address)
client.sendto(b'12 Hey!', server_address)
client.sendto(b'13 Hey!', server_address)
data, server = client.recvfrom(max_size)
print('At', datetime.now(), server, 'said', data)
client.close()