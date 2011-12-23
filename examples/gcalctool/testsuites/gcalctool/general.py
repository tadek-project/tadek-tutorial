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

from tadek.engine.testdefs import TestCase, TestSuite
from tadek.models.gcalctool import Calculator
from tadek.teststeps.gcalctool.common import *
from tadek.teststeps.gcalctool.calculation import *
from tadek.testcases.gcalctool.views import *

app = Calculator()

class GeneralSuite(TestSuite):
    description = "Test functionality of the calculator application"

    def setUpSuite(self, test, device):
        if app.getImmediate(device):
            app.kill(device)
            test.abortIf(app.getImmediate(device), "Could not kill running "
                         "instances of the calculator application")

    def tearDownCase(self, test, device):
        if app.getImmediate(device):
            app.menu.Calculator.Quit.click(device)

    caseRunClose = TestCase(stepRunCalculator(), stepCloseCalculator(),
                    description="Run and then close the calculator application")

    caseClearDisplay = TestCase(stepRunCalculator(),
                                stepClickButton(button='5'),
                                stepClearDisplay(),
                    description="Clear the calculator display after running")

    caseBasicCalculations = BasicView()
    caseAdvancedCalculations = AdvancedView()
    caseFinancialCalculations = FinancialView()
    caseScientificCalculations = ScientificView()
    caseProgrammingCalculations = ProgrammingView()

