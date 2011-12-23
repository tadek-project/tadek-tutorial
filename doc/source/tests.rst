Test Case Development
*********************

Like models, test cases in TADEK are written in Python. To start writing test
cases, basic knowledge on :ref:`models <models>` and
:ref:`locations <running_locations>` is needed.

.. _tests_simple_test_case:

Simple Test Case
================

A simple test case can be written very easily with use of
:epylink:`tadek.engine.testdefs.testCase` decorator. The following definition
uses tomboy model that can be found in the
:ref:`examples <installation_examples>`.

.. code-block:: python
    :linenos:

    from tadek.engine.testdefs import testCase
    from tadek.models.tomboy import Tomboy

    app = Tomboy()


    @testCase()
    def openPreferences(test, device):
        test.fail(app.launch(device), "Tomboy did not open")
        test.fail(app.search.menu.Edit.Preferences.click(device),
                  "Failed to click Preferences in Edit menu")
        test.fail(app.preferences.isShowing(device),
                  "Preferences window did not show")

The test case launches tomboy application, clicks on
:menuselection:`Edit --> Preferences` in the main menu of Search window and
checks if the Preferences dialog opens. All these interactions are made by
calling methods of respective widgets of the model which is instantiated as
``app`` global module variable in the line 4.

In general, a model object can be obtained by:

* Creating a local instance of a model class inside a module with test steps (like in the example)
* Importing it from the module inside the tadek.models package if it was instantiated there

In the second approach, the :mod:`tadek.models.tomboy` module should look like
this:

.. code-block:: python
    :linenos:

    from tadek.models import Model
    
    
    # Model definition:
    class Tomboy(Model):
        root = App("tomboy --search",
                   searcher("AT-SPI"),
                   structure(role="APPLICATION",
                             searchers=(frame("Search All Notes"),)))
        # ...
    
    # Global model instance:
    app = tomboy()

Then, the same instance of the model can be imported wherever it is needed:

.. code-block:: python
    :linenos:

    from tadek.engine.testdefs import testCase
    from tadek.models.tomboy import app


    @testCase()
    def openPreferences(test, device):
        test.fail(app.launch(device), "Tomboy did not open")
        # ...


Test Steps
==========

Test cases in TADEK are built of steps. This approach has been taken for
following reasons:

* Reusability -- One test step can be used in many test cases or even be shared across multiple projects.
* Maintainability -- If some behavior of a tested application changes, it is easy to adjust many test cases by updating only one test step.
* Scalability -- After some test cases are prepared it is very likely that adding a next one will only require implementing one test step.

The following example shows how to implement a test step:

.. code-block:: python
    :linenos:

    from tadek.models.tomboy import app
    from tadek.engine.testdefs import testStep

    @testStep(description="Clicks on File/New and sets text of a new note")
    def stepAddNewNote(test, device, text=None):
        test.fail(app.search.menu.File.New.click(device),
                  "Failed to click File/New")
        i = 0
        first = None
        for note in app.notes.childIter(device):
            i += 1
            first = note
        if text is None:
            return
        note.text.type(device, text)
        newText = note.text.getText(device)
        test.fail(newText==text, "Text of not is '%s' while should be '%s'"
                  % (newText, text))

First, an instance of *tomboy* model is imported. Test step *stepAddNewNote*
is defined as a function decorated with the
:epylink:`tadek.engine.testdefs.testStep` decorator (line 4). Interaction with
the application is done by calling methods on widgets of the model (lines 6,
10, 15, 16). The results of the interaction are checked against expected values
through assertion methods of the ``test`` parameter (lines 6, 17).

More on the signature of a test step function:

* Test step function can carry additional information that is provided through keyword arguments of the :epylink:`~tadek.engine.testdefs.testStep` decorator, e.g. ``description`` with a short description of the test case (line 4)
* The first two positional arguments must be ``test`` and ``device`` (line 5). Their values are supplied by TADEK's engine while the step is being executed. The ``test`` argument provides context of the test case upon which the step is performed which include assertion methods like :epylink:`~tadek.engine.testexec.TestExec.fail` or :epylink:`~tadek.engine.testexec.TestExec.failThis`. The ``device`` argument is an object that provides a device context that is required as the first argument of methods of widgets or a model itself.
* Keyword arguments can be provided to parameterize the test step. They must be supplied with default values, even if they are empty (line 5).

.. tip::
    It is convenient to follow a convention of prepending *step* to test step
    names


Test steps can be saved along with test cases -- under *testcases* or
*testsuites* directory where they can be used locally. An alternative place
for test steps is the *teststeps* directory which is a better solution when
test steps are intended to be easily reused by testcases defined in various
places inside a location or even by test cases from another locations.

Test Cases
==========

As shown in at the beginning of the chapter, a simple one-step test case can be
defined using :epylink:`tadek.engine.testdefs.testCase` decorator. The next
example demonstrates how to prepare a test case of multiple steps by using
:epylink:`tadek.engine.testdefs.TestCase` class:

.. code-block:: python
    :linenos:

    from tadek.engine.testdefs import TestCase
    from tadek.teststeps.gucharmap.basic import *

    caseEnterLetters = TestCase(
        stepRunCharacterMap(),
        stepLatin(),
        stepEnterCharacters(chars="Azfla"),
        description="Activate a sequence of letters and compare to the text field")

The general procedure is to:

#. Import the :epylink:`tadek.engine.testdefs.TestCase` class (line 1).
#. Define or import test steps that the test case will be composed of. The latter is done in the example (line 2).
#. Create an instance of :epylink:`~tadek.engine.testdefs.TestCase` class:

   * The instance can be created either as an attribute of a module, like in the example, or directly as an attribute of a test suite class.
   * Calls of test step functions should be provided to the initializer in desired order (lines 5-7). Step parameters can be given as keyword arguments (line 7).
   * Optionally some additional information can be attached to the test case. It can be performed by providing keyword arguments to the initializer, e.g. a ``description`` string (line 8).

.. hint::
    It is convenient to follow a convention of prepending *case* to test case
    names

Test cases can be stored inside the *testsuites* directory along with test
suites they are included in. Alternatively test cases can be stored separately
inside the *testcases* directory from where they are easy to import in any
module with test suites.

Test Suites
===========

Composing test suites is the last stage of test case development in TADEK.
After test cases are prepared, they have to be grouped into suites, since only
these are loadable by TADEK's engine. Of course it is possible to execute only
selected test cases from a suite (more information on running test cases can
be found in the :ref:`running` chapter).

Test suites are subclasses of :epylink:`tadek.engine.testdefs.TestSuite` class.
To prepare a test suite:

#. Import the :epylink:`tadek.engine.testdefs.TestSuite` class.
#. Import test case objects that the test suite will be composed of.
#. Create a subclass of :epylink:`~tadek.engine.testdefs.TestSuite` class.
#. Assign imported test case objects as attributes of the class.
#. Optionally define test fixture methods:

   * ``setupCase()`` and ``tearDownCase()``
   * ``setupSuite()`` and ``tearDownSuite()``

#. Optionally add some additional information to a test suite by setting class attributes, e.g. a ``description`` string.

An example of a module with a test suite definition:

.. code-block:: python

    from tadek.engine.testdefs import TestSuite
    from tadek.testcases.gedit import *

    class SimpleTestSuite(TestSuite):
        description = "Simple suite of tests for gedit application"
        
        caseOpenFile = caseOpenFile
        caseSaveFile = caseSaveFile
        caseCopyPaste = testCopyPaste

.. hint::
    It is possible to create test case objects in-line instead of importing
    them. The following example shows a test suite with in-line test cases:
    
    * By creating an instance of :epylink:`tadek.engine.testdefs.TestCase` class -- lines 20-23
    * By defining a function decorated with the :epylink:`tadek.engine.testdefs.testCase` decorator -- lines 12-18

    .. code-block:: python
        :linenos:

        from tadek.engine.testdefs import TestCase, TestSuite
        from tadek.models.gcalctool import Calculator
        from tadek.teststeps.gcalctool.common import *
        from tadek.teststeps.gcalctool.calculation import *
        from tadek.testcases.gcalctool.views import *

        app = Calculator()

        class GeneralSuite(TestSuite):
            description = "Test functionality of the calculator application"

            @testCase(description="Run and then close the calculator application")
            def caseRunClose(test, device):
                app.launch(device)
                test.fail(app.isOpen(device), "Calculator does not run")
                test.fail(app.menu.Calculator.Quit.click(device),
                          "Could not close the calculator application")
                test.fail(app.isClosed(device), "Calculator does not close")        

            caseClearDisplay = TestCase(stepRunCalculator(),
                                        stepClickButton(button="5"),
                                        stepClearDisplay(),
                            description="Clear the calculator display after running")

            caseBasicCalculations = BasicView()
            caseAdvancedCalculations = AdvancedView()
            caseFinancialCalculations = FinancialView()
            caseScientificCalculations = ScientificView()
            caseProgrammingCalculations = ProgrammingView()


Defining Fixture Methods
------------------------

Fixture methods are special methods that are called before or after execution
of a test suite or single test cases of a test suite. There are four such
methods: 

* ``setUpSuite()`` -- for a method that will be called once before any test case of a suite starts to execute
* ``tearDownSuite()`` -- for a method that will be called once after all test cases finished execution, even when the execution is aborted
* ``setUpCase()`` -- for a method that will be called before the execution of each test case of the suite, including test cases of child suites
* ``tearDownCase()`` -- for a method that will be called after the execution of each test case, even when the execution is aborted, including test cases of child suites

Failure of an assertion causes:

* In ``setUpSuite()`` -- the test suite won't be executed and the status of the suite is set to ``FAILED``
* In ``tearDownSuite()`` -- the status of the suite is set to ``FAILED``
* In ``setUpCase()`` -- test case won't be executed, its status is set to ``FAILED``, it does not affect the execution of other test cases in the suite
* In ``tearDownSuite()`` -- the status of the test case is set to ``FAILED``, it does not affect the execution of other test cases in the suite

Similarly to test step functions, fixture methods must have ``test`` and
``device`` positional parameters. Following example shows how to use
``setUpSuite()``, ``setUpCase()`` and ``tearDownCase()`` methods to arrange
running and closing a tested application.

.. code-block:: python
    :linenos:

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

        # test case definitions ...

In ``setUpSuite()`` method, all running instances of tested application are
killed before first test case begins to execute to make sure they won't affect
the tests. A new instance of the application is started for each test case in
``setUpCase()`` method. Persistent settings are removed before running, to
reset the application state remembered from the last run. In ``tearDownCase()``
method after each test case ends, the application is closed by selecting
:menuselection:`File --> Quit` from the menu or eventually killed in case the
closing attempt fails for some reason.

Creating Hierarchy
------------------

Apart form test cases a test suite can contain another test suites. Suppose
some test suites are defined in a module inside the *testcases* directory
of *gcalctool* location:

.. code-block:: python
    :linenos:

    from tadek.engine.testdefs import TestCase, TestSuite
    from tadek.teststeps.gcalctool.common import *
    from tadek.testcases.gcalctool.calculations import *


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

    class AdvancedView(TestSuite):
        description = "The advanced view test cases"
        
        # ...


    class ScientificView(TestSuite):
        description = "The scientific view test cases"
        
        # ...

A test suite for each view of the *gcalctool* application contains test cases that
perform some basic mathematical operations. All these three suites can be
enclosed in one suite the same way as with test cases:

.. code-block:: python
    :linenos:

    class CalculationsSuite(TestSuite):
        description = "Test basic calculation functionality of the calculator application"

        caseBasic = BasicView()
        caseAdvanced = AdvancedView()
        caseScientific = ScientificView()

A suite can also be included partially, i.e. only with selected test cases:

.. code-block:: python
    :linenos:

    class AdditionSuite(TestSuite):
        description = "Test addition functionality of the calculator application"

        caseBasic = BasicView("caseAddition")
        caseAdvanced = AdvancedView("caseAddition")
        caseScientific = ScientificView("caseAddition")

When an inner suite is executed, the order of fixture method calls is as
follows:

* ``setUpSuite()`` of outer suite
* ``setUpSuite()`` of inner suite
* ``setUpCase()`` of outer suite
* ``setUpCase()`` of inner suite
* ``tearDownCase()`` of inner suite
* ``tearDownCase()`` of outer suite
* ``tearDownSuite()`` of inner suite
* ``tearDownSuite()`` of outer suite

Test Context
============

The ``test`` argument of a test step function provides a test context. It
includes assertions and a storage for common variables.

Assertions
----------

A test context object provides assertions -- various methods that determine
whether a test step will fail, succeed or end up with an error. When none of
the assertions used inside a test step fails, the test step will be considered
``PASSED``.

**Examples**

If :epylink:`~tadek.engine.widgets.MenuItem.click` method returns ``False``,
then execution of test step, as well as test case which it is a part of will
stop with ``FAILED`` result::

    test.fail(app.search.menu.File.New.click(device), "Failed to click File/New")

If :epylink:`~tadek.engine.widgets.App.isOpen` method returns ``False``, then
the execution of test step will stop with ``FAILED`` result and the remaining
test steps of the test case it is a part of will continue to run::

    test.failThis(app.isOpen(device), "Application is not open")

If the length of a string returned from
:epylink:`~tadek.engine.widgets.Widget.getText` is greater than ``20``, then
the execution of test step will stop with ``FAILED`` result and the
remaining test steps of the test case it is a part of will continue to run::

    test.failThisIf(len(app.search.input.text.getText(device)) > 20,
                    "Text is too long")

.. note:: 

	``failThis()`` and ``failThisIf()`` assertions used inside fixture methods
	have the same effect as ``fail()`` assertion.

Shared Data
-----------

Apart form assertion methods, a context object can serve also as a dictionary
common to all steps and fixture methods within a test case. It is particularly
convenient when one step depends on data produced by another step. The
following example shows how a variable can be shared between multiple steps in
a test case of Tomboy Notes application:

.. code-block:: python
    :linenos:

    import random
    from tadek.engine.testdefs import testStep, TestCase, TestSuite
    from tadek.teststeps.tomboy.basic import stepRestartTomboy, stepAddNewNote
    from tadek.models.tomboy import Tomboy


    app = Tomboy()


    @testStep(description="Adds a random number of notes")
    def stepAddRandomNotes(test, device):
        noteCount = random.randint(2, 10)
        test['noteCount'] = noteCount
        for i in range(1, noteCount+1):
            stepAddNewNote.run(test, device)

    @testStep(description="Check number of items on note list")
    def stepCheckRandomNotesOnList(test, device):
        noteCount = test['noteCount']
        count = 0
        for item in app.search.noteList.childIter(device):
            count += 1
        test.fail(count == noteCount,
                  "There are %d items on list while should be %d" % (count, noteCount))

    @testStep(description="Check number of notes shown on status bar")
    def stepCheckRandomNotesOnStatusBar(test, device):
        expectedText = "Total: %d notes" % test['noteCount']
        text = app.search.status.getText(device)
        test.fail(text == expectedText,
                  "Status bar text is: '%s' while should be: '%s'" % (text, expectedText))
        

    class ExampleSuite(TestSuite):
        
        def setUpCase(self, test, device):
            test.fail(app.kill(device),
                      "Failed to kill previous instance of Tomboy application")
            app.removeSettings(device)
            test.fail(app.launch(device),
                      "Failed to launch Tomboy Application")
        
        caseAddRandomNumberOfNotes = TestCase(
            stepAddRandomNotes(),
            stepCheckRandomNotesOnList(),
            stepCheckRandomNotesOnStatusBar(),
            description="Adds a random number of notes")

In the example, the ``stepAddRandomNotes()`` step adds a random
number of new notes and saves that number under ``noteCount`` key in the test
context (line 13). Following ``stepCheckRandomNotesOnList()`` and
``stepCheckRandomNotesOnStatusBar()`` steps confront the number of items on
note list and the number shown in the status bar with value of ``noteCount``.

Except of the key-value pairs set manually, one special value is kept under
the ``result`` key of the context dictionary -- a return value of previously
executed test step function. Using it is suitable mainly in situations where
data have to be passed only from one step to a subsequent step.

.. note::

    As shown in the ``stepAddRandomNotes()`` step, it is possible to build a
    complex test step by embedding another steps inside. An inner test step
    is executed not by calling it directly, but by invoking the special
    ``run()`` method on it. Apart from step arguments, the ``test`` and the
    ``device`` objects have to be passed to the call (line 15).

Test context object is inherited through the hierarchy of test suites. As a
consequence, key-value pairs set in ``setUpSuite()`` method of outer suite
are visible not only in its test cases, but also in test cases of inner suites.

Interaction with Device
=======================

The ``device`` argument of a test step is an object that provides a device
context that is required for executing methods of widgets of a model or methods
of a model itself and should be provided as their first argument. Most of the
:epylink:`~tadek.engine.widgets.Widget` methods give feedback on status of their
execution as a return value.

**Examples**

Opening an application on a device::

    app.launch(device)

Pressing the *Backspace* button on a device::

    app.keyBackspace(device)

Creating file: *"/tmp/test.txt"* with content: ``'test 123'`` on a device::

    app.sendFile(device, "/tmp/test.txt", "test 123")

Executing the ``killall gcalctool`` command on a device and assigning the
return code, *stdout* and *stderr* to local variables::

    ret, out, err = app.systemCommand(device, "killall gcalctool")

Checking whether an input is focused or not and assigning a returned boolean to
a local variable::

    focused = app.search.input.text.isFocused(device)

Often a test step requires to wait for the application to accomplish some
initiated actions before further actions can be taken, e.g. to wait for a
dialog to open after a menu item is clicked. To address this issue, most of 
:epylink:`~tadek.engine.widgets.Widget` methods try several times to accomplish
their task, before returning a result.

Sometimes there is a need to invert the operation of a
:epylink:`~tadek.engine.widgets.Widget` method, e.g. to wait for a widget to
disappear with a use of :epylink:`~tadek.engine.widgets.Widget.isExisting`
method. It can be achieved by providing ``True`` value of ``expectedFailure``
argument. If the widget disappears, even after a while the result will be
``False`` as expected. Otherwise, the ``True`` result indicates that the widget
still exists while it shouldn't.

**Example**

First, the Close button of the Preferences dialog is clicked, then the
:epylink:`~tadek.engine.widgets.Widget.isExisting` method waits for the dialog
to disappear. The assertion succeeds when the return value is ``False``::

    app.preferences.Close(device)
    test.failIf(app.preferences.isExisting(device, expectedFailure=True),
                "The Preferences window did not close")

The way how the task is done in the example, though explanatory, have a
simpler alternative -- the :epylink:`tadek.engine.widgets.Dialog.isClosed`
method, which is designed to wait for the dialog widget to disappear
without the need to provide the additional parameter.
