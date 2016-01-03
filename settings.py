# coding: utf8

class Config(object):
    key = 'TODO/YOUR_APP_KEY'
    sec = 'TODO/YOUR_APP_SEC'
    domain = 'TODO/YOUR_PROXY_DOMAIN'

    DEFAULT_ITEM_FIELDS = 'num_iid,title,pic_url,price,nick,outer_id,cid,postage_id,seller_cids'

    nick = 'TODO/YOUR_NICK'
    token = 'TODO/YOUR_W2_AUTH_CODE'
    num_iid = 0L # TODO: replace with one of your item num_iid

    base_item = dict({
        'num': 100,
        'price': 100000.00,
        'type': 'fixed',
        'stuff_status': 'new',
        'title': '测试宝贝',
        'desc': '<span style="color:red">红色</span> 测试',
        'location.state': '浙江',
        'location.city': '杭州',
        # 'cid': 50014945, # 个性定值/设计服务/DIY > 其他定制 > 其他商品定制 (max 50)
        'cid': 251103, # 模玩/动漫/周边/cos/桌游 > 棋牌/桌游 > 其他棋牌/桌面游戏
        'image': open('img/taobao.png', 'rb')
    })


class MyConfig(Config):
    nick = ''
    token = ''
    num_iid = 0L

    def __init__(self):
        # TODO: fill for edit
        self.base_item['seller_cids'] = '0,'
        self.base_item['postage_id'] = 0
