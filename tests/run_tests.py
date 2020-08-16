from pathlib import Path
import sys
import difflib
import unittest

test_path = Path(__file__).resolve().parent
sys.path.insert(0, str(test_path.parent))
from rockstarpy.transpile import Transpiler


def check_files_identical(expected, actual):
    diff = difflib.unified_diff(expected, actual, fromfile="expected", tofile="actual",)
    line = None
    for line in diff:
        print(line, end="")
    if line is not None:
        print()
        assert False, "There are differences"

def main():
    identical_test_files = [
        (file, file.with_suffix(".py"))
        for file in test_path.iterdir()
        if file.suffix == ".rock"
    ]
    for rock_path, py_path in identical_test_files:
        print("testing", rock_path.name)

        assert py_path.is_file(), f"{py_path} does not exist"

        transpiler = Transpiler()
        converted_code = ""
        with rock_path.open() as rockstar_file:
            for line in rockstar_file:
                converted_code += transpiler.transpile_line(line)

        with py_path.open() as expected_file:
            expected_code = expected_file.read()

        check_files_identical(expected_code, converted_code)

    suite = unittest.defaultTestLoader.discover(test_path, pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
