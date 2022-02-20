
import requests
import json
import pprint
#import urllib3
# import warnings
# import contextlib
# import ssl
# import urllib.request

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# from urllib3.exceptions import MaxRetryError
# from urllib3.exceptions import SSLError
# from urllib3.exceptions import SecurityWarning

url = "https://172.19.195.39:3443/rpc/get-configuration"

payload={}
headers = {
  'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
  'Accept': 'application/json',
  'Content-Type': 'application/xml'
}

response = requests.request("GET", url, verify = False, headers=headers, data=payload)
response_dict = response.json()
#print(type(response.json()))
#print(type(response_dict))
# print(type(response.text))
#pprint.pprint(response_dict)
#pprint.pprint(response_dict['configuration'])
# pprint.pprint(response_dict['configuration']['@'])
# pprint.pprint(response_dict['configuration']['chassis'])
#pprint.pprint(response_dict['configuration']['forwarding-options']['storm-control-profiles'])
#pprint.pprint(response_dict['configuration']['interfaces']['interface'])
pprint.pprint(response_dict['configuration']['interfaces']['interface'][8]['unit'][0]['family']['inet']['dhcp']['vendor-id'])
#print(response.text)