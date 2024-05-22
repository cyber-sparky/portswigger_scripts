import requests
from bs4 import BeautifulSoup
import os
# Lab Url
# https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history

# Enter URL
host = input('Enter Host without "/" in the end: ')
git_endpoint = "/.git"
# i need to download the git using wget -r host/.git and go to that downloaded directory and do git log and go to the first commit and get the admin password 
# it will look like this: +ADMIN_PASSWORD=3iezp40gnrj31jrad0h1

#this is a blocker since i dont know how to do this using python