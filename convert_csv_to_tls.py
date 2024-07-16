import csv
import sys

def convert_csv_to_tls(csv_filename, TLS, notls=False):
    transformed_data = []
    output_filename = notls if notls else TLS
    with open(csv_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            if notls:
                formatted_ip = f"{row[0]}:80#自动优选快速-[使用本节点时请勿访问/发布色情涉政等非法内容]"
            else:
                formatted_ip = f"{row[0]}:443#自动优选"
            outfile.write(formatted_ip + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    TLS = 'TLS.txt'
    notls = False if len(sys.argv) == 1 else 'notls.txt'
    convert_csv_to_tls(csv_filename, TLS, notls)
