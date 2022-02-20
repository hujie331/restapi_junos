
import os

# curl --location --request GET 'https://172.19.195.39:3443/rpc/get-configuration' \
# --header 'Authorization: Basic amh1MTpIVWppZUAyMDIyMDIyNw==' \
# --header 'Accept: application/json' \
# --header 'Content-Type: application/xml'

curl_var = 'curl https://172.19.195.39:3443/rpc/get-configuration -k -u "jhu1:HUjie@20220227" -H "Content-Type: application/xml" -H "Accept: application/json"'
curl_var2 = os.system(curl_var)