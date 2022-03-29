# decoders for the query string
from urllib.parse import quote_plus, unquote
import base64

# HTTP requests
import requests

# math stuff to make the loop work
import math

# headers for authorization
headers = {'Authorization': 'Basic bmF0YXMyODpKV3dSNDM4d2tnVHNOS0JiY0pvb3d5eXNkTTgyWWplRg=='}
# base URL
url = 'http://natas28.natas.labs.overthewire.org/index.php?query='

# setting the payload
print('enter payload string: ')
string = input()
chars = list()

# split payload into characters
for char in string:
    chars += char

# print first part of hex with 10 spaces
spaces = '+'*10
r = requests.post(url+spaces, headers=headers)
query = r.url[60:] # query response from server starts at 60th character of response url.
for j in range(math.ceil(len(base64.b64decode(unquote(query))[:48])/16)):
    print(base64.b64decode(unquote(query))[j*16:j*16+16].hex(' ')) # print the rest of the returned query

# split the payload into 16 byte lines
for i in range(math.ceil(len(string)/16)): # first iteration
    if i == 0:
        payload = ' '*9+'\"'+''.join(chars[0:15])
        payload = quote_plus(payload) # url encode payload
        r = requests.post(url+payload, headers=headers)
        query = r.url[60:]
        print(base64.b64decode(unquote(query))[48:64].hex(' '))

    if i > 0 and i < math.ceil(len(string)/16)-1:
        x = i*16 - 1
        y = x + 16
        payload = '+'*10+''.join(chars[x:y])
        payload = quote_plus(payload) 
        r = requests.post(url+payload, headers=headers)
        query = r.url[60:]
        print(base64.b64decode(unquote(query))[48:64].hex(' '))

    if i == math.ceil(len(string)/16)-1: # last iteration
        x = i*16 - 1
        y = x + 16
        payload = '+'*10+''.join(chars[x:y])
        payload = quote_plus(payload) 
        r = requests.post(url+payload, headers=headers)
        query = r.url[60:]
        
        # range is the length of query from position 48 to the end, divided by 16, rounded up
        # this splits the result into nicely formatted 16 hex byte blocks
        for j in range(math.ceil(len(base64.b64decode(unquote(query))[48:])/16)):
            print(base64.b64decode(unquote(query))[48+j*16:64+j*16].hex(' ')) 