class ServerOb(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def SerConnect(self):
        ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser.bind((self.host, self.port))
        ser.listen(1)
        while True:
            print('Server-echo...')
            clisock, (clihost, cliport) = ser.accept()
            str = clisock.recv(1024)
            print('Connect: Host {host} Port {port}'.format(host = clihost, port = cliport))
            clisock.send(str + b' back')
            clisock.close()

if __name__=='__main__':
    import socket
    HOST = '127.0.0.1'
    PORT = 5500
    obj = ServerOb(HOST, PORT)
    obj.SerConnect()
