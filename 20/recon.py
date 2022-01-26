import requests
from bs4 import BeautifulSoup

headers = {'Authorization': 'Basic bmF0YXMyMDplb2ZtM1dzc2h4YzVid3RWbkV1R0lscjdpdmI5S0FCRg=='}

testnames = ['admin','admin','admin','admin']

for name in testnames:
    url = 'http://natas20.natas.labs.overthewire.org/index.php?name={}'.format(name)
    r = requests.post(url, headers=headers)
    print(name+'\t--> '+r.cookies['PHPSESSID'])