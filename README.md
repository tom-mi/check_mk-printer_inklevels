# check\_mk-printer\_inklevels

[![Build Status](https://travis-ci.org/tom-mi/check_mk-printer_inklevels.svg?branch=master)](https://travis-ci.org/tom-mi/check_mk-printer_inklevels)

Plugin for [Check_MK](https://mathias-kettner.de/check_mk.html) to inklevels of printers via [libinklevel](http://libinklevel.sourceforge.net/).

You can use the [ink](http://ink.sourceforge.net/) command line tool to check if your printer is supported.

## Installation

### Target host

Install [libinklevel](http://libinklevel.sourceforge.net/), e.g. on Debian:

    apt-get install libinklevel

Install the [python wrapper for libinklevel](https://github.com/tom-mi/python-inklevel/):


    pip install inklevel

Copy `agents/plugins/printer_inklevels` to the Check\_MK agent plugin directory, typically `/usr/lib/check_mk_agent/plugins`.

### Check\_MK host

Install the printer\_inklevels package:

    check_mk -P install printer_inklevels-*.mkp

## License

This software is licensed under GPLv2.
