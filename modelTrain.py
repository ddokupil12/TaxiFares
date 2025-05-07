import sys
from argparse import ArgumentParser

print(sys.argv)
# epoch (1, 20)
# Layer density (list of integers)
# Test size (0, 1)

parser = ArgumentParser()
parser.add_argument("-e", help="number of epochs")
parser.add_argument("-t", help="Test size (int between 0 and 1 exclusive)")
parser.add_argument("-h1", help="Defaults to len(df.columns)")
parser.add_argument("-h2", help="Defaults to 128")
parser.add_argument("-h3", help="Defaults to 72")
parser.add_argument("-h4", help="Defaults to 16")

args = parser.parse_args()

if args.e:
    print("e")

if args.t:
    print('t')

if args.h1:
    print("h1")

if args.h2:
    print("h2")

if args.h3:
    print("h3")

if args.h4:
    print("h4")
