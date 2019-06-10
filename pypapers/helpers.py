#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import click
import configparser


USER_CONFIG_DIR = os.path.expanduser("~/.pypapers/")
USER_CONFIG_FILE_NAME = "pypapers.ini"
USER_CONFIG_FILE_PATH = os.path.expanduser(USER_CONFIG_DIR + USER_CONFIG_FILE_NAME)


def init_config_folder(user_config_dir, user_config_file, papers_dir=None):
    """
    Create the config folder/file unless existing. If it exists, backup and create new one.
    """
    # papers_dir = args list
    if not papers_dir or not os.path.exists(papers_dir[0]):
        print("Please provide a valid directory path e.g. --init ~/Documents/papers")
        return False
    
    papers_dir = papers_dir[0]  

    if not os.path.exists(user_config_dir):
        os.mkdir(user_config_dir)
        # click.secho("Created %s" % user_config_dir, dim=True)
    if os.path.exists(user_config_file):
        click.secho("The config file `%s` already exists." % user_config_file, fg="red")
        if click.confirm("Overwrite?"):
            pass
        else:
            click.secho("Goodbye")
            return False

    f= open(user_config_file,"w+")
    f.write("[sourcedata]\n")
    f.write("location=" + papers_dir + "\n")
    f.close()
    click.secho(
        "Created %s" % user_config_file, dim=True
    )



def read_config_folder():
    config = configparser.ConfigParser()
    settings_info = os.path.expanduser(USER_CONFIG_FILE_PATH)
    try:
        config.read(settings_info)
    except:
        click.secho("ERROR: Config file not found at: %s" % settings_info, fg="red")
        raise
    try:
        section = config['sourcedata']
    except:
        click.secho("ERROR: Config file is not formatted correctly" , fg="red")
        raise
    return section  # access via section['location'] ..etc..


