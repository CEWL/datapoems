import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import urllib.request
from bs4 import BeautifulSoup
import config

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def get_poem(max_characters, url):
    opener = AppURLopener()
    response = opener.open(url)
    html = response.read()

    s = BeautifulSoup(html, 'html.parser')
    a=''
    poem = s.find_all('div', attrs={'style': 'text-indent: -1em; padding-left: 1em;'})
    for text in poem:
        b = text.get_text()
        a += ' '
        a += b

    a = process_poem(a)
    print(a)

def process_poem(str):
    #Remove html formatting
    str = str.replace("\xa0", '')
    str = str.replace("\r", '')
    str = str.replace("', '",'')

    #Remove punctuation
    str = str.replace(".", '')
    str = str.replace(",", '')
    str = str.replace("?", '')
    str = str.replace("!", '')
    str = str.replace("'", '')
    str = str.replace('"', '')
    str = str.replace(":", '')
    str = str.replace(";", '')
    str = str.replace("-", '')
    str = str.replace("–", '')
    str = str.replace("—", '')
    str = str.replace("—", '')
    str = str.replace("(", '')
    str = str.replace(")", '')
    str = str.replace("/", '')
    str = str.replace("&", 'and')


    #Remove extra spaces
    while "  " in str:
        str = str.replace("  ", " ")

    #Make lowercase
    str = str.lower()

    #Remove first character (will always be a space)
    str = str[1:]

    return str

def get_themes(total_themes, url):
    opener = AppURLopener()
    response = opener.open(url)
    html = response.read()

    s = BeautifulSoup(html, 'html.parser')
    themes = s.find('meta', attrs={'property': 'article:tag'})
    text = themes['content']

    themes_list=process_themes(text)

    final_themes = []
    for i in themes_list:
        if i in total_themes and i not in final_themes:
            final_themes.append(i)

    print(final_themes)


def process_themes(str):
    str = str.replace(' ', 'placeholder')
    str = str.replace(',', ' ')

    list = str.split()

    list = [e.replace('placeholder', ' ') for e in list]
    list = [e.lower() for e in list]


    return list




get_poem(config.max_characters, 'https://www.poetryfoundation.org/poetrymagazine/poems/149694/apostrophe')
get_themes(config.themes, 'https://www.poetryfoundation.org/poetrymagazine/poems/149694/apostrophe')
