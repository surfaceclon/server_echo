class ClientOb(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def CliConnect(self):
        cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli.connect((self.host, self.port))
        cli.send(b'Client-server')
        data = cli.recv(1024)
        print(data)
        cli.close()

if __name__=='__main__':
    import socket
    HOST = '127.0.0.1'
    PORT = 5500
    obj = ClientOb(HOST, PORT)
    obj.CliConnect()