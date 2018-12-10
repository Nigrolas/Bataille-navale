import socket

UDP_IP = "10.160.108.3"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) #buffer size is 1024 bytes
    print ("client:", data.decode())
    MESSAGE = input("réponse :")
    sock.sendto(MESSAGE.encode() ,addr)
