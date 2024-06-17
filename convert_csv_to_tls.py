import csv

def convert_csv_to_tls(csv_filename, output_filename):
    transformed_data = []
    with open(csv_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            formatted_ip = f"{row[0]}:443#自动优选IP"
            outfile.write(formatted_ip + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    output_filename = 'TLS.txt'
    convert_csv_to_tls(csv_filename, output_filename)