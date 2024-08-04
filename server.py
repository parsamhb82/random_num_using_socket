import socket
import random
server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_host = socket.gethostbyname(socket.gethostname())
print(server_host)
server_port = 8082
server_socket.bind((server_host, server_port))
server_socket.listen(1)
number = random.randint(1,1000)
while True:
    server_client, addr = server_socket.accept()
    guess = server_client.recv(1024)
    guess = guess.decode()
    if number > guess:
        output = "lower"
    elif number < guess:
        output = "higher"
    else:
        output = "Correct"
    server_client.sendall(output.encode())
    if output == "Correct":
        server_client.close()
        break
    