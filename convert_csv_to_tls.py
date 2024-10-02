import csv
import requests
import sys

def convert_csv_to_tls(csv_filename, output_filename, notls=False):
    with open(csv_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            ip = row[0]
            formatted_ip = f"{ip}"
            outfile.write(formatted_ip + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    output_filename = 'notls.txt' if len(sys.argv) > 1 and sys.argv[1] == 'notls' else 'TLS.txt'
    convert_csv_to_tls(csv_filename, output_filename, notls=(output_filename == 'notls.txt'))