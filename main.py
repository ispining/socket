import socket


hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(IP)
server = socket.socket(

    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind(('localhost', 1234))
server.listen(5)

while True:
    user_socket, addres = server.accept()
    text = ''
    user_socket.send(text.encode('utf-8'))