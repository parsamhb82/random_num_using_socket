import socket
server_host = input("enter the server host : ")
server_port = int(input("enter the server port : "))

server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_client.connect((server_host, server_port))

while True:
    number = int(input("give a number between 1 - 1000"))
    server_client.sendall(number.encode())
    output = server_client.recv(1024)
    output = output.decode()
    print(output)
    if output == "Correct":
        server_client.close()
        break


