#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = ['pytest-runner',]

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='add crontab task in crontab',
    long_description='add crontab task in crontab',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'crontab', 'mysql'
    ],
    name='pytest-crontab',
    packages=find_packages(include=['pytest_crontab']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-crontab',
    version='0.1',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner',
        'pymysql'
    ],
    entry_points={
        'pytest11': [
            'pytest-crontab = pytest_crontab.plugin',
        ]
    }
)
