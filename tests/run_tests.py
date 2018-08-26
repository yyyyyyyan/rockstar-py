import os
import sys
import difflib

sys.path=[os.path.dirname(os.path.dirname(os.path.realpath(__file__)))]+sys.path
from rockstarpy.transpile import Transpiler


def check_files_identical(expected, actual):
    diff = difflib.unified_diff(
        expected,
        actual,
        fromfile='expected',
        tofile='actual',
    )
    line = None
    for line in diff:
        print(line, end='')
    if line is not None:
        print()
        assert False, "There are differences"


def main():
    files = os.listdir('.')
    rock_files = filter(lambda f: f.split(".")[-1] in ['rock','rockstar','lyrics'] , files)
    py_files = set(filter(lambda f: f.endswith('.py'), files))
    for rock_file in rock_files:
        print("testing", rock_file)
        file_name = os.path.splitext(rock_file)[0]  # take off extension
        py_file = file_name + ".py"
        assert py_file in py_files, "Did not create a corrosponding expected output for " + rock_file

        transpiler = Transpiler()

        converted_code = ''
        with open(rock_file, 'r') as rockstar_file:
            for line in rockstar_file:
                converted_code += transpiler.transpile_line(line)

        with open(file_name +".py", 'r') as expected:
            expected_code = expected.read()

        check_files_identical(expected_code, converted_code)


if __name__ == '__main__':
    main()
