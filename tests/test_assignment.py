import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestAssignment(unittest.TestCase):
    def test_is_bool(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Life is ok\n")
        self.assertEqual(py_line, "Life = True\n")

    def test_is_poetic(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("My life is a mess\n")
        self.assertEqual(py_line, "my_life = 14\n")

        py_line = transpiler.transpile_line("Life is a one day after another\n")
        self.assertEqual(py_line, "Life = 13357\n")

    def test_is_numeric(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Seven is 11\n")
        self.assertEqual(py_line, "Seven = 11\n")

    def test_is_numeric_with_dot(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("X is 1.23\n")
        self.assertEqual(py_line, "X = 1.23\n")

    def test_is_poetic_with_dot(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line(
            "My dreams were ice. A life unfulfilled; wakin' everybody up, taking booze and pills\n"
        )
        self.assertEqual(py_line, "my_dreams = 3.1415926535\n")

    def test_is_poetic_with_hyphen(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Greed is all-consuming\n")
        self.assertEqual(py_line, "Greed = 3\n")

        py_line = transpiler.transpile_line("God is power-hungry\n")
        self.assertEqual(py_line, "God = 2\n")

    def test_is_poetic_and_numeric(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Car is 4 W D\n")
        self.assertEqual(py_line, "Car = 411\n")

    @unittest.skip("keywords are replaced too early in assignments")
    def test_is_poetic_keyword(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Tommy was without\n")
        self.assertEqual(py_line, "Tommy = 7\n")

    def test_is_string(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line('Message is "Hello"\n')
        self.assertEqual(py_line, 'Message = "Hello"\n')

    def test_let_be_bool(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Let my beer be empty\n")
        self.assertEqual(py_line, "my_beer = False\n")

    def test_let_be_poetic(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Let Stuart be a yellow Minion\n")
        self.assertEqual(py_line, "Stuart = 166\n")

    def test_let_be_numeric(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Let One be 0\n")
        self.assertEqual(py_line, "One = 0\n")

    def test_let_be_string(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line('Let the letter be "R"\n')
        self.assertEqual(py_line, 'the_letter = "R"\n')

    def test_put_into_bool(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put nothing into my hand\n")
        self.assertEqual(py_line, "my_hand = False\n")

    def test_put_into_poetic_assigns_variable(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put a flower into the vase\n")
        self.assertEqual(py_line, "the_vase = a_flower\n")

    def test_put_into_numeric(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line("Put 3.14 into PI\n")
        self.assertEqual(py_line, "Pi = 3.14\n")

    def test_put_into_string(self):
        transpiler = Transpiler()
        py_line = transpiler.transpile_line('Put "letter" into the envelope\n')
        self.assertEqual(py_line, 'the_envelope = "letter"\n')


if __name__ == "__main__":
    unittest.main()
