#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import click

from .search import *



CMD_LINE_EXAMPLES = """SOME EXAMPLES HERE:
$ pypapers
 => returns some nice text
"""




@click.command()
@click.argument('args', nargs=-1)
# @click.option('--examples', is_flag=True, help='Show some examples')
@click.option('-f', '--fulltext', is_flag=True, help='Search in full text')
@click.pass_context
def main_cli(ctx, args=None, examples=False, fulltext=False):
    """PyPapers is a simple utility for searching a folder of documents. All arguments are joined together so to form an AND query. By default matches file names only, use -f to search in full text."""

    # if examples:
    #     click.secho(CMD_LINE_EXAMPLES, fg="green")
    #     return

    if not args:
        click.echo(ctx.get_help())
        return

    query = " ".join(args)
    if False:
        for arg in args:
            print('passed argument :: {}'.format(arg))

    s = Searcher()
    if fulltext:
        data = s.search_full_text(query)
    else:
        data = s.search_by_name(query)
    
    if data:
        for x in data:
            print(x)
    else:
        click.secho("No results.")


if __name__ == '__main__':
    main_cli()
