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

from tadek.engine.searchers import *
from tadek.engine.widgets import *
from tadek.models import Model
from tadek.core.locale import gettext__ as _


__all__ = ["Tomboy"]


# Searchers 

class _note(structure):
    def __init__(self, name=None, state=None, nth=0):
        structure.__init__(self, name=name, role="FRAME", state=state, nth=nth,
                           searchers=(toolbar__(), text__()))

class _list(tablecell__):
    def __init__(self, name=None, state=None, nth=0):
        tablecell__.__init__(self, name=name, state=state, nth=nth, index=1,
                             count=0)

# Widgets

class Note(Dialog):
    '''
    Note window
    '''
    def __init__(self, *path):
        Widget.__init__(self, *path)

        self.define("toolbar", Widget(filler(), toolbar()))
        self.define("toolbar.Delete", Button(button__(_("Delete"))))
        self.define("text", Entry(filler(), scrollpane(), text()))


class Notes(Container):
    '''
    Container for note windows
    '''
    class_of_children = Note
    searcher_of_children = _note
    state_of_current = "ACTIVE"


class List(Container):
    '''
    Container for list entries
    '''
    searcher_of_children = _list
    state_of_current = "ACTIVE"


class SearchMenu(Container):
    '''
    container for last searched values
    '''
    class_of_children = MenuItem
    searcher_of_children = menuitem


class Tomboy(Model):
    '''
    Model of Tomboy application
    '''

    root = App("tomboy --search",
               searcher("AT-SPI"),
               structure(role="APPLICATION",
                         searchers=(frame(_("Search All Notes")),)))
    #Search window
    #    Menu
    root.define("search", Widget(frame(_("Search All Notes"))))
    root.define("search.menu", Widget(menubar__()))
    root.define("search.menu.File", Menu(menu(_("File"))))
    root.define("search.menu.File.New", MenuItem(menuitem(_("New"))))
    root.define("search.menu.File.Notebooks", Menu(menu(_("Notebooks"))))
    root.define("search.menu.File.Notebooks.NewNotebook",
                MenuItem(menuitem(_("New Notebook..."))))
    root.define("search.menu.File.Open", MenuItem(menuitem(_("Open..."))))
    root.define("search.menu.File.Close", MenuItem(menuitem(_("Close"))))
    root.define("search.menu.File.Quit", MenuItem(menuitem(_("Quit"))))
    root.define("search.menu.Edit", Menu(menu(_("Edit"))))
    root.define("search.menu.Edit.Preferences", MenuItem(
                menuitem(_("Preferences"))))

    #    Notes
    root.define("search.noteList", List(splitpane__(),
                structure(role="SCROLL_PANE",
                          searchers=(tablecolumnheader__(_("Note")),)),
                table()))
    root.define("search.notebookList", List(splitpane__(),
                structure(role="SCROLL_PANE",
                          searchers=(tablecolumnheader__(_("Notebooks")),)),
                table()))
    #    Input
    root.define("search.input", Widget(filler(), filler(),
                structure(role="FILLER", searchers=(button__(), text__()))))
    root.define("search.input.text", Entry(text__()))
    root.define("search.input.menu", SearchMenu(combobox__(), menu()))
    #    Status bar
    root.define("search.status", Widget(filler(), filler(), statusbar()))

    #Note windows
    root.define("notes", Notes())

    #Preferences dialog
    root.define("preferences", Dialog(dialog(_("Tomboy Preferences"))))
    root.define("preferences.Close", Button(button__(_("Close"))))
    root.define("preferences.tabs", Widget(pagetablist__()))
    root.define("preferences.tabs.Editing", Widget(pagetab(_("Editing"))))
    root.define("preferences.tabs.Editing.OpenNewNoteTemplate", Button(
                button__(_("Open New Note Template"))))
    root.define("preferences.tabs.Hotkeys", Widget(pagetab(_("Hotkeys"))))

    #Question dialog
    root.define("question", Dialog(structure(role="DIALOG",
                searchers=(icon__(_("Question")),))))
    root.define("question.Delete", Button(button__(_("Delete"))))
    root.define("question.Cancel", Button(button__(_("Cancel"))))

    # New notebook dialog
    root.define("newNotebook", Dialog(structure(role="DIALOG",
                searchers=(label__("&.*" + _("Create a new notebook")
                                   + ".*"),))))
    root.define("newNotebook.text", Entry(text__()))
    root.define("newNotebook.Create", Button(button__(_("Create"))))
    root.define("newNotebook.Cancel", Button(button__(_("Cancel"))))

    def kill(self, device):
        '''
        Kills the Tomboy application.

        :param device: A device to perform the operation on
        :type device: tadek.connection.device.Device
        :return: True if successful or there is nothing to kill, False otherwise
        :rtype: boolean
        '''
        pids = self.systemCommand(device, "pgrep tomboy")[1]
        if pids:
            self.systemCommand(device, "kill %s" % pids)
            return self.isClosed(device)
        return True
    
    def removeSettings(self, device):
        '''
        Removes configuration files of Tomboy application from user's home

        :param device: A device to perform the operation on
        :type device: tadek.connection.device.Device
        :return: True if successful or there is nothing to remove, False
            otherwise
        :rtype: boolean
        '''
        path = "~/.local/share/tomboy"
        self.systemCommand(device, "rm -R %s/*" % path)
        lsOut = self.systemCommand(device, "ls %s -1 | wc -l" % path)[1]
        return not (lsOut.strip() != "0")

