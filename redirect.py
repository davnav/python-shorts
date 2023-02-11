# import python request library
import requests

# send the get request to httpbin re-direct url with site we need to connect to 
# in this case we need https://httpbin.org/

# we need to step up the parameters as mentioned in the httpbin
payload = { 'url':'https://www.google.com/',
            'status_code': 302 }

# sending the get request to the re-direct url
r = requests.get('https://httpbin.org/redirect-to',params  = payload)

#status of the response
print(r.status_code)

# display the direct url history
for u in r.history:
    print(u.url)

# actual response url
print(r.url)

# actual content returned in the response
print(r.content)