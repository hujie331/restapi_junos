
import requests

url = "http://172.19.195.39:3000/rpc/get-configuration"

payload={}
headers = {
  'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
  'Accept': 'application/json',
  'Content-Type': 'application/xml'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)