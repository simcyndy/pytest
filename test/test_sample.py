# -*- coding: utf-8 -*-
"""
Execute in quiet mode : pytest -q [name_of_file].py
pytest --version # shows where pytest was imported from
pytest --fixtures # show available builtin function arguments
pytest -h | --help # show help on command line and config file option
pytest -x # stop after first failure
pytest --maxfail=2 # stop after two failures
Run tests by keyword expressions - pytest -k "MyClass and not method"
Run tests by node ids : Each collected test is assigned a unique nodeid which consist of the module filename followed by
specifiers like class names, function names and parameters from parametrization, separated by :: characters. i.e
pytest test/test_sample.py::test_sample

pytest --showlocals # show local variables in tracebacks
pytest -l # show local variables (shortcut)
pytest --tb=auto # (default) 'long' tracebacks for the first and last
# entry, but 'short' style for the other entries
pytest --tb=long # exhaustive, informative traceback formatting
pytest --tb=short # shorter traceback format
pytest --tb=line # only one line per failure
pytest --tb=native # Python standard library formatting
pytest --tb=no # no traceback at all

pytest --full-trace causes very long traces to be printed on error (longer than --tb=long). It also ensures that
a stack trace is printed on KeyboardInterrupt (Ctrl+C).

pytest -ra => short test summary info, a => (all except passes)
The -r options accepts a number of characters after it, with a used above meaning “all except passes”.
Here is the full list of available characters that can be used:
• f - failed
• E - error
• s - skipped
• x - xfailed
• X - xpassed

pytest -x --pdb # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3 # drop to PDB for first three failures

pytest --trace => This will invoke the Python debugger at the start of every test.

pytest --junitxml=path => create result files which can be read by Jenkins or other Continuous integration servers

pytest --pastebin=all - Send information to an online paste service
pytest -p pytest_cov => Load plugins early before test starts

"""

import pytest


def func(x):
	return x + 1


def test_sample():
	assert func(3) == 4


def f():
	raise SystemExit(1)


def test_mytest():
	with pytest.raises(SystemExit):
		f()


# Grouping Tests into Classes
class TestClass(object):
	def test_one(self):
		x = "this"
		assert 'h' in x


# def test_two(self):
# 	x = "hello"
# 	assert hasattr(x, "check") # will not pass


class Person:
	age = 334
	gender = "Female"
	name = "Jane Doe"


person = Person()


def test_person():
	assert hasattr(person, 'age')


###########################################

def test_needsfiles(tmpdir):
	print tmpdir


# assert 0


###########################################
@pytest.fixture
def error_fixture():
	assert 0


def test_ok():
	print("ok")


# def test_fail():
# 	assert 0


# def test_error(error_fixture):
# 	pass


def test_skip():
	pytest.skip("Skipping the test")


def test_xfail():
	pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason = "Always Fail")
def test_xpass():
	pass
