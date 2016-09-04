# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

from setuptools import setup

setup(
    name='initiate',
    version='0.1',
    py_modules=['initiate'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        initiate=initiate:initiate
    ''',
)
