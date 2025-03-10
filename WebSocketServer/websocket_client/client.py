import socket
import logging

logging.basicConfig(level=logging.INFO)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8081))
server_socket.connect(("127.0.0.1", 8080))

