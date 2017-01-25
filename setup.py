#! /usr/bin/env python
#
"""
@author: Adam Kniffen
@contact: adamkniffen@gmail.com
@copyright: Copyright 2016
@status: Development
"""


from setuptools import setup, find_packages

setup(
    name='fsf_server',
    version='1',
    packages=find_packages(),
    url='https://github.com/akniffe1/rock_fsf',
    license='Apache 2.0',
    author='Adam Kniffen',
    author_email='adamkniffen@gmail.com',
    description='High Performance Recursive File Scanning',
    install_requires=["yara-python", "czipfile", "pefile", "hachoir-parser", "hachoir-core", "hachoir-regex", "hachoir-metadata",
                      "hachoir-subfile", "ConcurrentLogHandler", "pypdf2", "xmltodict", "rarfile", "ssdeep", "pylzma",
                      "oletools", "pyasn1_modules", "pyasn1", "pyelftools", "javatools", "requests", "pefile"],
    data_files=[('/etc/systemd/system/', ['init.d/fsf.service'])],
    entry_points={
        'console_scripts': [
            'fsfserver=fsf_server.main:main',
	    'fsfclient=fsf_client.fsf_client:main'
        ]
    }
)
