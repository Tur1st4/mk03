# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response, request
from xvideos.cogs.find_tags import find_pagination, find_search_videos
from xvideos.cogs.request import get_search

app = Flask(__name__)

@app.route('/xvideos')
def test_api():
    page = request.args.get('page', default = 1, type = int)
    phrase = request.args.get('phrase', default = '', type = str)

    print(phrase)
    soup = get_search(phrase, page)
    videos = find_search_videos(soup)
    total_pages = find_pagination(soup)
    data = {
        "videos": videos,
        "pages": total_pages
    }

    return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run(debug=True)