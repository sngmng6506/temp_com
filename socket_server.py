

import socket



def RequestFromServer(SERVER_IP):
    PORT = 1097
    MAX_SIZE = 1024
    ADDR = (SERVER_IP, PORT)

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind(ADDR)
        server_socket.listen()

        while True:
            client_socket, client_addr = server_socket.accept()
            msg = client_socket.recv(MAX_SIZE)
            print("[{}] message : {}".format(client_addr,msg))
            YOUTUBE_URL  = msg.decode('utf-8')

            client_socket.sendall("connecting_success".encode())
            client_socket.close()
            return YOUTUBE_URL
        ##다중접속을위한 스레드 추후추가

SERVER_IP = socket.gethostbyname(socket.gethostname())   ##본인 컴퓨터 연결된 와이파이 주소 ipv4 // 5G든 그냥이든 똑같음
RequestFromServer(SERVER_IP)
