#!/usr/bin/python
# -*- coding: utf-8 -*-

import mdfind

LOCAL_PAPERS_DIR = "/Users/michele.pasin/Desktop/paperstest"


class Searcher():
    def __init__(self, folder=LOCAL_PAPERS_DIR):
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
