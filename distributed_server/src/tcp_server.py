import socket
import json

HOST = "164.41.98.26"
PORT = 10055


def start_tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            try:
                print(f"Connected by {addr}")
                while True:
                    print("Aguardando mensagem")
                    data = conn.recv(1024)
                    # received = sock.recv(1024)
                    received = str(data.decode("utf-8"))
                    if(len(received)) > 0:
                        print("Mensagem Recebida")
                        print("Mensagem: " + str(received))
                        return eval(received)
                    if not data:
                        break
                    conn.sendall(data)
            except Exception as err:
                conn.close()
                print("Erro: " + str(err))