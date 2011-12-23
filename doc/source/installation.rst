Installation of TADEK
*********************

.. _installation_daemon:

Server
======

To set up the TADEK server, *tadek-common* and *tadek-daemon* packages have to
be installed.

Requirements:

    * Python version 2.5 or newer must be installed

TADEK server requires also one of the accessibility plug-ins:
*tadek-a11y-pyspi*, *tadek-a11y-pyatspi* or *tadek-a11y-pyatspi2* depending on
which accessibility provider is present in the system. More information on
plug-in installation can be found in the :ref:`environment` chapter.

Debian, Ubuntu and Maemo
------------------------

Packages:

    * :pkglink:`deb/tadek-common_|version|.deb`
    * :pkglink:`deb/tadek-daemon_|version|.deb`

Installation command:

:pkgblock:`dpkg -i tadek-common_|version|.deb tadek-daemon_|version|.deb`

MeeGo
-----

Packages:

    * :pkglink:`rpm/tadek-common_|version|.rpm`
    * :pkglink:`rpm/tadek-daemon_|version|.rpm`

Installation command:

:pkgblock:`zypper install tadek-common_|version|.rpm tadek-daemon_|version|.rpm`

CLI Client: tadek-tools
=======================

tadek-tools includes *tadek-explorer*, *tadek* and *tadek-conf* tools.

Requirements:

    * Python version 2.5 or newer must be installed

Debian, Ubuntu and Maemo
------------------------

Packages:

    * :pkglink:`deb/tadek-common_|version|.deb`
    * :pkglink:`deb/tadek-tools_|version|.deb`

Installation command:

:pkgblock:`dpkg -i tadek-common_|version|.deb tadek-tools_|version|.deb`

MeeGo
-----

Packages:

    * :pkglink:`rpm/tadek-common_|version|.rpm`
    * :pkglink:`rpm/tadek-tools_|version|.rpm`

Installation command:

:pkgblock:`zypper install tadek-common_|version|.rpm tadek-tools_|version|.rpm`

GUI Client: tadek-ui
====================

tadek-ui GUI tool can be installed on Linux or Windows.

.. _installation_tadek-ui-requirements:

Requirements:

    * Python version 2.5 or newer must be installed
    * PySide libraries (Python bindings for Qt) version 1.0.1 or newer, newest version can be downloaded from `here <http://developer.qt.nokia.com/wiki/Category:LanguageBindings::PySide::Downloads>`_.

Debian, Ubuntu and Maemo
------------------------

Packages:

    * :pkglink:`deb/tadek-common_|version|.deb`
    * :pkglink:`deb/tadek-ui_|version|.deb`

Installation command:

:pkgblock:`dpkg -i tadek-common_|version|.deb tadek-ui_|version|.deb`

MeeGo
-----

Packages:

    * :pkglink:`rpm/tadek-common_|version|.rpm`
    * :pkglink:`rpm/tadek-ui_|version|.rpm`

Installation command:

:pkgblock:`zypper install tadek-common_|version|.rpm tadek-ui_|version|.rpm`

Installation from Sources
-------------------------

#. Install the :ref:`requirements <installation_tadek-ui-requirements>`
#. Download and unzip sources of `tadek-common <https://github.com/tadek-project/tadek-common/zipball/master>`_ and `tadek-ui <https://github.com/tadek-project/tadek-ui/zipball/master>`_ from github
#. Enter the unzipped directory with tadek-common sources and run command as root/administrator::

    python setup.py --skip-doc install

#. Enter the unzipped directory with tadek-ui sources and run command as root/administrator::

    python setup.py install

#. To run the tadek-ui, execute the *tadek-ui* script:
    * On a Linux system - just issue this command::

        tadek-ui

    * On a Windows system - open console, go to the directory where the python interpreter is installed, e.g. *C:\\Python26* and execute command::

        python.exe Scripts\tadek-ui

API Documentation
=================

Optional package containing HTML documentation of crucial TADEK
modules, classes, functions etc.

Debian, Ubuntu and Maemo
------------------------

Package:

    * :pkglink:`deb/tadek-doc_|version|.deb`

Installation command:

:pkgblock:`dpkg -i tadek-doc_|version|.deb`

MeeGo
-----

Package:

    * :pkglink:`rpm/tadek-doc_|version|.rpm`

Installation command:

:pkgblock:`zypper install tadek-doc_|version|.rpm`

.. _installation_examples:

Tutorial
========

A package containing a copy of this tutorial.

Debian, Ubuntu and Maemo
------------------------

Package:

    * :pkglink:`deb/tadek-tutorial_|version|.deb`

Installation command:

:pkgblock:`dpkg -i tadek-tutorial_|version|.deb`

MeeGo
-----

Package:

    * :pkglink:`rpm/tadek-tutorial_|version|.rpm`

Installation command:

:pkgblock:`zypper install tadek-tutorial_|version|.rpm`


Examples
========

A package containing example models and test cases for three GNOME
applications: gcalctool, gucharmap and tomboy.

Debian, Ubuntu and Maemo
------------------------

Package:

    * :pkglink:`deb/tadek-examples_|version|.deb`

Installation command:

:pkgblock:`dpkg -i tadek-examples_|version|.deb`

MeeGo
-----

Package:

    * :pkglink:`rpm/tadek-examples_|version|.rpm`

Installation command:

:pkgblock:`zypper install tadek-examples_|version|.rpm`

