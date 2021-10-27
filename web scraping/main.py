import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github user name: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
print(soup)