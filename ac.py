import socket
import time

def 测量速度(ip, port=443, data_size=1024*1024):  # 默认发送1MB的数据
    sock = socket.socket(socket.AF_INET6 if ':' in ip else socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    try:
        开始时间 = time.time()
        sock.connect((ip, port))

        # 模拟上传数据
        数据 = b'x' * data_size  # 创建要上传的数据
        sock.sendall(数据)  # 上传数据

        上传结束时间 = time.time()
        上传时间 = 上传结束时间 - 开始时间
        上传速度 = data_size / 上传时间 / (1024 * 1024)  # 计算上传速度 (MB/s)

        # 模拟下载数据
        接收数据 = b''
        while len(接收数据) < data_size:
            数据包 = sock.recv(4096)  # 每次接收4096字节
            if not 数据包:
                break
            接收数据 += 数据包

        下载结束时间 = time.time()
        下载时间 = 下载结束时间 - 上传结束时间
        下载速度 = len(接收数据) / 下载时间 / (1024 * 1024)  # 计算下载速度 (MB/s)

        return 上传速度, 下载速度
    finally:
        sock.close()

with open('TLS.txt') as 文件, open('open_ips.txt', 'w') as 输出:
    for 行 in 文件:
        ip = 行.split('/')[0].strip()
        try:
            上传速度, 下载速度 = 测量速度(ip)
            输出.write(f"{ip}\n")
        except Exception as e:
            pass  # 忽略错误，不写入输出文件
