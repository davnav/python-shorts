# import request library
import requests;

# send the get request
r = requests.get('https://httpbin.org/');

#print the status code
print(r.status_code)

#print the attributes of response
print(dir(r))

#print help for response
# print(help(r))

#print the content of the response
print(r.content)




