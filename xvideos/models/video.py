# -*- coding: utf-8 -*-
# Autor:        Paulo Jacob
# Data:         28/11/2021
# Descrição:    Objeto para informações do video

class Video:
    def __init__(self, title: str, url:str, duration: str, thumbnail: str) -> None:
        self.title = title
        self.url = 'https://www.xvideos.com' + url
        self.duration = duration
        self.thumbnail = thumbnail
