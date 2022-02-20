#!/usr/bin/python3

from getpass import getpass
import json

import sys
import signal
import os
import time
import https
import requests
from requests import request
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


os.system('clear')
username = input('please input your AD username: ')
password = getpass()
credentials = f'"{username}:{password}"'

os.system('cat /etc/hosts')
hostname = input('please select what device you want to operate: ')
request_headers = '"Content-Type: application/xml"'
response_headers = '"Accept: application/json"'
os.system('cat schema.txt')
schema = input('please select what ops command you want to perform: ')
url_curl = f'https://{hostname}:3443/rpc/{schema} -k -u {credentials} -H {request_headers} -H {response_headers}'
#url_requests = f'https://{hostname}:3443/rpc/{schema} -k -u {credentials} -H {request_headers} -H {response_headers}'
#url_requests = 'scheme://device:port/rpc/get-route-engine-information@format=json', auth=('username', 'password')
print('running......')
scheme = https
#url = https//spsw06:3443/rpc/get-software-information@format=json', auth=('username', 'password')
#request_get = requests.get(scheme//hostname:3443/rpc/get-software-information@format=json', auth=('username', 'password'))
#request_get = requests.get(https//172.19.195.39:3443/rpc/get-software-information@format=json', auth=('username', 'password'))
#request_get = requests.get(https://172.19.195.39:3443/rpc/get-configuration HTTP/1.1 Authorization: Basic amh1MTpIVWppZUAyMDIyMDIyNw==Accept: application/json Content-Type: application/xml)
request_get = requests.get(https://172.19.195.39:3443/rpc/get-configuration HTTP/1.1 Authorization: Basic amh1MTpIVWppZUAyMDIyMDIyNw==Accept: application/json Content-Type: application/xml)
print(request_get)
#os.system('curl https://172.19.195.39:3443/rpc/get-configuration -k -u "jhu1:ad_credentials" -H "Content-Type: application/xml" -H "Accept: application/json"')