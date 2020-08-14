import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestConditionals(unittest.TestCase):
    def test_equals(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy is nobody\n")
        self.assertEqual(py_line, "if Tommy == False:\n")

    def test_greater(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy is stronger than Superman\n")
        self.assertEqual(py_line, "if Tommy > Superman:\n")

    def test_greater_equals(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Love is as high as mountain\n")
        self.assertEqual(py_line, "if Love >= mountain:\n")

    def test_less(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy is weaker than a worm\n")
        self.assertEqual(py_line, "if Tommy < a_worm:\n")

    def test_less_equals(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If my mind is as low as my soul\n")
        self.assertEqual(py_line, "if my_mind <= my_soul:\n")

    def test_while_equals(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("While Tommy is nobody\n")
        self.assertEqual(py_line, "while Tommy == False:\n")

    def test_until_greater(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Until Tommy is stronger than Superman\n")
        self.assertEqual(py_line, "while not Tommy > Superman:\n")

    def test_not(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If not number is 28\n")
        self.assertEqual(py_line, "if not number == 28:\n")

    def test_or(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy is nobody or Billy is nobody\n")
        self.assertEqual(py_line, "if Tommy == False or Billy == False:\n")

    def test_and(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy is nobody and Billy is nobody\n")
        self.assertEqual(py_line, "if Tommy == False and Billy == False:\n")

    @unittest.skip("apostrophe handling is not working fully")
    def test_aint(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy ain't nobody\n")
        self.assertEqual(py_line, "if Tommy != False:\n")

    @unittest.skip("nor operator not implemented, yet")
    def test_nor(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("If Tommy is nobody nor Billy is nobody\n")
        self.assertEqual(py_line, "if not Tommy == False or Billy == False:\n")


if __name__ == "__main__":

    unittest.main()
