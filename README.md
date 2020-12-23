# PyPapers

PyPapers is a simple commmand line tool for searching a folder of PDF documents. 

You can pass search terms and all arguments are joined together so to form an `AND` query. By default it matches file names only, but you can use -f to search in full text.

![pypapers_animation](https://raw.githubusercontent.com/lambdamusic/pypapers/master/img/pypapers.gif)


## Why?

I've tried many of them and finally got fed up with [reference managements systems](https://en.wikipedia.org/wiki/Comparison_of_reference_management_software). Either too bloated with features, or lacking simplicity.

Let's try to do this the simple way: 

* All PDFs in one folder (or so) 
* A command line tool to search them 
* Rely on OSx excellent `mdfind` library for searching 
* Rely on excellent Preview app for reading/editing 

See also this [blog post](http://www.michelepasin.org/blog/2019/06/30/pypapers-a-bare-bones-command-line-pdf-manager/)


## Install

```
pip install pypapers
```

## Usage

```
pypapers --help
```


## Status

> alpha


## Comments, bug reports

PyPapers lives on [Github](https://github.com/lambdamusic/pypapers). You can file [issues]([issues](https://github.com/lambdamusic/pypapers/issues/new)) or pull requests there. Suggestions, pull requests and improvements welcome!
