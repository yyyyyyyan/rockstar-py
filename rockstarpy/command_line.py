import argparse
import rockstarpy as rockstar

parser = argparse.ArgumentParser(description="Python transpiler for the esoteric language Rockstar")
parser.add_argument('input', action='store', help='Input file (.rock)')
output_group = parser.add_mutually_exclusive_group()
output_group.add_argument('--output', action='store', help='Output file (.py)', default='output.py')
output_group.add_argument('--stream', action='store_true', help='Print output to stdout')
parser.add_argument('-v', action='version', help='Version', 
version='1.3.6')

def command_line():
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as rockstar_file:
            rockstar_code = rockstar_file.readlines()
    except FileNotFoundError:
        print('File not found.')
    else:
        if args.stream:
            stream(rockstar_code)
        else:
            write(rockstar_code, args.output)

def stream(rockstar_code):
    for line in rockstar.convert_code(rockstar_code):
        print(line,end="")

def write(rockstar_code, output):
    with open(output, 'w') as py_rockstar:
        for line in rockstar.convert_code(rockstar_code):
            py_rockstar.write(line)
