# coding: utf8

import click

from settings import config, top


@click.group()
def cli():
    pass


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


cli.add_command(run)

if __name__ == "__main__":
    cli()
