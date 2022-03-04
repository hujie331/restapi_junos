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
import sys,time
# from urllib3.exceptions import MaxRetryError
# from urllib3.exceptions import SSLError
# from urllib3.exceptions import SecurityWarning
os.system('clear')

def not_ready():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print_one_by_one("~ The switch you selected has not enabled restapi yet. Please try again. ~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print()

def invalid_choice():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print_one_by_one("      ~ Invalid Choice. Please try again. Thank you! ~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print()

def print_one_by_one(text):
    sys.stdout.write("\r " + " " * 60 + "\r")
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def switch_sjca(url, sw_name):
    payload = {}
    headers = {
        'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
        'Accept': 'application/json',
        'Content-Type': 'application/xml'
    }

    response = requests.request("GET", url, verify=False, headers=headers, data=payload)
    response_dict = response.json()
    while True:
        interface_choice = input("""\nPlease choose which interface you want to check: \n
                      0:    ae0
                      1:    ae1
                      2:    ae2
                      3:    ae3
                      4:    ae4
                      5:    ae5
                      6:    ae6
                      7:    ae7
                      8:    ae8
                      9:    ae9
                      10:   ae10
                      11:   ae11
                      12:   ae12
                      13:   ae13
                      14:   ae14
                      15:   ae15
                      16:   ae16
                      17:   ae17
                      18:   ae18
                      19:   ae19
                      20:   ae20
                      21:   ae21
                      22:   ae22
                      23:   ae23
                      24:   ae24
                      
                      Q:    Quit\n       
                  Your choice: """)

        if interface_choice == '0':
            interface_name = 'ae0'
        elif interface_choice == '1':
            interface_name = 'ae1'
        elif interface_choice == '2':
            interface_name = 'ae2'
        elif interface_choice == '3':
            interface_name = 'ae3'
        elif interface_choice == '4':
            interface_name = 'ae4'
        elif interface_choice == '5':
            interface_name = 'ae5'
        elif interface_choice == '6':
            interface_name = 'ae6'
        elif interface_choice == '7':
            interface_name = 'ae7'
        elif interface_choice == '8':
            interface_name = 'ae8'
        elif interface_choice == '9':
            interface_name = 'ae9'
        elif interface_choice == '10':
            interface_name = 'ae10'
        elif interface_choice == '11':
            interface_name = 'ae11'
        elif interface_choice == '12':
            interface_name = 'ae12'
        elif interface_choice == '13':
            interface_name = 'ae13'
        elif interface_choice == '14':
            interface_name = 'ae14'
        elif interface_choice == '15':
            interface_name = 'ae15'
        elif interface_choice == '16':
            interface_name = 'ae16'
        elif interface_choice == '17':
            interface_name = 'ae17'
        elif interface_choice == '18':
            interface_name = 'ae18'
        elif interface_choice == '19':
            interface_name = 'ae19'
        elif interface_choice == '20':
            interface_name = 'ae20'
        elif interface_choice == '21':
            interface_name = 'ae21'
        elif interface_choice == '22':
            interface_name = 'ae22'
        elif interface_choice == '23':
            interface_name = 'ae23'
        elif interface_choice == '24':
            interface_name = 'ae24'
        elif interface_choice.lower() == 'q':
            os._exit(0)
        else:
            invalid_choice()
            continue


        # print(type(response.json()))
        # print(type(response_dict))
        # print(type(response.text))

        # pprint.pprint(response_dict['configuration'])
        # pprint.pprint(response_dict['configuration']['@'])
        # pprint.pprint(response_dict['configuration']['chassis'])
        # pprint.pprint(response_dict['configuration']['forwarding-options']['storm-control-profiles'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'])
        # print(response.text)
        # pprint.pprint(response_dict['configuration']['interfaces']['interface']['family']['unit'][0]['family']['inet']['dhcp']['vendor-id'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][8]['unit'][0]['family']['inet']['dhcp']['vendor-id'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][125])  # interface ae0
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][125]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][126]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][127]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][128]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][129]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][130]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][131]['name'])
        # pprint.pprint(response_dict['configuration']['interfaces']['interface'][132]['name'])
        # pprint.pprint(response_dict)

        print(len(response_dict['configuration']['interfaces']['interface']))
        if_ids = len(response_dict['configuration']['interfaces']['interface'])
        for if_id in range(if_ids):
            if (response_dict['configuration']['interfaces']['interface'])[if_id]['name'] == interface_name:
                interface_id = if_id

        os.system('clear')
        print("~" * 80)
        if_dsc = response_dict['configuration']['interfaces']['interface'][interface_id]['description']
        print_one_by_one(
            f"Interface '{interface_name}' (description: '{if_dsc}') on \nswitch '{sw_name}' has the following VLAN members: \n")
        print_one_by_one("~" * 80 )
        print()
        pprint.pprint(response_dict['configuration']['interfaces']['interface'][interface_id]['unit'][0]['family'][
                          'ethernet-switching']['vlan']['members'])
        print("~" * 80)

        # (response_dict['configuration']['interfaces']['interface'][interface_id]['name'])

        # os._exit(0)
        # break


def sjca():
    while True:
        sw_choice = input ("""\nPlease choose which switch you want to check: \n
              1:  leaf-access01.corp.sjca
              2:  leaf-access02.corp.sjca
              3:  leaf-access03.corp.sjca
              4:  leaf-access04.corp.sjca
              5:  leaf-access05.corp.sjca
              6:  leaf-access06.corp.sjca:
              7:  leaf-access07.corp.sjca
              8:  leaf-access08.corp.sjca\n       
          Your choice: """)
        if sw_choice == '1' :
          url = "https://172.19.195.39:3443/rpc/get-configuration"
          sw_name = 'leaf-access01.corp.sjca'
          switch_sjca(url, sw_name)

        elif sw_choice == '2' :
          url = "https://172.19.195.39:3443/rpc/get-configuration"
          sw_name = 'leaf-access02.corp.sjca'
          switch_sjca(url, sw_name)

        elif sw_choice == '3' or sw_choice == '4' or sw_choice == '5' or sw_choice == '6' or sw_choice == '7' or sw_choice == '8' :
            not_ready()

        else:
          invalid_choice()










