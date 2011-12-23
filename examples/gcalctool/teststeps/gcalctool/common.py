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

__all__ = ["stepRunCalculator", "stepCloseCalculator",
           "stepClearDisplay", "stepSwitchToView"]

app = Calculator()

@testStep(description="Run the calculator application")
def stepRunCalculator(test, device):
    app.launch(device)
    test.fail(app.isOpen(device), "Calculator does not run")

@testStep(description="Close the calculator application")
def stepCloseCalculator(test, device):
    test.fail(app.menu.Calculator.Quit.click(device),
              "Could not close the calculator application")
    test.fail(app.isClosed(device), "Calculator does not close")

@testStep(description="Clear the display")
def stepClearDisplay(test, device):
    test.fail(app.buttons.Clear.click(device), "Could not clear the display")
    test.fail(app.display.entry.hasText(device, ''),
             "Display entry is not clear")
    test.fail(app.display.status.hasText(device, ''),
             "Display status is not clear")

@testStep(description="Switch to the '%(view)s' view")
def stepSwitchToView(test, device, view="Basic"):
    obj = getattr(app.view, view)
    if obj.getImmediate(device):
        return
    item = getattr(app.menu.View, view)
    test.fail(item.click(device), "Could not switch to the '%s' view" % view)
    test.fail(obj.isShowing(device),
              "Calculator does not switch to the '%s' view" % view)

