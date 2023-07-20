import socket

ip = 'ip'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    for port in range(100, 65500):
        try:
            s.connect((ip, port))
            print(f'port {port} is open')
        except:
            print(f'port {port} is not open')