#!/usr/bin/python3
#
# tzxtools - a collection for processing tzx files
#
# Copyright (C) 2016 Richard "Shred" Körber
#   https://github.com/shred/tzxtools
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import sys
import textwrap

from tzxlib.tapfile import TapHeader
from tzxlib.tzxfile import TzxFile


def tap_type(tap):
    type = 'Screen' if (tap.param1() == 0x4000 and tap.length() == 6912) else tap.type()
    return type


def ls_file(f):
    global info
    tzx = TzxFile()
    try:
        tzx.read(f)
    except:
        print("ERROR reading file as ZX Spectrum tape")
        return
    cnt = 0
    for b in tzx.blocks:
        if not args.long:  # Headers only
            if hasattr(b, 'tap') and isinstance(b.tap, TapHeader):
                # TAP header

                # TODO: FUDGE: should be in block class
                type = tap_type(b.tap)

                print(f"{type}: {b.tap.name()}")
        else:  # longer listing (think 'ls -l')
            if hasattr(b, 'tap') and isinstance(b.tap, TapHeader):
                print(f"{str(b):46s} {len(b.dump()):5d} ({b.type})")
            else:
                # print('%3d  %-27s %s' % (cnt, b.type, str(b)))
                print(f"{' ':46s} {len(b.dump()):5d} ({b.type})")
        if args.verbose:
            info = b.info()
            if info is not None:
                print(textwrap.indent(info.strip(), '\t'))
        cnt += 1


parser = argparse.ArgumentParser(description='List the contents of a TZX file')
parser.add_argument('file',
            nargs=argparse.REMAINDER,
            type=argparse.FileType('rb'),
            help='TZX files, stdin if omitted')
parser.add_argument('-l', '--long',
            dest='long',
            action='store_true',
            help='longer(er) listing - include all blocks, more details')
parser.add_argument('-v', '--verbose',
            dest='verbose',
            action='store_true',
            help='show content of information blocks')
args = parser.parse_args()

files = list(args.file)
if not sys.stdin.isatty() and len(files) == 0:
    files.append(sys.stdin.buffer)

if len(files) == 0:
    parser.print_help(sys.stderr)
    sys.exit(1)

for f in files:
    if len(files) > 1:
        name = f.name if hasattr(f, 'name') else f
        print('\n%s:' % (name))
    ls_file(f)
