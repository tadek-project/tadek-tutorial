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

from tadek.engine.testdefs import *
from tadek.engine.searchers import *
from tadek.models.gucharmap import *
from tadek.core.constants import *
from tadek.teststeps.gucharmap.basic import *

caseEnterLetters = TestCase(
    stepRunCharacterMap(),
    stepLatin(),
    stepEnterCharacters(chars="Azfla"),
    description="Activate a sequence of letters and compare to the text field")

def closeCharacterMap(self, test, device):
    if app.getImmediate(device):
        app.menu.File.Close.click(device)

class ActivateCharactersWithKeyboardTestsSuite(TestSuite):
    description = "Activate characters using keyboard"

    caseActivateCharactersWithSpace = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepActivateLettersWithKeyboard(letters="EbFFGF"),
        description="Activate a sequence of letters using Space and compare to the text field")

    caseActivateCharactersWithEnter = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepActivateLettersWithKeyboard(letters="EbFFGF", activatingKey=KEY_SYMS["ENTER"]),
        description="Activate a sequence of letters using Enter and compare to the text field")
