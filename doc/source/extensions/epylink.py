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


def epylink_role(role, rawtext, text, lineno, inliner, options={}, content=[]):

    epyDir = inliner.document.settings.env.app.config.epylink_api_dir
    if not epyDir:
        inliner.reporter.error("Configuration value 'epylink_api_dir' "
                               "is not set in conf.py")
    outDir = inliner.document.settings.env.app.config.epylink_output_dir
    if not outDir:
        inliner.reporter.error("Configuration value 'epylink_output_dir' "
                               "is not set in conf.py")
    sections = text.rsplit(".", 1)
    if text[0] == "~":
        text = text[1:]
        sections[0] = sections[0][1:]
        name = sections[1] if len(sections) == 2 else text
    else:
        name = text
    found = False
    url = "%s/%s-module.html" % (epyDir, text)
    if os.path.isfile(os.path.join(outDir, url)):
        found = True
    else:
        url = "%s/%s-class.html" % (epyDir, text)
        if os.path.isfile(os.path.join(outDir, url)):
            found = True
        else:
            if len(sections) == 2:
                for tag in ("class", "module"):                 
                    url = "%s/%s-%s.html" % (epyDir, sections[0], tag)
                    fullUrl = os.path.join(outDir, url)
                    if os.path.isfile(fullUrl):
                        f = None
                        try:
                            f = open(fullUrl)
                            html = f.read()
                            if "<a name=\"%s\">" % sections[1] in html:
                                url = "%s#%s" % (url, sections[1])
                                found = True
                                if re.search(
                                    "<a href=\"%s\".*summary-sig-name.*</a>(\("
                                    ".*summary-sig-arg|\(\))"
                                    % os.path.split(url)[1], html):
                                    name += "()"
                                break
                        finally:
                            if f:
                                f.close()
    if found:
        node = nodes.reference(rawtext, "", refuri=url, **options)
        node += nodes.literal(rawtext, name, classes=['xref'])
    else:
        inliner.reporter.warning("Target document not found for '%s'" % text,
                                 line=lineno)
        node = nodes.literal(rawtext, name)
    return [node], []

def setup(app):
    app.add_role("epylink", epylink_role)
    app.add_config_value("epylink_output_dir", "", "env")
    app.add_config_value("epylink_api_dir", "", "env")

