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
    a = ''
    poem = s.find_all('div', attrs={'style': 'text-indent: -1em; padding-left: 1em;'})
    for text in poem:
        b = text.get_text()
        a += ' '
        a += b

    a = process_poem(a)
    return a

def process_poem(s):
    #Remove html formatting
    s = s.replace("\xa0", '')
    s = s.replace("\r", '')
    s = s.replace("', '",'')

    #Remove punctuation
    s = s.replace(".", '')
    s = s.replace(",", '')
    s = s.replace("?", '')
    s = s.replace("!", '')
    s = s.replace("'", '')
    s = s.replace('"', '')
    s = s.replace(":", '')
    s = s.replace(";", '')
    s = s.replace("-", '')
    s = s.replace("–", '')
    s = s.replace("—", ' ')
    s = s.replace("—", '')
    s = s.replace("(", '')
    s = s.replace(")", '')
    s = s.replace("/", '')
    s = s.replace("&", 'and')
    s = s.replace("•", '')
    s = s.replace("’", '')

    #replace numbers
    s = s.replace("1", 'one')
    s = s.replace("2", 'two')
    s = s.replace("3", 'three')
    s = s.replace("4", 'four')
    s = s.replace("5", 'five')
    s = s.replace("6", 'six')
    s = s.replace("7", 'seven')
    s = s.replace("8", 'eight')
    s = s.replace("9", 'nine')
    s = s.replace("10", 'ten')


    #Remove extra spaces
    while "  " in s:
        s = s.replace("  ", " ")

    #Make lowercase
    s = s.lower()

    #Remove first and last characters (will always be spaces)
    s = s[1:]
    s=s[:-1]

    return s

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

    return final_themes


def process_themes(s):
    s = s.replace(' ', 'placeholder')
    s = s.replace(',', ' ')

    list = s.split()

    list = [e.replace('placeholder', ' ') for e in list]
    list = [e.lower() for e in list]


    return list


def convert_poem_binary(max_characters, poem):
    binary = ''
    for s in poem:
        binary += convert_binary(s)

    if len(poem) < max_characters:
        excess = max_characters - len(poem)
        binary += str(0)*27*excess

    if len(binary) == 54000:
        return binary
    else:
        return None

def convert_binary(s):
    if not s == " ":
        ind = ord(s)-97
        placeholder = (str(0)*ind) + str(1) + str(0)*(26-ind)
        return placeholder
    else:
        return '000000000000000000000000001'


def convert_themes(all_themes, poem_themes):
    binary = ''
    for i in range(len(all_themes)):
        if all_themes[i] in poem_themes:
            binary+= '1'
        else:
            binary+= '0'
    return binary
