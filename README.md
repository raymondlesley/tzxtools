# tzxtools

This is a collection of command line tools for processing TZX files.
Forked from https://github.com/benitoss/tzxtools.git
(forked from https://github.com/shred/tzxtools.git).

Main changes TODO:
* Convert to Linux/Python command-line scripts
* Refactor to avoid dependencies
* Refactor to support streaming
* Add TAP to TZX conversion

## Features

TZX is a common file format for preserving computer tapes of the ZX Spectrum, but also Amstrad CPC, C64 and MSX. `tzxtools` mainly supports ZX Spectrum TZX files, but raw file operations can be applied on any TZX file. It also supports TSX files, which are mainly used for MSX.

* Convert your old ZX Spectrum tape recordings into TZX files.
* List, split, merge, and divide the blocks inside TZX files.
* Play back TZX files and load them into the real hardware.
* Extract binary content from TZX blocks.
* Read hex dumps, disassembled Z80 machine code, or ZX Spectrum BASIC code.
* Convert ZX Spectrum screens to PNG files.
* Generate TAP files for ZX Spectrum Next and some emulators.
* Disassembler also supports all undocumented Z80 instructions and Z80N (ZX Spectrum Next) instructions.
* Also supports TSX Kansas City Standard blocks.
* All tools can also read TAP files.

## Installation

All the _tzxtools_ are written in Python 3 and intended to run as Linux scripts.

```sh
git clone tzxtools
```

## Tools

* `tzxcat` - Extracts data from a TZX file. Optionally disassembles, hex dumps or converts blocks to PNG.
* `tzxcleanup` - Removes all clutter blocks and leaves a clean TZX file.
* `tzxcut` - Cuts blocks from a TZX file.
* `tzxls` - Lists the contents of a TZX file.
* `tzxmerge` - Concatenates multiple TZX files into one file.
* `tzxplay` - Plays back a TZX file for loading into a real ZX Spectrum.
* `tzxsplit` - Splits a TZX file into separate programs.
* `tzxtap` - Converts a TZX file to TAP file format.
* `tzxwav` - Converts WAV file ZX Spectrum tape recordings to TZX files.

See the [documentation](https://shredzone.org/docs/tzxtools/index.html) for how the tools are used.

## File Format References

The TZX File Format is specified at [World of Spectrum](https://worldofspectrum.net/features/TZXformat.html).

The TSX "ID 4B - Kansas City Standard" block is not a part of the specification. A documentation can be found at the [makeTSX wiki](https://github.com/nataliapc/makeTSX/wiki/Tutorial-How-to-generate-TSX-files#14-the-new-4b-block).

The TAP File Format is described at [Sinclair Wiki](https://sinclair.wiki.zxnet.co.uk/wiki/TAP_format).

## Contribute

* Fork the [Source code at GitHub](https://github.com/shred/tzxtools). Feel free to send pull requests.
* Found a bug? [File a bug report!](https://github.com/shred/tzxtools/issues)

## License

_tzxtools_ is open source software. The source code is distributed under the terms of [GNU General Public License (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.en.html#content).

## Acknowledgements

* I would like to thank all the people who keep the retro computing scene alive.
