# -*- coding: utf-8 -*-

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

'''
A model for the GNOME calculator application (gcalctool).
Version of gcalctool: 5.30.2
'''

from tadek.engine.searchers import *
from tadek.engine.widgets import *
from tadek.models import Model
from tadek.core.locale import gettext__ as _

__all__ = ["Calculator"]

class Calculator(Model):
    root = App("gcalctool", searcher("AT-SPI"), application("gcalctool"))
    # Menu
    root.define("menu", Widget(filler__(), menubar()))
    root.define("menu.Calculator", Menu(menu(_("Calculator"))))
    root.define("menu.Calculator.Copy", MenuItem(menuitem(_("Copy"))))
    root.define("menu.Calculator.Paste", MenuItem(menuitem(_("Paste"))))
    root.define("menu.Calculator.Quit", MenuItem(menuitem(_("Quit"))))
    root.define("menu.View", Menu(menu(_("View"))))
    root.define("menu.View.Basic", MenuItem(radiomenuitem(_("Basic"))))
    root.define("menu.View.Advanced", MenuItem(radiomenuitem(_("Advanced"))))
    root.define("menu.View.Financial", MenuItem(radiomenuitem(_("Financial"))))
    root.define("menu.View.Scientific", MenuItem(radiomenuitem(_("Scientific"))))
    root.define("menu.View.Programming", MenuItem(radiomenuitem(_("Programming"))))
    root.define("menu.Help", Menu(menu(_("Help"))))
    root.define("menu.Help.Contents", MenuItem(menuitem(_("Contents"))))
    root.define("menu.Help.About", MenuItem(menuitem(_("About"))))
    # Display
    root.define("display", Widget(viewport__()))
    root.define("display.entry", Entry(searcher__(role="EDITBAR")))
    root.define("display.status", Widget(text__()))
    # Views
    root.define("buttons", Widget(filler__(), panel(count=6)))
    root.define("buttons.Zero", Button(button__('0')))
    root.define("buttons.One", Button(button__('1')))
    root.define("buttons.Two", Button(button__('2')))
    root.define("buttons.Three", Button(button__('3')))
    root.define("buttons.Four", Button(button__('4')))
    root.define("buttons.Five", Button(button__('5')))
    root.define("buttons.Six", Button(button__('6')))
    root.define("buttons.Seven", Button(button__('7')))
    root.define("buttons.Eight", Button(button__('8')))
    root.define("buttons.Nine", Button(button__('9')))
    root.define("buttons.Point", Button(button__('.')))
    root.define("buttons.Add", Button(button__('+')))
    root.define("buttons.Subtract", Button(button__('−')))
    root.define("buttons.Multiply", Button(button__('×')))
    root.define("buttons.Divide", Button(button__('÷')))
    root.define("buttons.Percentage", Button(button__('%')))
    root.define("buttons.Calculate", Button(button__('=')))
    root.define("buttons.Clear", Button(button__(_("Clr"))))
    root.define("view", Widget())
    root.define("view.Basic", Widget(frame(_("Calculator"))))
    root.define("view.Advanced",
                Widget(frame(_("Calculator") + " —" + _(" Advanced"))))
    root.define("view.Financial",
                Widget(frame(_("Calculator") + " —" + _(" Financial"))))
    root.define("view.Scientific",
                Widget(frame(_("Calculator") + " —" + _(" Scientific"))))
    root.define("view.Programming",
                Widget(frame(_("Calculator") + " —" + _(" Programming"))))
    # Dialogs
    root.define("dialogs", Widget())
    root.define("dialogs.About", Dialog(dialog("&" + _("About") + ".*")))
    root.define("dialogs.About.buttons", Widget())
    root.define("dialogs.About.buttons.Credits", Button(button__(_("Credits"))))
    root.define("dialogs.About.buttons.Licence", Button(button__(_("Licence"))))
    root.define("dialogs.About.buttons.Close", Button(button__(_("Close"))))

