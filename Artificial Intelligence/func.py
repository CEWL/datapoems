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

    soup = BeautifulSoup(response, 'lxml')
    text = soup.find_all('Well, read')
    print(text)

get_poem(config.max_characters, 'https://www.poetryfoundation.org/poems/149945/cold-valley')
