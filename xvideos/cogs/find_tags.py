# -*- coding: utf-8 -*-
# Autor:        Paulo Jacob
# Data:         28/11/2021
# Descrição:    Módulo para encontrar todas as tags necessárias e converter em objetos

from bs4 import BeautifulSoup


def find_search_videos(soup: BeautifulSoup):
    matchs = soup.find_all('div', class_='thumb-block')
    videos = []

    for video in matchs:
        info = video.find('div', class_='thumb-under').find('a')
        title = info['title']
        url = 'https://www.xvideos.com' + info['href']
        duration = info.find('span').text
        thumbnail = video.find('div', class_='thumb-inside').find('img')['data-src']

        videos.append({"title": title, "url": url, "duration": duration, "thumbnail": thumbnail})

    return videos

def find_pagination(soup: BeautifulSoup):
    last_page = soup.find('a', class_='last-page').text

    return int(last_page)