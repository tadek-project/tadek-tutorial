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

app = CharacterMap()

@testStep(description="Run the Character Map application")
def stepRunCharacterMap(test, device):
    app.launch(device)
    test.fail(app.isOpen(device), "Character Map application does not run")

@testStep(description="Close the Character Map application")
def stepCloseCharacterMap(test, device):
    app.menu.File.Close.click(device)
    test.fail(app.isClosed(device), "Character Map application does not close")

@testStep(description="Activate a sequence of characters")
def stepEnterCharacters(test, device, chars=""):
    startingSequence = app.view.Text.getText(device)
    for char in chars:
        app.view.CharacterTable.getChild(ord(char)).doAction(device, "ACTIVATE")
    test.fail(app.view.Text.getText(device)==startingSequence+chars,
        "Wrong text")
    return chars

@testStep(description="Choose script Common")
def stepCommon(test, device):
    app.menu.View.ByScript.click(device)
    app.view.Script.Common.grabFocus(device)
    test.fail(app.view.Script.Common.isSelected(device), "Common Script not selected")

@testStep(description="Simulate typing characters")
def stepEnterKeyboardCharacters(test, device, chars=""):
    app.view.Text.grabFocus(device)
    for char in chars:
        app.generateKey(device, ord(char))
    test.fail(app.view.Text.getText(device)==chars, "Wrong text")

@testStep(description="Simulate typing characters with modifiers")
def stepEnterKeyboardCharactersWithModifiers(test, device, chars=[],
        textToCompare=""):
    app.view.Text.grabFocus(device)
    app.generateKey(device, 'RIGHT')
    for char in chars:
        if isinstance(char, (tuple, list)):
            modifiers = char[1:]
            char = char[0]
        else:
            modifiers = ()
        if len(char)==1:
            char = ord(char)
        app.generateKey(device, char, modifiers)
    test.fail(app.view.Text.getText(device)==textToCompare, "Wrong text")

@testStep(description="Type characters")
def stepTypeCharacters(test, device, chars=""):
    app.view.Text.type(device, chars)
    test.fail(app.view.Text.getText(device)==chars, "Wrong text")

@testStep(description="Choose script Latin")
def stepLatin(test, device):
    app.menu.View.ByScript.click(device)
    app.view.Script.Latin.grabFocus(device)
    test.fail(app.view.Script.Latin.isSelected(device),
        "Latin Script not selected")

@testStep(description="Activate letters with Space or Enter")
def stepActivateLettersWithKeyboard(test, device, letters="",
        activatingKey=KEY_CODES["SPACE"]):
    previous = "A"
    app.view.CharacterTable.grabFocus(device)
    for letter in letters:
        distance = (abs(ord(letter)-ord(previous))-
            (ord('a')-ord('Z')-1)*(letter.isupper()!=previous.isupper()))
        if letter>previous:
            for i in xrange(distance):
                app.menu.Go.NextCharacter.click(device)
        elif letter<previous:
            for i in xrange(distance):
                app.menu.Go.PreviousCharacter.click(device)
        previous = letter
        app.generateKey(device, activatingKey)
    test.fail(app.view.Text.getText(device)==letters, "Wrong text")

@testStep(description="Copy text to clipboard")
def stepCopy(test, device):
    app.view.Copy.click(device)

@testStep(description="Copy text to clipboard")
def stepPopUpCopy(test, device):
    app.view.Text.grabFocus(device)
    app.view.Text.mouseClick(device, "RIGHT")
    app.popUpMenu.Copy.click(device)

@testStep(description="Paste text from clipboard to the text field")
def stepPaste(test, device):
    startingSequence = app.view.Text.getText(device)
    app.view.Text.grabFocus(device)
    app.keyRight(device)
    app.view.Text.mouseClick(device, "RIGHT")
    app.popUpMenu.Paste.click(device)
    test.fail(app.view.Text.getText(device)==startingSequence+startingSequence,
        "Text not pasted correctly")

@testStep(description="Show and check a popup menu with a character")
def stepPopUpCharacter(test, device):
    app.view.CharacterTable.mousePress(device, "RIGHT")
    status = app.popUpCharacter.isExisting(device)
    app.view.CharacterTable.mouseRelease(device, "RIGHT")
    test.fail(status, "Icon does not exist")

@testStep(description="Test 'About' dialog")
def stepAboutDialog(test, device):
    app.menu.Help.About.click(device)
    test.fail(app.dialogs.About.isOpen(device),
        "Dialog was not opened")
    app.dialogs.About.Buttons.Close.click(device)
    test.fail(app.dialogs.About.isClosed(device),
        "Dialog is still open")

@testStep(description="Change a font size")
def stepChangeFontSize(test, device, up=1, down=0):
    app.font.FontSize.grabFocus(device)
    for i in xrange(up):
        app.generateKey(device, 'UP')
    for i in xrange(down):
        app.generateKey(device, 'DOWN')
    test["up"] = up
    test["down"] = down

@testStep(description="Set a font size")
def stepSetFontSize(test, device, size=0.0):
    app.font.FontSize.grabFocus(device)
    app.font.FontSize.setValue(device, size)
    test["size"] = size

@testStep(description="Test a font size")
def stepCheckFontSize(test, device):
    app.font.FontSize.grabFocus(device)
    size = test["size"] if test["size"] else 0.0
    up = test["up"] if test["up"] else 0
    down = test["down"] if test["down"] else 0
    size += up-down
    test.fail(app.font.FontSize.getValue(device)==size,
        "Font size is incorrect")

@testStep(description="Check status bar")
def stepCheckStatusBar(test, device):
    char = test["result"][-1]
    test.fail(app.view.StatusBar.getText(device)[:29]==
        "U+%04X LATIN CAPITAL LETTER %c"%(ord(char), char),
        "Incorrect status bar")

@testStep(description="Check status bar")
def stepCheckStatusBarSeriesOfChars(test, device, chars=""):
    for char in chars:
        stepEnterCharacters(chars=char).run(test, device)
        stepCheckStatusBar().run(test, device)

