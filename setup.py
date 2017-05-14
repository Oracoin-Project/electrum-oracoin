#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")



data_files = []
if platform.system() in [ 'Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-oracoin.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-oracoin.png'])
    ]


setup(
    name="Electrum-Oracoin",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'tlslite',
        'dnspython',
		'ltc_scrypt',
    ],
    package_dir={
        'electrum_oracoin': 'lib',
        'electrum_oracoin_gui': 'gui',
        'electrum_oracoin_plugins': 'plugins',
    },
    packages=['electrum_oracoin','electrum_oracoin_gui','electrum_oracoin_gui.qt','electrum_oracoin_plugins'],
    package_data={
        'electrum_oracoin': [
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_oracoin_gui': [
            "qt/themes/cleanlook/name.cfg",
            "qt/themes/cleanlook/style.css",
            "qt/themes/sahara/name.cfg",
            "qt/themes/sahara/style.css",
            "qt/themes/dark/name.cfg",
            "qt/themes/dark/style.css",
        ]
    },
    scripts=['electrum-oracoin'],
    data_files=data_files,
    description="Electrumweight Oracoin Wallet",
    author="oracoinDEV",
    author_email="oracoincoin@twitter",
    license="GNU GPLv3",
    url="http://www.oracoin.com",
    long_description="""Electrumweight Oracoin Wallet"""
)
