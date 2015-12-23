# coding: utf8


def main():
    from taobaopy.taobao import TaoBaoAPIClient
    from settings import MyConfig
    from crawl_douban import crawl_douban
    from upload import upload_list

    config = MyConfig()
    top = TaoBaoAPIClient(config.key, config.sec, domain=config.domain)

    url = "http://www.douban.com/tag/2014/movie?start=15"

    book_list = crawl_douban(url)

    upload_list(top, config, book_list)

    return 0


if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')

    sys.exit(main())
