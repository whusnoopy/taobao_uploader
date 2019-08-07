# taobao_uploader

This is an items uploader for Taobao seller, which crawl books or movies from Douban.

# Usage

## 0. Prepare your environment

    virtualenv env
    source env/bin/active
    pip install -r requirements.txt

## 1. Fill the api info in `settings.py`

    # settings.py
    key = 'TODO/YOUR_APP_KEY'
    sec = 'TODO/YOUR_APP_SEC'
    domain = 'TODO/YOUR_PROXY_DOMAIN'

    # ...

    nick = 'TODO/YOUR_NICK'
    token = 'TODO/YOUR_W2_AUTH_CODE'
    num_iid = 0L # TODO: replace with one of your valid taobao item num_iid

## 2. Get one of your item, to fill other info in `settings.py`

    python ./run.py get-item

    ...
    {
      postage_id: TODO,
      seller_cat: TODO,
      ...
    }

## 3. Use any list link you favor to crawl and upload

    # run.py
    url = "http://www.douban.com/tag/2014/movie?start=15"

    python ./run.py upload-list
