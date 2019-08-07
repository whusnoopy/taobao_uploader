# coding: utf8

import os

import requests
from pyquery import PyQuery

from logger import log


def crawl_douban(url, img_dir="img"):
    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)

    book_list = list()

    req = requests.get(url)
    pq = PyQuery(req.text)

    log.debug("fetch %s success", url)

    items = pq(".article dl")
    for item in items.items():
        img_url = item("img").attr("src")
        title = item(".title").text()
        desc = item(".desc").text()

        img_path = os.path.join(img_dir, img_url.split('/')[-1])
        r = requests.get(img_url, stream=True)
        if r.status_code == 200:
            with open(img_path, 'wb') as fp:
                fp.write(r.content)

        book_list.append(dict(title=title, desc=desc, img_path=img_path))

        log.debug("crawled\n  %s\n    %s\n    %s", title, desc, img_path)

    return book_list
