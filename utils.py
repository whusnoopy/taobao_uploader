# coding: utf8

import json
import logging

from taobaopy.taobao import TaoBaoAPIError


logger = logging.getLogger(__name__)


def get_taobao_item(top, config, num_iid):
    try:
        r = top.item_seller_get(num_iid=num_iid, fields=config.DEFAULT_ITEM_FIELDS, session=config.token)
        logger.debug(json.dumps(r, indent=2))
    except TaoBaoAPIError, e:
        logger.debug(e)

    return 0


def get_seller_cid(top, config):
    try:
        r = top.sellercats_list_get(nick=config.nick, session=config.token)
        logger.debug(json.dumps(r, indent=2))

        for cat in r['sellercats_list_get_response']['seller_cats']['seller_cat']:
            print cat['cid'], cat['name']

    except TaoBaoAPIError, e:
        logger.debug(e)

    return 0
