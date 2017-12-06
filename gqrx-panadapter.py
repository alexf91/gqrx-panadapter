#!/usr/bin/env python
#
# Copyright 2017 Alexander Fasching
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import print_function, division

import sys
import argparse
import socket
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--gqrx-port', type=int, default=7356,
            metavar='P', help='remote control port configured in Gqrx')
    parser.add_argument('-r', '--rigctld-port', type=int, default=4532,
            metavar='P', help='listening port of rigctld')
    parser.add_argument('-i', '--interval', type=int, default=1000,
            metavar='T', help='update interval in milliseconds')
    parser.add_argument('-f', '--ifreq', type=float, default=68.33,
            metavar='F', help='intermediate frequency in MHz')

    args = parser.parse_args()

    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs.connect(('127.0.0.1', args.rigctld_port))
    except Exception as e:
        print('Connection to rigctld failed:', e, file=sys.stderr)
        return 1

    try:
        gs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gs.connect(('127.0.0.1', args.gqrx_port))
    except Exception as e:
        print('Connection to Gqrx failed:', e, file=sys.stderr)
        return 1

    try:
        while True:
            rs.send(b'f\n')

            rigfreq = int(rs.recv(1024))
            lnbfreq = rigfreq - int(args.ifreq * 1e6)

            gs.send('LNB_LO {}'.format(lnbfreq).encode())
            gs.recv(1024)

            time.sleep(args.interval / 1000.0)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print('Unexpected error:', e, file=sys.stderr)
        return 1

    rs.close()
    gs.close()


if __name__ == '__main__':
    sys.exit(main() or 0)
