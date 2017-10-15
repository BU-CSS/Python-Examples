import re
import socket
import select
import threading
from termcolor import colored

class Client:
    def __init__(self):
        self.challenges = {
            'username': False,
            'timestamp': False
        }

    def get_challenge(self, challenge):
        if challenge in self.challenges.keys():
            return self.challenges[challenge]

    def complete_challenge(self, challenge):
        if challenge in self.challenges.keys():
            self.challenges[challenge] = True

class IMServer(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.server_socket = None
        self.connected_clients = []
        self.client_history = []
        self.client_logs = {}
        self.points = 0

    def bind_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(25)
        self.connected_clients.append(self.server_socket)

    def broadcast(self, sock, message):
        for client in self.connected_clients:
            if client != self.server_socket:
                try:
                    if message[0:1] != '\r':
                        message = '\r' + str(message, 'utf-8')
                        message = bytes(message, 'utf-8')

                    client.send(message)
                except:
                    client.close()

                    if socket in self.connected_clients:
                        self.connected_clients.remove()

    def run(self):
        self.bind_server()

        while True:
            ready_to_read, write_sockets, error_sockets = select.select(self.connected_clients, [], [], 0)

            for sock in ready_to_read:
                if sock == self.server_socket:
                    conn, addr = self.server_socket.accept()
                    self.connected_clients.append(conn)

                    if addr[0] not in self.client_history:
                        self.points += 1
                        self.client_history.append(addr[0])
                        self.client_logs[addr[0]] = Client()
                        print(colored('[+] Someone connected from {} (+1 point)'.format(addr), 'green'))
                        self.show_points()
                else:
                    try:
                        data = sock.recv(1024)

                        if data:
                            data_string = str(data, 'utf-8')
                            address = sock.getpeername()[0]
                            username_challenge = self.check_username_challenge(data_string)
                            timestamp_challenge = self.check_timestamp_challenge(data_string)

                            if username_challenge is True:
                                if self.client_logs[address].get_challenge('username') is False:
                                    self.points += 2
                                    self.client_logs[address].complete_challenge('username')
                                    print(colored('[+] {} has completed the username challenge (+2 points)'.format(address), 'green'))
                                    self.show_points()
                            else:
                                data_string = '\r[{}] {}\n'.format(sock.getpeername()[0], data_string)

                            if timestamp_challenge is True:
                                if self.client_logs[address].get_challenge('timestamp') is False:
                                    self.points += 4
                                    self.client_logs[address].complete_challenge('timestamp')
                                    print(colored('[+] {} has completed the timestamp challenge (+4 points)'.format(address), 'green'))
                                    self.show_points()

                            self.broadcast(sock, bytes(data_string, 'utf-8'))
                        else:
                            if sock in self.connected_clients:
                                self.connected_clients.remove(sock)

                            # client left
                    except: # client left
                        continue

        self.server_socket.close()

    @staticmethod
    def check_username_challenge(message):
        pattern = re.compile('(\[.*\])(.*)')
        match = re.match(pattern, message)

        return bool(match is not None)

    @staticmethod
    def check_timestamp_challenge(message):
        pattern = re.compile(r'(.*)(- Sent at )([0-9][0-9]):([0-9][0-9]):([0-9][0-9])$')
        match = re.match(pattern, message)

        return bool(match is not None)

    def show_points(self):
        point_string = 'Your Room\'s Points: {}'.format(self.points)
        space_string = ' '*int((80 - len(point_string)) / 2)

        print(colored('='*80, 'blue', attrs=['bold']))
        print(colored('{}{}'.format(space_string, point_string), 'blue', attrs=['bold']))
        print(colored('='*80, 'blue', attrs=['bold']))
        print('\r')

if __name__ == '__main__':
    im_server = IMServer('0.0.0.0', 9999)
    im_server.start()
