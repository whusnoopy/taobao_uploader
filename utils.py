# coding: utf8

import json

from taobaopy.taobao import TaoBaoAPIClient, TaoBaoAPIError

from logger import log


def get_item(top, config, num_iid):
    try:
        r = top.item_seller_get(num_iid=num_iid, fields=config.DEFAULT_ITEM_FIELDS, session=config.token)
        log.debug(json.dumps(r, indent=2))
    except TaoBaoAPIError, e:
        log.debug(e)

    return 0


def get_seller_cid(top, config):
    try:
        r = top.sellercats_list_get(nick=config.nick, session=config.token)
        log.debug(json.dumps(r, indent=2))

        for cat in r['sellercats_list_get_response']['seller_cats']['seller_cat']:
            print cat['cid'], cat['name']

    except TaoBaoAPIError, e:
        log.debug(e)

    return 0


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    from settings import MyConfig

    config = MyConfig()
    top = TaoBaoAPIClient(config.key, config.sec, domain=config.domain)

    if len(sys.argv) <= 1:
        sys.exit(get_item(top, config, config.num_iid))

    if sys.argv[1] == 'cid':
        sys.exit(get_seller_cid(top, config))
