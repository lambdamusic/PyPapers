#!/usr/bin/python
# -*- coding: utf-8 -*-

import mdfind
import subprocess
import click

class Searcher():
    def __init__(self, folder):
        self.dir = folder
        # check that folder exists otherwise raise 

    def search_by_name(self, name):
        results = mdfind.name(name, onlyin=self.dir)
        return results

    def search_full_text(self, name):
        args = [name, '-onlyin', self.dir]
        results = mdfind.mdfind(args)
        if results:
            return results.split("\n")
        else:
            return []


class Renderer():
    def __init__(self, documents_list, local_dir=""):
        self.docs = documents_list
        self.local_dir = local_dir

    def open(self, fpath):
        subprocess.Popen(['open', fpath])


    def show_list_and_select(self):
        counter = 1
        click.secho("--------------")
        for el in self.docs:
            name = str(el).replace(self.local_dir, "")
            # click.echo("[%d] " % (counter)  + click.style(name, bold=True))
            click.echo(click.style("[%d] " % (counter), dim=True)  + click.style(name, bold=True))
            counter += 1
        click.secho("--------------")
        click.secho("Please select one option by entering its number, or 'a' to open all (enter=exit): ")
        while True:
            var = input("> ")
            if var == "":
                click.secho("Goodbye")
                break
            elif var == 'a':
                for d in self.docs:
                    self.open(d)
            elif var.isdigit():
                var = int(var)
                if var <= len(self.docs):
                    self.open(self.docs[var-1])
                else:
                    print("Selection not valid")
 