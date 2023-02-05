#import requests library
import requests
from requests.auth import HTTPBasicAuth


# request sending without authentication details
# r = requests.get('http://httpbin.org/')

#basic authentication - request building
# r = requests.get('https://httpbin.org/basic-auth/user/pass',auth=HTTPBasicAuth('user','pass'))


#Bearer authentication (also called token authentication)

token = 'LonKingxx'
headers = { 
    "Authorization": f"Bearer {token}" 
    }     
r = requests.get("https://httpbin.org/bearer",headers=headers)


print(r.status_code)
print(r.url)
