import os
import sys
import difflib

path = os.path.dirname(os.path.realpath(__file__))
path = '/'.join(path.split('/')[:-1])
sys.path = [path] + sys.path
from rockstarpy import convert_code


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

        rockstar_code = ""
        with open(rock_file, 'r') as rockstar_file:
            rockstar_code = rockstar_file.readlines()

        converted_code = ''.join(convert_code(rockstar_code))
        with open(file_name +".py", 'r') as expected:
            expected_code = expected.read()
            check_files_identical(expected_code, converted_code)

if __name__ == '__main__':
    main()