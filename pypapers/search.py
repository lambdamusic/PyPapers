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

    def select_item(self):
        x = self.show_list()
        if x == "all":
            for d in self.docs:
                self.open(d)
        elif isinstance(x, int):
            self.open(self.docs[x-1]) 
        return

    def show_list(self):
        counter = 1
        click.secho("--------------")
        for el in self.docs:
            name = str(el).replace(self.local_dir, "")
            # click.echo("[%d] " % (counter)  + click.style(name, bold=True))
            click.echo(click.style("[%d] " % (counter), dim=True)  + click.style(name, bold=True))
            counter += 1
        click.secho("--------------")
        click.secho("Please select one option by entering its number, or 'a' to open all (enter=exit): ")
        var = input()
        if var == "":
            return None
        elif var == 'a':
            return "all"
        elif var.isdigit():
            var = int(var)
            if var <= len(self.docs):
                return var
            else:
                print("Selection not valid")
                return None                

        # elif var.isdigit():
        #     try:
        #         var = int(var)
        #         return self.docs[var-1]
        #     except:
        #         print("Selection not valid")
        #         return None
        else:
            return None
