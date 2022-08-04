import socket
import json
from utils import get_message

HOST = "164.41.98.26"  
PORT = 10055

def start_client_tcp(modo_noturno, modo_emergencia, modo_normal, modo_debug):
    m = get_message(modo_noturno, modo_emergencia, modo_normal, modo_debug)
    data = json.dumps(m)
    print("Mensagem enviada: " + str(m))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(data,encoding="utf-8"))
        data = s.recv(1024)
    print("Received " + str(data))