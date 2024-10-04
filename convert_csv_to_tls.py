import pandas as pd
import sys

def convert_csv_to_tls(csv_filename, output_filename):
    # 使用pandas读取CSV文件
    df = pd.read_csv(csv_filename, encoding='utf-8')
    # 选取第一列，并且只取前10行
    ips = df.iloc[:, 0].head(10)
    # 将IP地址写入文件，每个IP地址一行
    ips.to_csv(output_filename, index=False, header=False)

# 假设csv_filename为 'result.csv'
csv_filename = 'result.csv'
output_filename = 'notls.txt' if len(sys.argv) > 1 and sys.argv[1] == 'notls' else 'TLS.txt'
convert_csv_to_tls(csv_filename, output_filename)