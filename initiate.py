# !/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
This file automates some stuff which is required right after creating a django\
project like creating a .gitignore, local_settings.py, \
local_settings_sample.py with required data
"""
import os
import click


@click.command()
@click.argument('projectname')
@click.option('--dbengine', default='django.db.backends.sqlite3',
              help='name of your database engine')
@click.option('--dbname', default='mydatabase', help='name of your database')
@click.option('--user', default='', help='username of your database')
@click.option('--password', default='', help='password to your database')
@click.option('--host', default='127.0.0.1', help='hostname of your database')
@click.option('--port', default='', help='port of your database')
@click.option('--testdb', default='mydatabasetest',
              help='Name of your test database')
@click.option('--debug', default=True, help='DEBUG value')
def initiate(projectname, dbengine, dbname, user, password, host, port,
             testdb, debug):
    if os.path.exists(projectname + "/settings.py"):
        create_gitignore()
        # local_settings_sample.py
        create_local_settings(projectname)
        # local_settings.py
        create_local_settings(projectname, 'local_settings.py', dbengine,
                              dbname, user, password, host, testdb, port,
                              debug, get_secret_key(projectname))
        update_settings(projectname)


def create_gitignore():
    gitignore_content = \
        "# Django #" + "\n" + \
        "*.log" + "\n" + \
        "*.pot" + "\n" + \
        "*.pyc" + "\n" + \
        "__pycache__/" + "\n" + \
        "local_settings.py" + "\n" + \
        "db.sqlite3" + "\n" + \
        "media" + "\n" + \
        "# Ignore all local_settings #" + "\n" + \
        "*_settings.py" + "\n" + \
        "# Linux #" + "\n" + \
        "*.swp"
    print("Creating .gitignore ...")
    with open(".gitignore", "w+") as gitignore:
        gitignore.write(gitignore_content)


def get_secret_key(base_dir):
    SECRET_KEY = ""
    with open(base_dir + "/settings.py", "r") as settings:
        print("Searching for SECRET_KEY in settings.py ...")
        for line in settings:
            if "SECRET_KEY" in line:
                SECRET_KEY = line
                print("Yay!!! Found SECRET KEY!")
                return SECRET_KEY
    return ''


def create_local_settings(base_dir, file_name='local_settings_sample.py',
                          db_engine='', db_name='', db_user='', db_password='',
                          db_host='', db_test='', db_port='', DEBUG=True,
                          SECRET_KEY=''):
    with open(base_dir + "/" + file_name, "w+") as \
                                        local_settings:
        print("Generating " + file_name + " ...")
        local_settings_content = \
            "DEBUG = " + str(DEBUG) + "\n\n" + \
            "DATABASES = {" + "\n" + \
            "   'default': {" + "\n" + \
            "       'ENGINE': '" + db_engine + "'," + "\n" + \
            "       'NAME': '" + db_name + "'," + "\n" + \
            "       'USER': '" + db_user + "'," + "\n" + \
            "       'PASSWORD': '" + db_password + "'," + "\n" + \
            "       'HOST': '" + db_host + "'," + "\n" + \
            "       'PORT': '" + db_port + "'," + "\n" + \
            "       'TEST': {" + "\n" + \
            "           'NAME': '" + db_test + "'," + "\n" + \
            "       }," + "\n" + \
            "   }" + "\n" + \
            "}"
        if not SECRET_KEY:
            local_settings_content = "SECRET_KEY = ''" + "\n\n" + \
                local_settings_content
        else:
            local_settings_content = SECRET_KEY + "\n\n" + \
                local_settings_content
        local_settings.write(local_settings_content)


def update_settings(base_dir):
    print("Updating settings ...")
    with open(base_dir + "/settings.py", "a") as settings:
        append_content = "\n" + \
            "try:" + "\n" + \
            "    from local_settings import SECRET_KEY, DATABASES, DEBUG  # noqa" + "\n" + \
            "except ImportError as e:" + "\n" + \
            "    print('Error:', e.msg)"
        settings.write(append_content)


if __name__ == "__main__":
    generate()
