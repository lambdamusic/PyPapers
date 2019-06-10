#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import click

from .search import *
from .VERSION import *
from .helpers import *



@click.command()
@click.argument('args', nargs=-1)
# @click.option('--examples', is_flag=True, help='Show some examples')
@click.option('-f', '--fulltext', is_flag=True, help='Search in full text')
@click.option(
    "-i",
    "--init",
    is_flag=True,
    help="Initialize the configuration file with your Documents path info.")
@click.pass_context
def main_cli(ctx, args=None, init=False, fulltext=False):
    """PyPapers is a simple utility for searching a folder of documents. All arguments are joined together so to form an AND query. By default matches file names only, use -f to search in full text."""

    if not init and not os.path.exists(USER_CONFIG_FILE_PATH):
        click.secho(
            "ERROR: Please set a documents folder first - you can do that by typing: `pypapers --init <documents-path>`",
            bold=True,
        )
        return

    if init:
        init_config_folder(USER_CONFIG_DIR, USER_CONFIG_FILE_PATH, args)
        return 

    if not args:
        click.secho("PyPapers (" + VERSION + ")", dim=True)
        click.echo(ctx.get_help())
        return

    query = " ".join(args)

    LOCAL_PAPERS_DIR = read_config_folder()['location']
    s = Searcher(LOCAL_PAPERS_DIR)

    if fulltext:
        data = s.search_full_text(query)
    else:
        data = s.search_by_name(query)
    
    if data:
        r = Renderer(data, LOCAL_PAPERS_DIR)
        r.show_list_and_select()

        # for x in data:
        #     print(x)
    else:
        click.secho("No results.")


if __name__ == '__main__':
    main_cli()



