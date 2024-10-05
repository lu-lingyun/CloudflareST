import socket
import time

def measure_speed(ip, port=443, data_size=1024*1024):  # 默认发送1MB的数据
    sock = socket.socket(socket.AF_INET6 if ':' in ip else socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    try:
        start_time = time.time()
        sock.connect((ip, port))

        # 模拟上传数据
        data = b'x' * data_size  # 创建要上传的数据
        sock.sendall(data)  # 上传数据

        upload_end_time = time.time()
        upload_time = upload_end_time - start_time
        upload_speed = data_size / upload_time / (1024 * 1024)  # 计算上传速度 (MB/s)

        # 模拟下载数据
        received_data = b''
        while len(received_data) < data_size:
            packet = sock.recv(4096)  # 每次接收4096字节
            if not packet:
                break
            received_data += packet

        download_end_time = time.time()
        download_time = download_end_time - upload_end_time
        download_speed = len(received_data) / download_time / (1024 * 1024)  # 计算下载速度 (MB/s)

        return upload_speed, download_speed
    finally:
        sock.close()

with open('TLS.txt') as file, open('open_ips.txt', 'w') as output:
    for line in file:
        ip = line.split('/')[0].strip()
        try:
            upload_speed, download_speed = measure_speed(ip)
            output.write(f"{ip} - Upload Speed: {upload_speed:.2f} MB/s, Download Speed: {download_speed:.2f} MB/s\n")
        except Exception as e:
            output.write(f"{ip} - Error: {e}\n")
