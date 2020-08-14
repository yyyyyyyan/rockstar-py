import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestPronouns(unittest.TestCase):
    def test_it_if(self):
        rock = ["Green is 0\n", "Build it up\n"]

        py = ["Green = 0\n", "Green += 1\n"]

        self.__run_block_test(rock, py)

    @unittest.skip("Pronouns are not working in calculations")
    def test_it_until(self):
        rock = ["The day is 0\n", "Until the day is 7\n", "Build it up\n"]

        py = ["the_day = 0\n", "while not the_day == 7:\n", "    the_day += 1\n"]

        self.__run_block_test(rock, py)

    def __run_block_test(self, rock, py):
        transpiler = Transpiler()
        transpiled = [transpiler.transpile_line(line) for line in rock]
        self.assertEqual(len(py), len(transpiled))
        for py_line, transpiled_line in zip(py, transpiled):
            self.assertEqual(py_line, transpiled_line)
