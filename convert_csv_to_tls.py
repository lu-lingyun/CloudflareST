import pandas as pd
import sys

def convert_csv_to_tls(csv_filename, output_filename):
    pd.read_csv(csv_filename, encoding='utf-8').iloc[:, 0].to_csv(output_filename, index=False, header=False)

csv_filename = 'result.csv'
output_filename = 'notls.txt' if len(sys.argv) > 1 and sys.argv[1] == 'notls' else 'TLS.txt'
convert_csv_to_tls(csv_filename, output_filename)