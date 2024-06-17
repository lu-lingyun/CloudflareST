import csv

def convert_csv_to_tls():
    csv_filename = 'result.csv'
    output_filename = 'TLS.txt'
    
    transformed_data = []
    with open(csv_filename, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            original_ip = row[0]
            formatted_ip = f"{original_ip}:443#测试节点请勿测速"
            transformed_data.append(formatted_ip)

    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        for data in transformed_data:
            outfile.write(data + '\n')

if __name__ == "__main__":
    convert_csv_to_tls()