import csv
import sys
import requests

def get_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            return data['countryCode']
        else:
            return None
    except requests.RequestException as e:
        print(f"Error getting location for IP {ip}: {e}")
        return None

def convert_csv_to_tls(csv_filename, TLS, notls=False):
    output_filename = 'notls.txt' if notls else TLS
    with open(csv_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row
        for row in reader:
            ip = row[0]
            countryCode = get_location(ip)
            if countryCode:
                variable = f"[{countryCode}]"
            else:
                variable = "[位置获取失败]"

            if notls:
                formatted_ip = f"{ip}:80#{variable}-自动优选快速-[使用本节点时请勿访问/发布色情涉政等非法内容]"
            else:
                formatted_ip = f"{ip}:443#{variable}-自动优选"

            outfile.write(formatted_ip + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    TLS = 'TLS.txt'
    notls = False if len(sys.argv) < 2 else 'notls.txt'
    convert_csv_to_tls(csv_filename, TLS, notls)