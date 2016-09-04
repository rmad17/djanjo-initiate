# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

from setuptools import setup

setup(
    name='django-initiate',
    version='0.1',
    description='Configure .gitignore and local_settings for a django project',
    author='Sourav Basu',
    author_email='souravbasu17@gmail.com',
    url='https://github.com/rmad17/djanjo-initiate',
    py_modules=['initiate'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        initiate=initiate:initiate
    ''',
)
