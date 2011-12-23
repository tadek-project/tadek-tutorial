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
from tadek.teststeps.gcalctool.common import *
from tadek.testcases.gcalctool.calculations import *

__all__ = ["BasicView", "AdvancedView", "FinancialView",
           "ScientificView", "ProgrammingView"]

caseRunBasic = TestCase(stepRunCalculator(), stepSwitchToView(view="Basic"),
                        description = "Run calculator in the basic view")

class BasicView(TestSuite):
    description = "The basic view test cases"

    caseAddition = TestCase(caseRunBasic(), caseAddition(),
                            description = "Calculate 37 + 59 in the basic view")
    caseSubtraction = TestCase(caseRunBasic(), caseSubtraction(),
                        description = "Calculate 823 - 658 in the basic view")
    caseMultiplication = TestCase(caseRunBasic(), caseMultiplication(),
                        description = "Calculate 462 * 857 in the basic view")
    caseDivision = TestCase(caseRunBasic(), caseDivision(),
                            description = "Calculate 56 / 8 in the basic view")
    caseMalformed = TestCase(caseRunBasic(), caseMalformed(),
                            description = "Calculate 10 % 29 in the basic view")

caseRunAdvanced = TestCase(stepRunCalculator(),
                           stepSwitchToView(view="Advanced"),
                        description = "Run calculator in the advanced view")

class AdvancedView(TestSuite):
    description = "The advanced view test cases"

    caseAddition = TestCase(caseRunAdvanced(), caseAddition(),
                        description = "Calculate 37 + 59 in the advanced view")
    caseSubtraction = TestCase(caseRunAdvanced(), caseSubtraction(),
                    description = "Calculate 823 - 658 in the advanced view")
    caseMultiplication = TestCase(caseRunAdvanced(), caseMultiplication(),
                    description = "Calculate 462 * 857 in the advanced view")
    caseDivision = TestCase(caseRunAdvanced(), caseDivision(),
                        description = "Calculate 56 / 8 in the advanced view")
    caseMalformed = TestCase(caseRunAdvanced(), caseMalformed(),
                        description = "Calculate 10 % 29 in the advanced view")


caseRunFinancial = TestCase(stepRunCalculator(),
                            stepSwitchToView(view="Financial"),
                        description = "Run calculator in the financial view")

class FinancialView(TestSuite):
    description = "The financial view test cases"

    caseAddition = TestCase(caseRunFinancial(), caseAddition(),
                        description = "Calculate 37 + 59 in the financial view")
    caseSubtraction = TestCase(caseRunFinancial(), caseSubtraction(),
                    description = "Calculate 823 - 658 in the financial view")
    caseMultiplication = TestCase(caseRunFinancial(), caseMultiplication(),
                    description = "Calculate 462 * 857 in the financial view")
    caseDivision = TestCase(caseRunFinancial(), caseDivision(),
                        description = "Calculate 56 / 8 in the financial view")
    caseMalformed = TestCase(caseRunFinancial(), caseMalformed(),
                        description = "Calculate 10 % 29 in the financial view")


caseRunScientific = TestCase(stepRunCalculator(),
                             stepSwitchToView(view="Scientific"),
                        description = "Run calculator in the scientific view")

class ScientificView(TestSuite):
    description = "The scientific view test cases"

    caseAddition = TestCase(caseRunScientific(), caseAddition(),
                    description = "Calculate 37 + 59 in the scientific view")
    caseSubtraction = TestCase(caseRunScientific(), caseSubtraction(),
                    description = "Calculate 823 - 658 in the scientific view")
    caseMultiplication = TestCase(caseRunScientific(), caseMultiplication(),
                    description = "Calculate 462 * 857 in the scientific view")
    caseDivision = TestCase(caseRunScientific(), caseDivision(),
                        description = "Calculate 56 / 8 in the scientific view")
    caseMalformed = TestCase(caseRunScientific(), caseMalformed(),
                            description = "Calculate 10 % 29 in the scientific view")


caseRunProgramming = TestCase(stepRunCalculator(),
                              stepSwitchToView(view="Programming"),
                        description = "Run calculator in the programming view")

class ProgrammingView(TestSuite):
    description = "The programming view test cases"

    caseAddition = TestCase(caseRunProgramming(), caseAddition(),
                    description = "Calculate 37 + 59 in the programming view")
    caseSubtraction = TestCase(caseRunProgramming(), caseSubtraction(),
                    description = "Calculate 823 - 658 in the programming view")
    caseMultiplication = TestCase(caseRunProgramming(), caseMultiplication(),
                    description = "Calculate 462 * 857 in the programming view")
    caseDivision = TestCase(caseRunProgramming(), caseDivision(),
                    description = "Calculate 56 / 8 in the programming view")
    caseMalformed = TestCase(caseRunProgramming(), caseMalformed(),
                            description = "Calculate 10 % 29 in the programming view")

