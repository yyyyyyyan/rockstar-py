import os
from rockstarpy.rockstar import convert_code
import difflib
from pprint import pprint
try:
    from StringIO import StringIO # python 2
except:
    from io import StringIO  # python 3


def check_files_identical(expected, actual):
    diff = difflib.unified_diff(
                expected,
                actual,
                fromfile='expected',
                tofile='actual',
    )
    diff = list(diff)
    if len(diff):
        for d in diff:
            print(diff)
        assert False, "There are differences"

def main():
    files = os.listdir('.')
    rock_files = filter(lambda f: '.rock' == f[-5:], files)
    py_files = set(filter(lambda f: '.py' == f[-3:], files))
    for rock_file in rock_files:
        file_name = rock_file[:-5]
        py_file = file_name + ".py"
        assert py_file in py_files, "Did not create a corrosponding expected output for " + file_name + ".rock"
    
        converted_code = StringIO() # open(file_name +".actual.py", 'w')
        rockstar_code = ""
        with open(rock_file, 'r') as rockstar_file:
            rockstar_code = rockstar_file.readlines()
        
        convert_code(rockstar_code, converted_code )
        with open(file_name +".py", 'r') as expected:
            check_files_identical(expected.read(), converted_code.getvalue())
        converted_code.close()

if __name__ == '__main__':
    main()


