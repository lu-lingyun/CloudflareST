#!/usr/bin/env python3
# 文件名: convert_csv_to_tls.py

import csv
import os

# 函数定义开始
def convert_csv_to_tls():
    # 定义CSV和输出文件的名称
    csv_filename = 'result.csv'
    output_filename = 'TLS.txt'
    
    # 检查CSV文件是否存在
    if not os.path.isfile(csv_filename):
        print(f"错误：文件 {csv_filename} 不存在。")
        return
    
    # 存储转换后的数据
    transformed_data = []

    # 读取CSV文件并转换数据
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        # 跳过标题行
        next(reader)
        
        for row in reader:
            # 假设第一列是IP地址
            original_ip = row[0]
            # 格式化IP地址和注释
            formatted_ip = f"{original_ip}:443#测试节点【请勿测速】"
            transformed_data.append(formatted_ip)

    # 写入转换后的数据到新文件
    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        for data in transformed_data:
            outfile.write(data + '\n')

    print("数据转换完成，并已写入到新文件TLS.txt。")

# 主程序入口
if __name__ == "__main__":
    convert_csv_to_tls()
