#!/usr/bin/env python
from setuptools import setup

requires = ['httplib2']

entry_points = {
    'console_scripts': [
        'saythanks = saythanks:main'
    ]
}


README = open('README.rst').read()
CHANGELOG = open('changelog.rst').read()


setup(
    name="saythanks",
    version="0.1",
    url='',
    author='Lin Yiyu',
    author_email='linyiyu1992@gmail.com',
    description="Saythanks is a tools for NHD users",
    long_description=README + '\n' + CHANGELOG,
    packages=['saythanks'],
    include_package_data=True,
    install_requires=requires,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
         'Environment :: Console',
         'License :: OSI Approved :: GNU Affero General Public License v3',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.3',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='',
)
