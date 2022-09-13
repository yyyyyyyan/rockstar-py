import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestList(unittest.TestCase):

    def test_list(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Shatter a string into a list\n")
        self.assertEqual(py_line, "a_list = list(a_string)\n")
    
    def test_pop(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Roll a list into variable\n")
        self.assertEqual(py_line, "variable = a_list.pop(0)\n")

if __name__ == "__main__":
    unittest.main()
