import sys
import argparse

from rockstarpy import convert


parser = argparse.ArgumentParser(description="Python transpiler for the esoteric language Rockstar")

parser.add_argument('input', action='store', help='Input file (.rock)')
parser.add_argument('-v', action='version', help='Version', version='1.3.6')

output_group = parser.add_mutually_exclusive_group()
output_group.add_argument('--output', action='store', help='Output file (.py)', default='output.py')
output_group.add_argument('--stream', action='store_true', help='Print output to stdout')

args = parser.parse_args()


def command_line():

    # connnect input
    lyrics = open(args.input, 'r')

    # connect output
    if args.stream:
        output = sys.stdout
    else:
        output = open(args.output, 'w')

    # Read, Convert, Write, loop
    for line in lyrics:
        output.write( convert.convert_line(line) )

    # close input
    lyrics.close()

    # close output
    if not args.stream:
        output.close()
