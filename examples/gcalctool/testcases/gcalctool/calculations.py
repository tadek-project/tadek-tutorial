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

from tadek.engine.testdefs import TestCase
from tadek.teststeps.gcalctool.calculation import *
from tadek.core.locale import gettext__ as _

__all__ = ["caseAddition", "caseSubtraction", "caseMultiplication",
           "caseDivision", "caseMalformed"]

caseAddition = TestCase(stepClickButton(button='3'),
                        stepClickButton(button='7'),
                        stepClickButton(button='+'),
                        stepClickButton(button='5'),
                        stepClickButton(button='9'),
                        stepCalculateResult(result="96"),
                        description="Calculate 37 + 59")

caseSubtraction = TestCase(stepClickButton(button='8'),
                           stepClickButton(button='2'),
                           stepClickButton(button='3'),
                           stepClickButton(button='-'),
                           stepClickButton(button='6'),
                           stepClickButton(button='5'),
                           stepClickButton(button='8'),
                           stepCalculateResult(result="165"),
                           description="Calculate 823 - 658")

caseMultiplication = TestCase(stepClickButton(button='4'),
                              stepClickButton(button='6'),
                              stepClickButton(button='2'),
                              stepClickButton(button='*'),
                              stepClickButton(button='8'),
                              stepClickButton(button='5'),
                              stepClickButton(button='7'),
                              stepCalculateResult(result="395934"),
                              description="Calculate 462 * 857")

caseDivision = TestCase(stepClickButton(button='5'),
                        stepClickButton(button='6'),
                        stepClickButton(button='/'),
                        stepClickButton(button='8'),
                        stepCalculateResult(result='7'),
                        description="Calculate 56 / 8")

caseMalformed = TestCase(stepClickButton(button='1'),
                        stepClickButton(button='0'),
                        stepClickButton(button='%'),
                        stepClickButton(button='2'),
                        stepClickButton(button='9'),
                        stepCalculateResult(result="10%29",
                                            status=_("Malformed expression")),
                        description="Calculate 10 % 29")

