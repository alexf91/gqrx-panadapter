# Gqrx Panadapter

A [Gqrx](http://gqrx.dk/) to [Hamlib](http://www.hamlib.org) interface that
keeps the frequency displayed in Gqrx synchronized with the frequency settings
on your radio.

The IF output of the radio should be connected to a SDR, which is then received by Gqrx.
This script continuously reads the frequency of the radio from ```rigctld```
and sets the LNB setting Gqrx.

## Usage

```
gqrx-panadapter.py [-h] [-g P] [-r P] [-i T] [-f F]

optional arguments:
  -h,   --help            show this help message and exit
  -g P, --gqrx-port P     remote control port configured in Gqrx
  -r P, --rigctld-port P  listening port of rigctld
  -i T, --interval T      update interval in milliseconds
  -f F, --ifreq F         intermediate frequency in MHz
```

Make sure you configure [remote control](http://gqrx.dk/doc/remote-control) in Gqrx.
