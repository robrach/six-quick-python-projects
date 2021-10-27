import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github user name: ')
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image_link = soup.find('img', {'alt': 'Avatar'})['src']
print('Here is the link to ' + github_user + ' avatar:\n' + profile_image_link)