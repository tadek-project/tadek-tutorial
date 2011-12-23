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
from tadek.testcases.gcalctool.views import *

app = Calculator()

class AdditionSuite(TestSuite):
    description = "Test addition functionality of the calculator application"

    def tearDownCase(self, test, device):
        if app.getImmediate(device):
            app.menu.Calculator.Quit.click(device)

    caseBasic = BasicView("caseAddition")
    caseAdvanced = AdvancedView("caseAddition")
    caseFinancial = FinancialView("caseAddition")
    caseScientific = ScientificView("caseAddition")
    caseProgramming = ProgrammingView("caseAddition")


class SubtractionSuite(TestSuite):
    description = "Test subtraction functionality of the calculator application"

    def tearDownCase(self, test, device):
        if app.getImmediate(device):
            app.menu.Calculator.Quit.click(device)

    caseBasic = BasicView("caseSubtraction")
    caseAdvanced = AdvancedView("caseSubtraction")
    caseFinancial = FinancialView("caseSubtraction")
    caseScientific = ScientificView("caseSubtraction")
    caseProgramming = ProgrammingView("caseSubtraction")


class MultiplicationSuite(TestSuite):
    description = "Test multiplication functionality of the calculator application"

    def tearDownCase(self, test, device):
        if app.getImmediate(device):
            app.menu.Calculator.Quit.click(device)

    caseBasic = BasicView("caseMultiplication")
    caseAdvanced = AdvancedView("caseMultiplication")
    caseFinancial = FinancialView("caseMultiplication")
    caseScientific = ScientificView("caseMultiplication")
    caseProgramming = ProgrammingView("caseMultiplication")


class DivisionSuite(TestSuite):
    description = "Test division functionality of the calculator application"

    def tearDownCase(self, test, device):
        if app.getImmediate(device):
            app.menu.Calculator.Quit.click(device)

    caseBasic = BasicView("caseDivision")
    caseAdvanced = AdvancedView("caseDivision")
    caseFinancial = FinancialView("caseDivision")
    caseScientific = ScientificView("caseDivision")
    caseProgramming = ProgrammingView("caseDivision")

