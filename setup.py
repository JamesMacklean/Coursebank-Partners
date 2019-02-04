# -*- coding: utf-8 -*-
#
# Imports ###########################################################

import os
from setuptools import setup

# Main ##############################################################

setup(
    name='partners_pages',
    version='1.0',
    description='LMS - Coursebank Partners Pages',
    packages=['partners'],
    install_requires=[
        'Django',
    ],
)
