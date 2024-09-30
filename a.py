import socket

with open('ip.txt', 'r') as file, open('open_ips.txt', 'w') as output:
    for line in file:
        ip = line.split('/')[0].strip()
        sock = socket.socket(socket.AF_INET6 if ':' in ip else socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        if sock.connect_ex((ip, 443)) == 0:
            output.write(ip + '\n')
        sock.close()