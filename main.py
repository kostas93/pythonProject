# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
s = BeautifulSoup(url_txt, 'lxml')
my_table = s.find('table', class_='wikitable sortable plainrowheaders')
table_links = my_table.find_all('a',href=True)
actors = []
for links in table_links:
      actors.append(links.get('title'))
print(actors)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
