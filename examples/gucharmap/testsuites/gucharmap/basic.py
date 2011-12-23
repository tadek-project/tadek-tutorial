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
from tadek.testcases.gucharmap.basic import *

class BasicTestsSuite(TestSuite):
    description = "Test basic functionalities of the Character Map application"

    tearDownCase = closeCharacterMap

    caseRunClose = TestCase(
        stepRunCharacterMap(),
        stepCloseCharacterMap(),
        description="Run and then close the Character Map application")

    caseEnterLetters1 = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepEnterCharacters(chars="A"),
        description="Activate a sequence of letters and compare to the text field")

    caseEnterLetters2 = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepEnterCharacters(chars="AFZN"),
        description="Activate a sequence of letters and compare to the text field")

    caseEnterLetters3 = caseEnterLetters()

    caseEnterDigits = TestCase(
        stepRunCharacterMap(),
        stepCommon(),
        stepEnterCharacters(chars="0143256789"),
        description="Activate a sequence of letters and compare to the text field")

    caseEnterLettersDigits = TestCase(
        stepRunCharacterMap(),
        stepCommon(),
        stepEnterCharacters(chars="4092"),
        stepLatin(),
        stepEnterCharacters(chars="abP"),
        stepCommon(),
        stepEnterCharacters(chars="867"),
        stepLatin(),
        stepEnterCharacters(chars="AMi"),
        description="Activate a sequence of letters and compare to the text field")

    activateCharacters = ActivateCharactersWithKeyboardTestsSuite()

class CopyPasteTestsSuite(TestSuite):
    description = "Test copy-paste functionalities of the Character Map application"

    tearDownCase = closeCharacterMap

    caseCopyPaste = TestCase(
        caseEnterLetters(),
        stepCopy(),
        stepPaste(),
        description="Copy the text to the clippboard and then append it to the text field")

    caseCopyPasteKeyboard = TestCase(
        stepRunCharacterMap(),
        stepEnterKeyboardCharacters(chars="Kp5;="),
        stepCopy(),
        stepPaste(),
        description="Copy the text to the clippboard and then append it to the text field")

    caseCopyPasteTypeKeys = TestCase(
        stepRunCharacterMap(),
        stepTypeCharacters(chars="Kp5;="),
        stepCopy(),
        stepPaste(),
        description="Copy the text to the clippboard and then append it to the text field")

    casePopUpCopyPaste = TestCase(
        stepRunCharacterMap(),
        stepTypeCharacters(chars="Kp5;="),
        stepPopUpCopy(),
        stepPaste(),
        description="Copy the text to the clippboard and then append it to the text field")

class ExtraTestsSuite(TestSuite):
    description = "Test additional functionalities of the Character Map application"

    tearDownCase = closeCharacterMap

    casePopUpCharacter = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepPopUpCharacter(),
        description="Show popup character and test it")

    caseAboutDialog = TestCase(
        stepRunCharacterMap(),
        stepAboutDialog(),
        description="Test openning and closing 'About' dialog")

    caseCharactersWithModifiers = TestCase(
        stepRunCharacterMap(),
        stepEnterKeyboardCharactersWithModifiers(chars=[('a', 'LEFT_SHIFT'),
            'b', ('p', 'RIGHT_SHIFT'), ('c', 'LEFT_ALT')],
            textToCompare="AbP"),
        stepEnterKeyboardCharactersWithModifiers(chars=[('v', 'LEFT_CONTROL'),
            ' ', 'a', 'b', ('LEFT', 'RIGHT_CONTROL', 'RIGHT_SHIFT'),
            ('c', 'LEFT_CONTROL'), 'END', ('v', 'LEFT_CONTROL'),
            (';', 'RIGHT_SHIFT'), 'a'],
            textToCompare="AbPAbP abab:a"),
        description="")

    caseChangeFontSize1 = TestCase(
        stepRunCharacterMap(),
        stepSetFontSize(size=20.0),
        stepChangeFontSize(up=5, down=1),
        stepCheckFontSize(),
        description="Change font size")

    caseChangeFontSize2 = TestCase(
        stepRunCharacterMap(),
        stepSetFontSize(size=25.0),
        stepChangeFontSize(up=2, down=3),
        stepCheckFontSize(),
        description="Change font size")

    caseTestStatusBar1 = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepEnterCharacters(chars="B"),
        stepCheckStatusBar(),
        stepEnterCharacters(chars="XM"),
        stepCheckStatusBar(),
        description="Check status bar")

    caseTestStatusBar2 = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepCheckStatusBarSeriesOfChars(chars="AKLUISHEPWRN"),
        description="Check status bar")

