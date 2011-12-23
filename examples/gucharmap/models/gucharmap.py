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

__all__ = ["CharacterMap"]

class TableContainer(Container):
    searcher_of_children = tablecell

class CharacterMap(Model):
    root = App("LC_ALL= LANG= gucharmap", searcher("AT-SPI"),
        application("gucharmap"))
    # Menu
    root.define("popUpMenu", Widget(window(), menu("")))
    root.define("popUpMenu.Paste", MenuItem(menuitem("Paste")))
    root.define("popUpMenu.Copy", MenuItem(menuitem("Copy")))
    root.define("popUpCharacter", Widget(window(), icon()))
    root.define("menu", Widget(filler__(), menubar()))
    root.define("menu.File", MenuItem(menu("File")))
    root.define("menu.File.Close", MenuItem(menuitem("Close")))
    root.define("menu.View", MenuItem(menu("View")))
    root.define("menu.View.ByScript", MenuItem(checkmenuitem("By Script")))
    root.define("menu.View.ByUnicodeBlock",
        MenuItem(checkmenuitem("By Unicode Block")))
    root.define("menu.View.SnapColumnsToPowerOfTwo",
        MenuItem(checkmenuitem("Snap Columns to Power of Two")))
    root.define("menu.View.ZoomIn", MenuItem(menuitem("Zoom In")))
    root.define("menu.View.ZoomOut", MenuItem(menuitem("Zoom Out")))
    root.define("menu.View.NormalSize", MenuItem(menuitem("Normal Size")))
    root.define("menu.Search", MenuItem(menu("Search")))
    root.define("menu.Search.Find", MenuItem(menuitem("Find")))
    root.define("menu.Search.FindNext", MenuItem(menuitem("Find Next")))
    root.define("menu.Search.FindPrevious", MenuItem(menuitem("Find Previous")))
    root.define("menu.Go", MenuItem(menu("Go")))
    root.define("menu.Go.NextCharacter", MenuItem(menuitem("Next Character")))
    root.define("menu.Go.PreviousCharacter",
        MenuItem(menuitem("Previous Character")))
    root.define("menu.Go.NextScript", MenuItem(menuitem("Next Script")))
    root.define("menu.Go.PreviousScript", MenuItem(menuitem("Previous Script")))
    root.define("menu.Help", MenuItem(menu("Help")))
    root.define("menu.Help.Contents", MenuItem(menuitem("Contents")))
    root.define("menu.Help.About", MenuItem(menuitem("About")))

    root.define("font", Widget())
    root.define("font.FontSize", Valuator(spinbutton__("Font Size")))

    root.define("view", Widget())
    root.define("view.Script", Widget(table__("")))
    root.define("view.Script.Arabic", Widget(tablecell("Arabic")))
    root.define("view.Script.Latin", Widget(tablecell("Latin")))
    root.define("view.Script.Common", Widget(tablecell("Common")))
    root.define("view.CharacterTable", TableContainer(table__("Character Table")))
    root.define("view.Text", Entry(text__()))
    root.define("view.Copy", Button(button__("Copy")))
    root.define("view.StatusBar", Widget(statusbar__()))

    # Dialogs
    root.define("dialogs", Widget())
    root.define("dialogs.About", Dialog(dialog("&About.*")))
    root.define("dialogs.About.Buttons", Widget())
    root.define("dialogs.About.Buttons.Credits", Button(button__("Credits")))
    root.define("dialogs.About.Buttons.Licence", Button(button__("Licence")))
    root.define("dialogs.About.Buttons.Close", Button(button__("Close")))
