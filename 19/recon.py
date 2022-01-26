import requests

headers = {'Authorization': 'Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=='}



tests = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb', 'ab', 'ba'] # some characters to test

for test in tests:
    url = 'http://natas19.natas.labs.overthewire.org/index.php?username={}&password={}'.format(test, test)
    r = requests.post(url, headers=headers)
    print(test+'\t--> '+bytes.fromhex(r.cookies['PHPSESSID']).decode('ascii'))