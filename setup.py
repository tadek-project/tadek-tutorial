#!/usr/bin/env python

################################################################################
##                                                                            ##
## This file is a part of TADEK.                                              ##
##                                                                            ##
## TADEK - Test Automation in a Distributed Environment                       ##
## (http://tadek.comarch.com)                                                 ##
##                                                                            ##
## Copyright (C) 2011,2012 Comarch S.A.                                       ##
## All rights reserved.                                                       ##
##                                                                            ##
## TADEK is free software for non-commercial purposes. For commercial ones    ##
## we offer a commercial license. Please check http://tadek.comarch.com for   ##
## details or write to tadek-licenses@comarch.com                             ##
##                                                                            ##
## You can redistribute it and/or modify it under the terms of the            ##
## GNU General Public License as published by the Free Software Foundation,   ##
## either version 3 of the License, or (at your option) any later version.    ##
##                                                                            ##
## TADEK is distributed in the hope that it will be useful,                   ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of             ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              ##
## GNU General Public License for more details.                               ##
##                                                                            ##
## You should have received a copy of the GNU General Public License          ##
## along with TADEK bundled with this file in the file LICENSE.               ##
## If not, see http://www.gnu.org/licenses/.                                  ##
##                                                                            ##
## Please notice that Contributor Agreement applies to any contribution       ##
## you make to TADEK. The Agreement must be completed, signed and sent        ##
## to Comarch before any contribution is made. You should have received       ##
## a copy of Contribution Agreement along with TADEK bundled with this file   ##
## in the file CONTRIBUTION_AGREEMENT.pdf or see http://tadek.comarch.com     ##
## or write to tadek-licenses@comarch.com                                     ##
##                                                                            ##
################################################################################

import os
import sys
from glob import glob
from subprocess import check_call
from distutils import log
from distutils.core import setup
from distutils.dir_util import remove_tree
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
from distutils.command.install import install as _install
try:
    from tadek.core.config import DATA_DIR, DOC_DIR, VERSION
except ImportError:
    print >> sys.stderr, "Required tadek-common package is not installed"
    exit(1)

DATA_FILES = []

BUILD_HTML_DIR = os.path.join("build", "html")
BUILD_DOC_TREES_DIR = os.path.join("build", "doctrees")

API_DOC_DIR = os.path.join(DOC_DIR, "api", "html")
HTML_DOC_DIR = os.path.join(DOC_DIR, "tutorial", "html")

def getExamplesPaths(files, dirname, names):
    files.append((os.path.join(DATA_DIR, dirname),
                  [os.path.join(dirname, name) for name in names
                   if os.path.isfile(os.path.join(dirname, name))
                   and (name.endswith(".py") or name.endswith(".mo"))]))

os.path.walk("examples", getExamplesPaths, DATA_FILES)

class build(_build):
    def run(self):
        _build.run(self)
        if not os.path.exists(BUILD_HTML_DIR):
            os.makedirs(BUILD_HTML_DIR)
            SPHINX = ["sphinx-build", "-b", "html",
                "-d", os.path.join("build", "doctrees"),
                "-D", "epylink_output_dir=" + API_DOC_DIR,
                "-D", "epylink_api_dir=" + os.path.join(
                                os.pardir, os.pardir, "api", "html"),
                os.path.join("doc", "source"),
                BUILD_HTML_DIR]
            check_call(SPHINX)
        DATA_FILES.extend([
            (HTML_DOC_DIR, glob(os.path.join("build", "html", "[!_]*"))),
            (os.path.join(HTML_DOC_DIR, "_images"),
                glob(os.path.join("build", "html", "_images", '*'))),
            (os.path.join(HTML_DOC_DIR, "_sources"),
                glob(os.path.join("build", "html", "_sources", '*'))),
            (os.path.join(HTML_DOC_DIR, "_static"),
                glob(os.path.join("build", "html", "_static", '*'))),
            ])

class install(_install):
    sub_commands = []
    # Skip the install_egg_info sub-command
    for name, method in _install.sub_commands:
        if name != "install_egg_info":
            sub_commands.append((name, method))
    del name, method

class clean(_clean):
    def run(self):
        if self.all:
            if os.path.exists(BUILD_HTML_DIR):
                remove_tree(BUILD_HTML_DIR, dry_run=self.dry_run)
            else:
                log.warn("'%s' does not exist -- can't clean it",
                    BUILD_HTML_DIR)
            if os.path.exists(BUILD_DOC_TREES_DIR):
                remove_tree(BUILD_DOC_TREES_DIR, dry_run=self.dry_run)
            else:
                log.warn("'%s' does not exist -- can't clean it",
                    BUILD_DOC_TREES_DIR)
        _clean.run(self)

setup(
    name="tadek-tutorial",
    version=VERSION,
    description="TADEK tutorial source files and examples",
    long_description=''.join(['\n', open("README").read()]),
    author="Comarch TADEK Team",
    author_email="tadek@comarch.com",
    license="http://tadek.comarch.com/licensing",
    url="http://tadek.comarch.com/",
    cmdclass={"build": build, "install": install, "clean": clean},
    data_files=DATA_FILES,
)

