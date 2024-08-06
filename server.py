import socket
import random
server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_host = socket.gethostbyname(socket.gethostname())
print(server_host)
server_port = 8082
server_socket.bind((server_host, server_port))
number = random.randint(1,1000)
print(number)
server_socket.listen()
socket_client, addr = server_socket.accept()
while True:
    guess = socket_client.recv(1024)
    guess = int(guess.decode())
    if number < guess:
        output = "lower"
    elif number > guess:
        output = "higher"
    else:
        output = "Correct"
    socket_client.sendall(output.encode())
    if output == "Correct":
        socket_client.close()
        break
    