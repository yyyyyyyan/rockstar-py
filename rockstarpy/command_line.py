import argparse
from . import rockstar

parser = argparse.ArgumentParser(description="Python transpiler for the esoteric language Rockstar")
parser.add_argument('input', action='store', help='Input file (.rock|.rockstar|.lyrics)')
parser.add_argument('--output', action='store', help='Output file (.py)')

def main():
	args = parser.parse_args()

	try:
	    rockstar_file = open(args.input, 'r')
	    rockstar_code = rockstar_file.readlines()
	    rockstar_file.close()
	except FileNotFoundError:
	    print('File not found.')

	output_file = args.output if args.output else 'output.py'
	py_rockstar = open(output_file, 'w')
	rockstar.convert_code(rockstar_code, py_rockstar)
	py_rockstar.close()
