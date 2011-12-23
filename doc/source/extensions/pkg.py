################################################################################
##                                                                            ##
## This file is a part of TADEK.                                              ##
##                                                                            ##
## TADEK - Test Automation in a Distributed Environment                       ##
## (http://tadek.comarch.com)                                                 ##
##                                                                            ##
## Copyright (C) 2011 Comarch S.A.                                            ##
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
import re
from docutils import nodes


def _sections(text, replacement):
    sections = []
    lastIndex = 0
    for m in re.finditer("\|version\|", text):
        start, stop = m.span()
        sections.append((False, text[lastIndex:start]))
        lastIndex = stop
        sections.append((True, replacement))
    if lastIndex != len(text):
        sections.append((False, text[lastIndex:]))
    return sections

def pkglink_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    pkgDir = inliner.document.settings.env.app.config.pkglink_dir
    version = inliner.document.settings.env.app.config.version

    sections = _sections(os.path.split(text)[1], version)
    text = re.sub("\|version\|", version, text)
    if not pkgDir:
        inliner.reporter.error("Configuration value 'pkglink_dir' "
                               "is not set in conf.py")
        node = nodes. literal(rawtext, text)
    else:
        node = nodes.reference(rawtext, refuri="%s/%s"%(pkgDir, text),
                               **options)
        for emp, section in sections:
            if emp:
                node += nodes.emphasis(section, section)
            else:
                node += nodes.inline(section, section)

    return [node], []

def pkgblock_role(role, rawtext, text, lineno, inliner, options={},
                      content=[]):
    version = inliner.document.settings.env.app.config.version
    sections = _sections(text, version)
    node = nodes.literal_block(rawtext)
    for emp, section in sections:
        if emp:
            node += nodes.emphasis(section, section)
        else:
            node += nodes.inline(section, section)
    
    return [node], []

def setup(app):
    app.add_role("pkglink", pkglink_role)
    app.add_config_value("pkglink_dir", "", "env")
    app.add_role("pkgblock", pkgblock_role)
