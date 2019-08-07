# coding: utf8

import json
import logging

from taobaopy.taobao import TaoBaoAPIError


logger = logging.getLogger(__name__)


def upload_taobao_item(top, config, title=None, desc=None, img_path=None):
    item_kws = dict(config.base_item)

    if title:
        item_kws['title'] = "[测试商品] " + title
    if desc:
        item_kws['desc'] = desc
    if img_path:
        item_kws['image'] = open(img_path, 'rb')

    try:
        r = top.item_add(session=config.token, **item_kws)
        logger.debug("upload response:\n%s", json.dumps(r, indent=2))
    except TaoBaoAPIError, e:
        logger.debug("upload failed: %s|%s", e.msg, e.sub_msg)
        return 1

    return 0


def upload_list_to_taobao(top, config, up_list):
    for u in up_list:
        upload(top, config, u['title'], u['desc'], u['img_path'])

    return 0
