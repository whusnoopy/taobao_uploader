# coding: utf8

import click

from settings import config, top


@click.group()
def cli():
    pass


@click.command()
@click.option('--num_iid', type=int, default=config.num_iid, help="taobao item num_iid to fetch")
def get_item(num_iid):
    """fetch item from taobao to show its props"""
    from utils import get_taobao_item

    return get_taobao_item(top, config, num_iid)


@click.command()
def get_cid():
    """fetch taobao seller cid"""
    from utils import get_seller_cid

    return get_seller_cid(top, config)


@click.command()
def upload_item():
    """upload an item to taobao with default config"""
    from upload import upload

    return upload(top, config)


@click.command()
@click.option('-u', '--upload', default=False, is_flag=True,
              help="upload to taobao or just test crawl")
def run(upload):
    """crawl books from douban and upload to taobao as items"""
    from crawl_douban import crawl_douban
    from upload import upload_list

    book_list = crawl_douban(config.fetch_url)
    if upload:
        upload_list(top, config, book_list)

    return len(book_list)


cli.add_command(get_item)
cli.add_command(get_cid)
cli.add_command(upload_item)
cli.add_command(run)

if __name__ == "__main__":
    cli()
