#!/usr/bin/env python
from setuptools import setup, find_packages

install_reqs = [
    'requests',
]

setup(
    name='newsapi',
    version='0.0.0',
    description='Python client for the News-API REST API',
    author='James Christopher',
    author_email='jcahall@washington.edu',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    url='https://github.com/News-API-gh/News-API-python',
    install_requires=install_reqs,
)