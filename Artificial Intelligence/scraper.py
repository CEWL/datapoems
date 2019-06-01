import func
import numpy as np
import config
import pandas as pd
import requests
from bs4 import BeautifulSoup

poem_data = []
themes_data = []


url = 'https://www.poetryfoundation.org/poems/browse#page=1&sort_by=recently_added'
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
s = BeautifulSoup(page.text, "html.parser")
list_urls_string = s.find_all('h2', attrs={'class': 'c-hdgSans c-hdgSans_2'})

print(s)

'''
list_string = list_urls_string.split()
list_urls = []
for s in list_string:
    if 'https://www.poetryfoundation.org/poetrymagazine/poems' in s:
        last_index = s.rfind('"') - 1
        first_index = 6
        list_urls.append(s[first_index:last_index])

print(list_urls)
print(len(list_urls))
'''
