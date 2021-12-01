# -*- coding: utf-8 -*-
# Autor:        Paulo Jacob
# Data:         28/11/2021
# Descrição:    Módulo para pegar o html do site

import requests
import bs4


def get_search(phrase: str):
    url = 'https://www.xvideos.com/?k=' + phrase.replace(' ', '+')
    page = requests.get(url)

    print(url)
    return bs4.BeautifulSoup(page.text, 'html.parser')
