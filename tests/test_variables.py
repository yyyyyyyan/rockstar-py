import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestVariables(unittest.TestCase):
    def test_simple_variables(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("X is 2\n")
        self.assertEqual(py_line, "X = 2\n")

        py_line = transpiler.transpile_line("Tommy is a rockstar\n")
        self.assertEqual(py_line, "Tommy = 18\n")

    def test_common_variables(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("My variable is 5\n")
        self.assertEqual(py_line, "my_variable = 5\n")

        py_line = transpiler.transpile_line("Shout the total\n")
        self.assertEqual(py_line, "print(the_total)\n")

    def test_proper_variables(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Master Of The Universe is nothing\n")
        self.assertEqual(py_line, "Master_Of_The_Universe = False\n")


if __name__ == "__main__":
    unittest.main()
