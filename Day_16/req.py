import requests
from requests_html import HTMLSession


session = HTMLSession()
r = session.get('https://python.org/')

# print(r.html.links)
print(r.html.search('Python is a {} language')[0])

# # payload = {'username': 'John', 'password': 'testing@123'}
# r = requests.get('https://httpbin.org/get', data=payload)
# print(r.text)

