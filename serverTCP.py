import socket
import sys
import time
import os

def create_TCP_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_file_size(file_path):
    size = os.path.getsize(file_path)
    return size

# Create a TCP/IP socket
sock = create_TCP_socket()

# Bind the socket to the port
server_address = ('localhost', 8080)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Create arch
file_path = 'archivo_enviado.mp4'
file_size_bytes = get_file_size(file_path)
file_size_MB = file_size_bytes/1000000

f = open(file_path, 'rb')

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        l = connection.recv(16)
        print('received {!r}'.format(l))
        
        # Receive the data in small chunks and retransmit it
        print('Receiving...')

        l = f.read(1024)
        start_time = time.time()
        while (l):
            #print ('Sending...')
            connection.send(l)
            l = f.read(1024)
        f.close()
        end_time = time.time()
        current_time = end_time-start_time
        print('File sent in %f seconds ---' % current_time)
        data_rate = file_size_MB/current_time
        print('Data rate %s MB/s' % data_rate)
        break
    finally:
        # Clean up the connection
        connection.close()
        