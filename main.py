# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response
from xvideos.cogs.find_tags import find_search_videos

from xvideos.cogs.request import get_search

app = Flask(__name__)

@app.route('/')
def test_api():
    soup = get_search('creampie glory hole')
    videos = find_search_videos(soup)

    return make_response(jsonify(videos), 200)

if __name__ == '__main__':
    app.run(debug=True)