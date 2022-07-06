import requests
from collections import Counter

URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

req = requests.get(URL)
with open('log', 'a', encoding='utf-8') as f:
    f.write(req.text)


def pars(log_line):
    remote_addr, log_line = log_line.split(' - - ')
    other, log_line = log_line.split(']')
    request_type, log_line = log_line.split(' /')
    request_type = request_type.lstrip(' "')
    requested_resource, log_line = log_line.split(' HTTP')
    return remote_addr, request_type, requested_resource


def pars_ip(log_line):
    remote_addr, log_line = log_line.split(' - - ')
    other, log_line = log_line.split(']')
    return remote_addr


with open('log', encoding='utf-8') as f:
    try:
        while True:
            print(pars(f.readline()))
    except ValueError:
        print('ValueError')

with open('log', encoding='utf-8') as f:
    ip = []
    for i in f:
        pars_line_1 = pars_ip(f.readline())
        ip.append(pars_line_1)
    print(Counter(ip).most_common(1), '-спамер')
