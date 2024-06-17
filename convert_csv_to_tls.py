#!/usr/bin/env python3

import csv

# 函数定义开始
def convert_csv_to_tls():
    # 定义CSV和输出文件的名称
    csv_filename = 'result.csv'
    output_filename = 'TLS.txt'
    
    # 存储转换后的数据
    transformed_data = []

    # 读取CSV文件并转换数据
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  # 跳过标题行
        for row in reader:
            original_ip = row[0]
            formatted_ip = f"{original_ip}:443#测试节点【请勿测速】"
            transformed_data.append(formatted_ip)

    # 写入转换后的数据到新文件
    with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
        for data in transformed_data:
            outfile.write(data + '\n')

# 主程序入口
if __name__ == "__main__":
    convert_csv_to_tls()