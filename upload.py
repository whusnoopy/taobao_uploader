# coding: utf8

import json
import os

from taobaopy.taobao import TaoBaoAPIClient, TaoBaoAPIError

from logger import log

def upload(top, config, title=None, desc=None, img_path=None):
    item_kws = dict(config.base_item)

    if title:
        item_kws['title'] = "[测试商品] " + title
    if desc:
        item_kws['desc'] = desc
    if img_path:
        item_kws['image'] = open(img_path, 'rb')

    try:
        r = top.item_add(session=config.token, **item_kws)
        log.debug("upload response:\n%s" % json.dumps(r, indent=2))
    except TaoBaoAPIError, e:
        log.debug("upload failed: %s|%s" % (e.msg, e.sub_msg))
        return 1

    return 0


def upload_list(top, config, up_list):
    for u in up_list:
        upload(top, config, u['title'], u['desc'], u['img_path'])

    return 0


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    from settings import MyConfig

    config = MyConfig()
    top = TaoBaoAPIClient(config.key, config.sec, domain=config.domain)

    sys.exit(upload(top, config))
