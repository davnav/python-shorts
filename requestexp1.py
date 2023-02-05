# import request library
import requests;

#setting the headers for http request
headers = { 'user-agent': 'myapp/0.0.1','val':'1'}
# send the get request
r = requests.get('https://httpbin.org/',headers=headers);

print(r.request.headers)
print(r.url)
#print the status code
print(r.status_code)
print(r.headers)
#print the attributes of response
# print(dir(r))

#print help for response
# print(help(r))

#print the content of the response
print(r.content)


# creating a payload
payload = {'key1':['value1','value2']}

# url will be something like  https://httpbin.org/post?key1=value1&key1=value2
r1 = requests.post('https://httpbin.org/post',params=payload)

print(r1.url)





