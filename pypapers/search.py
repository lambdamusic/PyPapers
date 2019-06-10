#!/usr/bin/python
# -*- coding: utf-8 -*-

import mdfind


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
    def __init__(self, documents_list):
        self.docs = documents_list

    def open(self, n=None):
        fpath = "" #@TODO
        subprocess.Popen(['open', fpath])




