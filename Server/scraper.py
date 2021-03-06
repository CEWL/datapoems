''' Caleb Lammers June 5th
This file is used to create a database of poems with their themes '''

#Import needed libraries
from selenium import webdriver
import func
import numpy as np
import config
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Set whether it is the first time running the scraper
first_time = False

#If it is the first time, create poem data and themes data arrays
if first_time:
    poem_data = []
    themes_data = []

#If it is not the first time, load the poem data and themes data arrays
if not first_time:
    poem_data = np.load('poem_data.npy')
    poem_data = poem_data.tolist()
    themes_data = np.load('themes_data.npy')
    themes_data = themes_data.tolist()


#Function to get a list of URLs which have poems given a url on the browse page (because these pages use react, must use a different library)
def get_poem_urls(url):
    #Open the URL using the chrome webdriver
    browser = webdriver.Chrome()
    browser.get(url)

    #From the open page, get the html text
    innerHTML = browser.execute_script("return document.body.innerHTML")

    parsed_text = BeautifulSoup(innerHTML, "lxml")
    list_urls_string = parsed_text.find_all('h2', attrs={'class': 'c-hdgSans c-hdgSans_2'})

    list_string = str(list_urls_string).split()
    list_urls = []
    for s in list_string:
        if 'https://www.poetryfoundation.org/poetrymagazine/poems/29195' in s:
            break
        if 'https://www.poetryfoundation.org/poetrymagazine/poems' in s or 'https://www.poetryfoundation.org/poems' in s:
            last_index = s.rfind('"')
            first_index = 6
            list_urls.append(s[first_index:last_index])

    return list_urls



start = 330
end = 335
for i in range(start, end):
    url = 'https://www.poetryfoundation.org/poems/browse#page=' + str(i) + '&sort_by=recently_added'
    list_urls = get_poem_urls(url)

    print("URLs:")
    print(list_urls)

    for poem_url in list_urls:

        poem = func.get_poem(config.max_characters, poem_url)
        poem_binary = func.convert_poem_binary(config.max_characters, poem)
        themes = func.get_themes(config.themes, poem_url)
        themes_binary = func.convert_themes(config.themes, themes)
        title = func.get_title(poem_url)
        print("Theme Binary:")
        print(themes_binary)
        print("Poem Binary:")
        print(poem_binary)
        if not themes_binary == '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000' and poem_binary is not None:
            poem_data.append(poem_binary)
            themes_data.append(themes_binary)

            print(len(poem_data))
    if i == (end - 1):
        poem_data = np.array(poem_data)
        themes_data = np.array(themes_data)
        np.save('poem_data.npy', poem_data)
        np.save('themes_data.npy', themes_data)


arr = []
for i in range(len(poem_data)):
    entry = []
    for digit in themes_data[i]:
        entry.append(float(digit))
    for digit in poem_data[i]:
        entry.append(float(digit))
    arr.append(entry)

arr = np.array(arr)
np.save('arr4.npy', arr)

data = np.load('arr4.npy')

print(data.shape)
