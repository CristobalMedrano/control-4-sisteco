import socket
import sys

def create_TCP_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a TCP/IP socket
sock = create_TCP_socket()

# Connect to socket to the port where the server is listening
server_address = ('localhost', 8080)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
msg = b'ok'

file_path = 'archivo_recibido.mp4'
f = open(file_path, 'wb')

try:
    # Send data
    print('Sending request...')
    sock.sendall(msg)
    print('Done sending')

    # Receive the data in small chunks and retransmit it
    print('Receiving...')

    l = sock.recv(1024)
    while (l):
        #print('Receiving...')
        f.write(l)
        l = sock.recv(1024)
    f.close()
    print('Done receiving')
    
finally:
    print('Closing socket')
    sock.close()