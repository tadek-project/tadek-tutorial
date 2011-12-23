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
from tadek.teststeps.tomboy.basic import *
from tadek.core.locale import gettext__ as _


class BasicSuite(TestSuite):

    description = "Tests basic functionalities of the Tomboy application"

    def setUpSuite(self, test, device):
        test.fail(app.kill(device), "Failed to kill Tomboy application")

    def setUpCase(self, test, device):
        test.fail(app.removeSettings(device),
                  "Failed to remove settings of Tomboy application")
        test.fail(app.launch(device),
                  "Failed to execute command that launches Tomboy application")
        test.fail(app.isOpen(device), "Tomboy application did not run")
    
    def tearDownCase(self, test, device):
        try:
            test.fail(app.search.menu.File.Quit.click(device),
                      "Failed to click File/Quit")
            test.fail(app.isClosed(device),
                "Tomboy application did not close after clicking File/Quit")
        finally:
            test.fail(app.kill(device), "Failed to kill Tomboy application")

    caseSearchWindow = TestCase(
        stepCheckSearchWindow(),
        description="Checks is Search window opens on startup")

    caseAddNote = TestCase(
        stepAddNewNote(),
        stepCountNoteListEntries(count=1),
        stepFindNoteOnList(name=_("New Note")+" 1"),
        description="Adds a note")

    caseDeleteNote = TestCase(
        stepAddNewNote(),
        stepCountNoteListEntries(count=1),
        stepFindNoteOnList(name=_("New Note")+" 1"),
        stepDeleteNote(name=_("New Note")+" 1"),
        stepCountNoteListEntries(count=0),
        description="Adds a note")

    caseNoteText = TestCase(
        stepAddNewNote(text="text "*10),
        description="Enters a text in note's window")

    caseNoteTitle = TestCase(
        stepAddNewNote(text="title\n"+"text "*10),
        stepFindNoteOnList(name="title"),
        stepCountNoteListEntries(count=1),
        description="Sets title of new note")

    caseAddMoreNotes = TestCase(
        stepAddNewNote(text="note 1\n"+"text "*10),
        stepAddNewNote(text="note 2\n"+"text "*10),
        stepAddNewNote(text="note 3\n"+"text "*10),
        stepCountNoteListEntries(count=3),
        stepFindNoteOnList(name="note 1"),
        stepFindNoteOnList(name="note 2"),
        stepFindNoteOnList(name="note 3"),
        description="Adds three new notes")

    caseAddRandomNumberOfNotes = TestCase(
        stepAddRandomNotes(),
        stepCheckRandomNotesOnList(),
        stepCheckRandomNotesOnStatusBar(),
        description="Adds a random number of notes")

    caseSearchNotes = TestCase(
        stepAddNewNote(text="yellow blue\n"+"olive red "*10),
        stepAddNewNote(text="brown green\n"+"black pink "*10),
        stepAddNewNote(text="black white\n"+"orange yellow "*10),
        stepCountNoteListEntries(count=3),
        stepFindNoteOnList(name="yellow blue"),
        stepFindNoteOnList(name="brown green"),
        stepFindNoteOnList(name="black white"),
        stepEnterFilterText(text="yellow"),
        stepFindNoteOnList(name="yellow blue"),
        stepFindNoteOnList(name="black white"),
        stepEnterFilterText(text="black"),
        stepFindNoteOnList(name="brown green"),
        stepFindNoteOnList(name="black white"),
        description="Searches notes")

    caseAddNotebook = TestCase(
        stepCountNotebookListEntries(count=2),
        stepFindNotebookOnList(name=_("All Notes")),
        stepFindNotebookOnList(name=_("Unfiled Notes")),
        stepNewNotebook(name="dummy notebook"),
        stepCountNotebookListEntries(count=3),
        stepFindNotebookOnList(name="dummy notebook"),
        description="Adds a new notebook")

    caseSearchHistory = TestCase(
        stepCheckSearchHistory(list=[]),
        stepEnterFilterText(text="first"),
        stepEnterFilterText(text="second"),
        stepEnterFilterText(text="third"),
        stepCheckSearchHistory(list=["third", "second", "first"]),
        desctiption="Checks search history")

    caseNoteTemplate = TestCase(
        stepOpenPreferences(),
        stepOpenNewNoteTemplate(expectedName=_("New Note Template")),
        stepSetNoteText(name=_("New Note Template"),
                        text=_("New Note Template")+"\n"+"text 123"),
        stepAddNewNote(),
        stepCheckNoteText(name="&"+_("New Note")+" [0-9]+.*",
                          text="&"+_("New Note")+" [0-9]+\ntext 123"),
        description="Sets template for new notes")

    caseNotesPersistance = TestCase(
        stepAddNewNote(text="note 1\n"+"text "*10),
        stepAddNewNote(text="note 2\n"+"text "*10),
        stepAddNewNote(text="note 3\n"+"text "*10),
        stepRestartTomboy(),
        stepCountNoteListEntries(count=3),
        stepFindNoteOnList(name="note 1"),
        stepFindNoteOnList(name="note 2"),
        stepFindNoteOnList(name="note 3"),
        description="Adds three new notes and checks if they are present after "
            "restart")
