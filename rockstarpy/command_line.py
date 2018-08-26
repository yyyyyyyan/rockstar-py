import sys
import argparse

from rockstarpy.transpile import Transpiler


parser = argparse.ArgumentParser(description="Python transpiler for the esoteric language Rockstar")

input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument('--input', action='store', help='Input file (.rock)')
input_group.add_argument('--stdin', action='store_true', help='Stream in stdin')

output_group = parser.add_mutually_exclusive_group(required=True)
output_group.add_argument('--output', action='store', help='Output file (.py)', default='output.py')
output_group.add_argument('--stdout', action='store_true', help='Stream to stdout')

parser.add_argument('-v', action='version', help='Version', version='1.3.6')

args = parser.parse_args()


def command_line():

    # connnect input
    if args.stdin:
        lyrics = sys.stdin
    else:
        lyrics = open(args.input, 'r')

    # connect output
    if args.stdout:
        enc = False
        output = sys.stdout
    else:
        enc = True
        output = open(args.output, 'wb', 0)

    # Read, Convert, Write, loop
    transpiler = Transpiler()
    for line in lyrics:
        output.write( encode( transpiler.transpile_line(line), enc ) )

    # close input
    if not args.stdin:
        lyrics.close()

    # close output
    if not args.stdout:
        output.close()


def encode(line, enc):
    if enc:
        return line.encode()
    return line
