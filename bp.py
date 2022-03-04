import requests
import json
import pprint
import os

from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import sys,time

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

def switch_bp(url, sw_name):
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
                      0:    ae0     (MC-LAG interconnection)
                      1:    ae1     (to access01-blue)
                      2:    ae2     (to access02-grey)
                      3:    ae3     (to access03-green)
                      4:    ae4     (to mgig AP switch)
                      15:   ae15    (to Core)
                      
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
        elif interface_choice == '15':
            interface_name = 'ae15'
        elif interface_choice.upper() == 'Q':
            os._exit(0)
        else:
            invalid_choice()
            continue
        if_ids = len(response_dict['configuration']['interfaces']['interface'])
        for if_id in range(if_ids):
            if (response_dict['configuration']['interfaces']['interface'])[if_id]['name'] == interface_name:
                interface_id = if_id

        os.system('clear')
        print("~" * 80)
        if_dsc = response_dict['configuration']['interfaces']['interface'][interface_id]['description']
        print_one_by_one(
            f"Interface '{interface_name}' (description: '{if_dsc}') on switch \n'{sw_name}' has the following VLAN members: \n")
        print_one_by_one("~" * 80)
        print()
        pprint.pprint(response_dict['configuration']['interfaces']['interface'][interface_id]['unit'][0]['family'][
                          'ethernet-switching']['vlan']['members'])
        print("~" * 80)
        #os._exit(0)
        #break

def bp():
    while True:
        sw_choice = input ("""\nPlease choose which switch you want to check: \n
              1:  dist01.b1f5idf.bp01
              2:  dist02.b1f5idf.bp01
              3:  dist01.b2f2idf.bp01
              4:  dist02.b2f2idf.bp01
              5:  dist01.b2f3idf.bp01
              6:  dist02.b2f3idf.bp01\n
          Your choice: """)
        if sw_choice == '1' :
              url = "https://160.33.125.101:3443/rpc/get-configuration"
              sw_name = 'dist01.b1f5idf.bp01'
              switch_bp(url, sw_name)

        elif sw_choice == '2' :
              url = "https://160.33.125.102:3443/rpc/get-configuration"
              sw_name = 'dist02.b1f5idf.bp01'
              switch_bp(url, sw_name)

        elif sw_choice == '3' or  sw_choice == '4' or  sw_choice == '5' or sw_choice =='6':
            not_ready()

        else:
          invalid_choice()








