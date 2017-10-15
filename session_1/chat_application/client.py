import socket
import select
import sys
import time

def prompt():
    sys.stdout.write('[You] ')
    sys.stdout.flush()

host = '127.0.0.1'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(2)
client_socket.connect((host, port))
prompt()

while True:
    socket_list = [sys.stdin, client_socket]
    ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

    for sock in ready_to_read:
        if sock == client_socket:
            data = sock.recv(1024)
            
            if not data:
                sys.stdout.write('Disconnected')
                exit()
            else:
                sys.stdout.write(str(data, 'utf-8'))
                prompt()
        else:
            time_now = time.strftime('%H:%M:%S', time.localtime())
            msg = sys.stdin.readline()
            msg = '{} {}'.format('[user1]', msg.replace('\n', ''))
            msg = '{} - Sent at {}\n'.format(msg, time_now)
            client_socket.send(bytes(msg, 'utf-8'))
            prompt()

client_socket.close()
