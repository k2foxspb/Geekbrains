import requests

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


with open('log', encoding='utf-8') as f:
    while True:
        print(pars(f.readline()))
