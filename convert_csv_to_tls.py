import csv

def convert_csv_to_tls(csv_filename, output_filename):
    transformed_data = []
    with open(csv_filename, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header
        for original_ip in reader:
            formatted_ip = f"{original_ip[0]}:443#测试节点请勿测速"
            transformed_data.append(formatted_ip)

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for data in transformed_data:
            outfile.write(data + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    output_filename = 'TLS.txt'
    convert_csv_to_tls(csv_filename, output_filename)