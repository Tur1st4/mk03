# -*- coding: utf-8 -*-
# Autor:        Paulo Jacob
# Data:         28/11/2021
# Descrição:    Web Scraping do site vermelho e preto

from cogs.find_tags import find_pagination, find_search_videos
from cogs.request import get_search


if __name__ == '__main__':
    soup = get_search('creampie glory hole')
    videos = find_search_videos(soup)
    last_page = find_pagination(soup)

    for video in videos:
        print(f'Titulo: {video.title}\nDuração: {video.duration}\nURL: {video.url}\nThumbnail: {video.thumbnail}')

    print(f'Total de páginas: {last_page}')
