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

import re
import random

from tadek.engine.testdefs import *
from tadek.models.tomboy import Tomboy
from tadek.core.locale import gettext as _


app = Tomboy()


@testStep(description="Restarts Tomboy")
def stepRestartTomboy(test, device):
    try:
        test.failThis(app.search.menu.File.Quit.click(device),
                      "Failed to click File/Quit")
        test.failThis(app.isClosed(device),
            "Tomboy application did not close after clicking File/Quit")
    finally:
        test.failThis(app.kill(device), "Failed to kill Tomboy application")
    test.failThis(app.launch(device),
        'Failed to execute command that launches Tomboy application')
    test.failThis(app.isOpen(device), "Tomboy did not run")

@testStep(description="Checks if Search window is open")
def stepCheckSearchWindow(test, device):
    test.fail(app.search.isExisting(device), "Search window did not open")

@testStep(description="Clicks on File/New and sets text of a new note")
def stepAddNewNote(test, device, text=None):
    test.fail(app.search.menu.File.New.click(device),
              "Failed to click File/New")
    i = 0
    for note in app.notes.childIter(device):
        i += 1
    if text is None:
        return
    note.text.type(device, text)
    newText = note.text.getText(device)
    test.fail(newText==text, "Text of not is '%s' while should be '%s'"
              % (newText, text))

@testStep(description="Checks number of entries on note list")
def stepCountNoteListEntries(test, device, count=0):
    i = 0
    for c in app.search.noteList.childIter(device):
        i += 1
    test.fail(i == count, "There are %d items on list while there should be %d"
              % (i, count))
        
@testStep(description="Checks number of entries on notebook list")
def stepCountNotebookListEntries(test, device, count=0):
    i = 0
    for c in app.search.notebookList.childIter(device):
        i += 1
    test.fail(i == count, "There are %d items on list while there should be %d"
              % (i, count))

@testStep(description="Checks if provided entry on note list exists")
def stepFindNoteOnList(test, device, name=""):
    test.fail(app.search.noteList.hasChild(device, name),
              "Entry: '%s' not found on note list" % name)

@testStep(description="Checks if provided entry on notebook list exists")
def stepFindNotebookOnList(test, device, name=""):
    test.fail(app.search.notebookList.hasChild(device, name),
              "Entry: '%s' not found on notebook list" % name)

@testStep(description="Clicks Delete on toolbar of note of given name")        
def stepDeleteNote(test, device, name=""):
    note = app.notes.getChild(name)
    test.fail(note.getImmediate(device), "Note '%s' was not found" % name)
    test.fail(note.toolbar.Delete.click(device),
              "Failed to click Delete on toolbar of note %s" % name)
    test.fail(app.question.isShowing(device), "Question dialog did not show")
    test.fail(app.question.Delete.click(device),
              "Failed to click Delete button")

@testStep(description="Enters a string into text field in Search window")
def stepEnterFilterText(test, device, text=""):
    test.fail(app.search.input.text.type(device, text),
              "Failed to enter text '%s' into text field" % text)

@testStep(description="Clicks File/Notebooks/New Notebook...")
def stepNewNotebook(test, device, name=""):
    test.fail(app.search.menu.File.Notebooks.NewNotebook.click(device),
              "Failed to click File/Notebooks/New Notebook...")
    test.fail(app.newNotebook.isShowing(device),
              "'Create a new notebook' dialog did not show")
    test.fail(app.newNotebook.text.type(device, name),
              "Failed to enter name of new notebook")
    test.fail(app.newNotebook.Create.click(device), "Failed to click 'Create'")
    test.failIf(app.newNotebook.isShowing(device, expectedFailure=True),
                "'Create a new notebook' dialog did not hide")

@testStep(description="Checks if search combo-box contain provided entries")
def stepCheckSearchHistory(test, device, list=[]):

    def listToStr(list):
        return ", ".join(("'%s'" % text for text in list)).strip(", ")

    actualList = []
    for item in app.search.input.menu.childIter(device):
        actualList.append(item.getName(device))
    test.fail(len(list) == len(actualList),
              "Entries are '%s' while should be '%s'"
              % (listToStr(actualList), listToStr(list)))
    match = True
    for t1, t2 in zip(actualList, list):
        if t1 != t2:
            match = False
            break
    test.fail(match, "Entries are '%s' while should be '%s'"
              % (listToStr(actualList), listToStr(list)))

@testStep(description="Clicks Edit/Preferences")
def stepOpenPreferences(test, device):
    test.fail(app.search.menu.Edit.Preferences.click(device),
              "Failed to click Edit/Preferences")
    test.fail(app.preferences.isOpen(device),
              "'Tomboy Preferences' dialog did not show")

@testStep(description="Opens 'Open New Note Template' window")
def stepOpenNewNoteTemplate(test, device, expectedName=""):
    test.fail(app.preferences.isOpen(device),
              "'Tomboy Preferences' dialog is closed")
    Editing = app.preferences.tabs.Editing
    if not Editing.isSelected(device):
        test.fail(Editing.mouseClick(device),
                  "Failed to mouse click on Editing tab")
    test.fail(Editing.isSelected(device),
              "Editing tab is not selected")
    test.fail(Editing.OpenNewNoteTemplate.click(device),
              "Failed to click 'Open New Note Template'")
    note = app.notes.getChild(expectedName)
    test.fail(note.isOpen(device),
              "'Open New Note Template' did not open")

@testStep(description="Types text into a note")
def stepSetNoteText(test, device, name="", text=""):
    note = app.notes.getChild(name)
    test.fail(note.isOpen(device), "'%s' is not open" % name)
    note.text.type(device, text)
    noteText = note.text.getText(device)
    test.fail(noteText==text, "Text of note '%s' is '%s' while should be '%s'"
              % (name, noteText, text))

@testStep(description="checks if text of a note matches the given one")
def stepCheckNoteText(test, device, name="", text=""):
    note = app.notes.getChild(name)
    test.fail(note.isOpen(device), "'%s' is not open" % name)
    noteText = note.text.getText(device)
    if text[0] == "&":
        text = text[1:]
    test.fail(re.match(text, noteText),
              "Text of note '%s' is '%s' while should be '%s'"
              % (name, noteText, text))

@testStep(description="Adds a random number of notes")
def stepAddRandomNotes(test, device):
    noteCount = random.randint(2,10)
    test['noteCount'] = noteCount
    for i in range(1, noteCount+1):
        stepAddNewNote.run(test, device)

@testStep(description="Check number of items on note list")
def stepCheckRandomNotesOnList(test, device):
    noteCount = test['noteCount']
    count = 0
    for item in app.search.noteList.childIter(device):
        count += 1
    test.fail(count == noteCount,
              "There are %d items on list while should be %d"
              % (count, noteCount))

@testStep(description="Check number of notes shown on status bar")
def stepCheckRandomNotesOnStatusBar(test, device):
    expectedText = _("Total", device) + ": %s " % test['noteCount']
    text = app.search.status.getText(device)
    test.fail(expectedText in text,
              "Status bar text does not contain: '%s'" % expectedText)