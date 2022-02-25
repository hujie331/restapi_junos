
import requests
import json
import pprint
import os
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
os.system('clear')
sw_choice = input ("""\nPlease choose which switch you want to check: \n
        1:  leaf-access01.corp.sjca
        2:  leaf-access02.corp.sjca\n       
    Your choice: """)
if sw_choice == '1' :
  url = "https://172.19.195.39:3443/rpc/get-configuration"
  sw_name = 'leaf-access01.corp.sjca'
else :
  url = "https://172.19.195.39:3443/rpc/get-configuration"
  sw_name = 'leaf-access02.corp.sjca'


if_choice = input("""\nPlease choose which interface you want to check: \n
        0:  ae0
        1:  ae1
        2:  ae2
        3:  ae3
        4:  ae4
        5:  ae5
        6:  ae6
        7:  ae7\n       
    Your choice: """)
if if_choice == '0':
#  interface_id = int('125')
  interface_name = 'ae0'
elif if_choice == '1':
#  interface_id = int('126')
  interface_name = 'ae1'
elif if_choice == '2':
#  interface_id = int('127')
  interface_name = 'ae2'
elif if_choice == '3':
#  interface_id = int('128')
  interface_name = 'ae3'
elif if_choice == '4':
#  interface_id = int('129')
  interface_name = 'ae4'
elif if_choice == '5':
#  interface_id = int('130')
  interface_name = 'ae5'
elif if_choice == '6':
#  interface_id = int('131')
  interface_name = 'ae6'
else:
#  interface_id = int('132')
  interface_name = 'ae7'

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

#pprint.pprint(response_dict['configuration'])
# pprint.pprint(response_dict['configuration']['@'])
# pprint.pprint(response_dict['configuration']['chassis'])
#pprint.pprint(response_dict['configuration']['forwarding-options']['storm-control-profiles'])
#pprint.pprint(response_dict['configuration']['interfaces']['interface'])
#print(response.text)
#pprint.pprint(response_dict['configuration']['interfaces']['interface']['family']['unit'][0]['family']['inet']['dhcp']['vendor-id'])
#pprint.pprint(response_dict['configuration']['interfaces']['interface'][8]['unit'][0]['family']['inet']['dhcp']['vendor-id'])
#pprint.pprint(response_dict['configuration']['interfaces']['interface'][125])  # interface ae0
#pprint.pprint(response_dict['configuration']['interfaces']['interface'][125]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][126]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][127]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][128]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][129]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][130]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][131]['name'])
# pprint.pprint(response_dict['configuration']['interfaces']['interface'][132]['name'])
#pprint.pprint(response_dict)

print(len(response_dict['configuration']['interfaces']['interface']))
if_ids = len(response_dict['configuration']['interfaces']['interface'])
for if_id in range(if_ids):
  if (response_dict['configuration']['interfaces']['interface'])[if_id]['name'] == interface_name:
    interface_id = if_id

os.system('clear')
print ("~" * 80)
if_dsc = response_dict['configuration']['interfaces']['interface'][interface_id]['description']
print(f"Interface '{interface_name}' (description: '{if_dsc}') on switch '{sw_name}' has the following VLAN members: \n")
pprint.pprint(response_dict['configuration']['interfaces']['interface'][interface_id]['unit'][0]['family']['ethernet-switching']['vlan']['members'])
print ("~" * 80)


#(response_dict['configuration']['interfaces']['interface'][interface_id]['name'])



