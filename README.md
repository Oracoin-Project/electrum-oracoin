Electrum-Oracoin - electrumweight oracoin client
=====================================

  Licence: GNU GPL v3
  Author: Thomas Voegtlin
  maintainer: oracoin
  Language: Python
  Homepage: https://www.oracoin.com/

  
1. GETTING STARTED
------------------

To run Electrum-Oracoin from this directory, just do::

    ./electrum-oracoin

If you install Electrum-Oracoin on your system, you can run it from any
directory.

If you have pip, you can do::

    python setup.py sdist
    sudo pip install --pre dist/Electrum-Oracoin-2.3.0.tar.gz


If you don't have pip, install with::

    python setup.py sdist
    sudo python setup.py install




2. HOW OFFICIAL PACKAGES ARE CREATED
------------------------------------

On Linux/Windows::

    pyrcc4 icons.qrc -o gui/qt/icons_rc.py
    python setup.py sdist --format=zip,gztar

On Mac OS X::

    # On port based installs
    sudo python setup-release.py py2app

    # On brew installs
    ARCHFLAGS="-arch i386 -arch x86_64" sudo python setup-release.py py2app --includes sip

    sudo hdiutil create -fs HFS+ -volname "Electrum-Oracoin" -srcfolder dist/Electrum-Oracoin.app dist/electrum-oracoin-VERSION-macosx.dmg
