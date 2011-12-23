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

from tadek.engine.testdefs import testStep
from tadek.models.gcalctool import Calculator

__all__ = ["stepClickButton", "stepCalculateResult"]

app = Calculator()

_buttonMap = {
    '0': ('0', app.buttons.Zero),
    '1': ('1', app.buttons.One),
    '2': ('2', app.buttons.Two),
    '3': ('3', app.buttons.Three),
    '4': ('4', app.buttons.Four),
    '5': ('5', app.buttons.Five),
    '6': ('6', app.buttons.Six),
    '7': ('7', app.buttons.Seven),
    '8': ('8', app.buttons.Eight),
    '9': ('9', app.buttons.Nine),
    '.': ('.', app.buttons.Point),
    '+': ('+', app.buttons.Add),
    '-': ('−', app.buttons.Subtract),
    '*': ('×', app.buttons.Multiply),
    '/': ('÷', app.buttons.Divide),
    '%': ('%', app.buttons.Percentage)
}

@testStep(description="Click a '%(button)s' button")
def stepClickButton(test, device, button='1'):
    text = _buttonMap[button][0]
    if test["result"]:
        text = test["result"] + text
    test.fail(_buttonMap[button][1].click(device),
              "Could not click the '%s' button" % button)
    if not app.display.entry.hasText(device, text):
         test.fail(False, "Incorrect text displayed: %s"
                            % app.display.entry.getText(device))
    return text

@testStep(description="Calculate a result")
def stepCalculateResult(test, device, result='', status=''):
    test.fail(app.buttons.Calculate.click(device), "Could not calculate result")
    if not app.display.entry.hasText(device, result):
        test.fail(False, "Incorrect result displayed: %s"
                            % app.display.entry.getText(device))
    if not app.display.status.hasText(device, status):
        test.fail(False, "Incorrect status displayed: %s"
                            % app.display.status.getText(device))

