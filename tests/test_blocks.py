import os
import sys
import unittest

sys.path = [os.path.dirname(os.path.dirname(os.path.realpath(__file__)))] + sys.path
from rockstarpy.transpile import Transpiler


class TestBlocks(unittest.TestCase):
    def test_if_block(self):
        rock = ["If Tommy is nobody\n", 'Shout "Tommy?"\n', "\n", 'Shout "Tommy!"\n']

        py = ["if Tommy == False:\n", '    print("Tommy?")\n', "", 'print("Tommy!")\n']

        self.__run_block_test(rock, py)

    def test_if_else_block(self):
        rock = [
            "If Tommy is nobody\n",
            'Shout "Tommy?"\n',
            "Else\n",
            'Shout "Tommy!"\n',
            "\n",
            'Shout "Tommy!"\n',
        ]

        py = [
            "if Tommy == False:\n",
            '    print("Tommy?")\n',
            "else:\n",
            '    print("Tommy!")\n',
            "",
            'print("Tommy!")\n',
        ]

        self.__run_block_test(rock, py)

    def test_while_block(self):
        rock = [
            "While Tommy is not 0\n",
            "Knock Tommy down\n",
            "\n",
            'Shout "Tommy!"\n',
        ]

        py = ["while Tommy != 0:\n", "    Tommy -= 1\n", "", 'print("Tommy!")\n']

        self.__run_block_test(rock, py)

    def test_until_block(self):
        rock = ["Until Tommy is 0\n", "Knock Tommy down\n", "\n", 'Shout "Tommy!"\n']

        py = ["while not Tommy == 0:\n", "    Tommy -= 1\n", "", 'print("Tommy!")\n']

        self.__run_block_test(rock, py)

    def test_function_numeric(self):
        rock = [
            "Multiply takes Love and Life\n",
            "Give back Love of Life\n",
            "\n",
            "Say Multiply taking 3, 444\n",
        ]

        py = [
            "def Multiply(Love, Life):\n",
            "    return Love * Life\n",
            "",
            "print(Multiply(3, 444))\n",
        ]

        self.__run_block_test(rock, py)

    def test_function_variables(self):
        rock = [
            "Multiply takes Love and Life\n",
            "Give back Love of Life\n",
            "\n",
            "Put 1 into my heart\n",
            "Put 666 into the devil\n",
            "Multiply taking my heart, the devil\n",
        ]

        py = [
            "def Multiply(Love, Life):\n",
            "    return Love * Life\n",
            "",
            "my_heart = 1\n",
            "the_devil = 666\n",
            "Multiply(my_heart, the_devil)\n",
        ]

        self.__run_block_test(rock, py)

    def __run_block_test(self, rock, py):
        transpiler = Transpiler()
        transpiled = [transpiler.transpile_line(line) for line in rock]
        self.assertEqual(len(py), len(transpiled))
        for py_line, transpiled_line in zip(py, transpiled):
            self.assertEqual(py_line, transpiled_line)


if __name__ == "__main__":
    unittest.main()
