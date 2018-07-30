import argparse
import rockstarpy as rockstar

parser = argparse.ArgumentParser(description="Python transpiler for the esoteric language Rockstar")
parser.add_argument('input', action='store', help='Input file (.rock)')
parser.add_argument('--output', action='store', help='Output file (.py)', default='output.py')
parser.add_argument('-v', action='version', help='Version', version='1.3.4')

def command_line():
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as rockstar_file:
            rockstar_code = rockstar_file.readlines()
    except FileNotFoundError:
        print('File not found.')
    else:
        with open(args.output, 'w') as py_rockstar:
            rockstar.convert_code(rockstar_code, py_rockstar)