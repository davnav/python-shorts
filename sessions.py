# import request library
import requests

# creating auth variable
auth = ('user','pass')

#creating a custom header
header = { 'name': 'naveendavis'}

# creating session object
s = requests.session()

# setting session auth
s.auth = auth

# updating session header
s.headers.update(header)

# get request to httpbin.org
r = s.get('https://httpbin.org/headers')

# printing the session object
print(s)

# printing session header
print(s.headers)

# printing response
print(r.status_code)


# second get request to httpbin.org
r1 = s.get('https://httpbin.org/')

# second request - printing session headers
print(s.headers)

# second request - printing response status
print(r1.status_code)

#third request - stand alone
r3 = requests.get('https://httpbin.org')

print(r3.status_code)





