# -*- coding: utf-8 -*-
# Autor:        Paulo Jacob
# Data:         28/11/2021
# Descrição:    Módulo para pegar o html do site

from typing import Optional
import requests
import bs4


def get_search(phrase: str, page: int):
    url = 'https://www.xvideos.com/?k=' + phrase.replace(' ', '+') + f'&p={page}'

    print(url)

    page = requests.get(url, headers={'User-Agent': 'Chrome'})

    print(url)
    return bs4.BeautifulSoup(page.text, 'html.parser')
