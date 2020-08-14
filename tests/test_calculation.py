import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestCalculation(unittest.TestCase):
    def test_add_numbers(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put 1 plus 3 into my pocket\n")
        self.assertEqual(py_line, "my_pocket = 1 + 3\n")

    def test_add_poetic(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put this with that into my pocket\n")
        self.assertEqual(py_line, "my_pocket = this + that\n")

    def test_subtract_numbers(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put 1 minus 3 into my pocket\n")
        self.assertEqual(py_line, "my_pocket = 1 - 3\n")

    def test_subtract_poetic(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put this without that into my pocket\n")
        self.assertEqual(py_line, "my_pocket = this - that\n")

    def test_multiply_numbers(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put 1 times 3 into my pocket\n")
        self.assertEqual(py_line, "my_pocket = 1 * 3\n")

    def test_multiply_poetic(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put this of that into my pocket\n")
        self.assertEqual(py_line, "my_pocket = this * that\n")

    def test_divide_numbers(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put 1 over 3 into my pocket\n")
        self.assertEqual(py_line, "my_pocket = 1 / 3\n")

    def test_divide_poetic(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put this over that into my pocket\n")
        self.assertEqual(py_line, "my_pocket = this / that\n")

    def test_decrement(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Knock the hate down\n")
        self.assertEqual(py_line, "the_hate -= 1\n")

    def test_increment(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Build my money up\n")
        self.assertEqual(py_line, "my_money += 1\n")

    @unittest.skip("Compound assignment not implemented, yet")
    def test_compund_addition_assignment(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Let X be with 10\n")
        self.assertEqual(py_line, "X += 10\n")


if __name__ == "__main__":
    unittest.main()
