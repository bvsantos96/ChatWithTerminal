import socket
import logging

logging.basicConfig(level=logging.INFO)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 80))
server_socket.listen(1)

logging.info("Server listening in port %s...." % server_socket.getsockname()[1])

connectedClients = dict()

server_socket.listen()
logging.info("Waiting for client connection...")
sock, addr = server_socket.accept()
connectedClients[addr] = sock;
logging.info("Connected to client...")
# infinite loop listening into incoming requests
# while True:

server_socket.close()
