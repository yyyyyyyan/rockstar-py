from rockstarpy.transpile import Transpiler
from io import BytesIO
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Python transpiler for the esoteric language Rockstar"
)

input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument("-i", "--input", action="store", help="Input file (.rock)")
input_group.add_argument(
    "--stdin",
    action="store_const",
    const=sys.stdin.buffer,
    help="Stream in stdin. Send EOF (Ctrl+D in *nix, Ctrl+Z in Windows) to stop",
)

output_group = parser.add_mutually_exclusive_group()
output_group.add_argument(
    "-o", "--output", action="store", help="Output file (.py)", default="output.py"
)
output_group.add_argument(
    "--stdout", action="store_const", const=sys.stdout.buffer, help="Stream to stdout"
)
output_group.add_argument(
    "--exec", action="store_true", help="Execute (without saving) the transpiled code "
)

parser.add_argument(
    "-v", "--version", action="version", help="Version", version="2.1.0"
)

args = parser.parse_args()

def command_line():
    sys.tracebacklimit = 0
    lyrics = args.stdin or open(args.input, "rb")
    output = BytesIO() if args.exec else args.stdout or open(args.output, "wb")

    transpiler = Transpiler()
    line_number = 1
    for line in lyrics:
        line = line.decode("utf8")
        try:
            output.write(transpiler.transpile_line(line).encode("utf8"))
        except SyntaxError as err:
            raise SyntaxError(err.msg + f":\n{line_number}.\t{line}")
        line_number += 1

    if args.exec:
        exec(output.getvalue())
    if args.stdin is None:
        lyrics.close()
    if args.stdout is None:
        output.close()
