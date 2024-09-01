import csv
import requests

def get_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        return data['countryCode'] if data['status'] == 'success' else None
    except requests.RequestException:
        return None

def convert_csv_to_tls(csv_filename, output_filename, notls=False):
    with open(csv_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row
        for row in reader:
            ip = row[0]
            countryCode = get_location(ip)
            variable = f"[{countryCode}]" if countryCode else "[位置获取失败]"
            port = ":443" if not notls else ":80"
            formatted_ip = f"{ip}{port}#{variable}-自动优选"
            if notls:
                formatted_ip += "-自动优选快速-[使用本节点时请勿访问/发布色情涉政等非法内容]"
            outfile.write(formatted_ip + '\n')

if __name__ == "__main__":
    csv_filename = 'result.csv'
    convert_csv_to_tls(csv_filename, 'TLS.txt')