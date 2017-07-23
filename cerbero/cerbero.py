"""Cerbero

Usage: cerbero [-hv] --config <config> --keydir <keydir>

-h, --help                          Shows this help
-v, --version                       Shows program's version
-c CONFIGFILE, --config=CONFIGFILE  Config file to be used
-k KEYDIR, --keydir=KEYDIR          Key directory to be used
"""

VERSION="Cerbero v0.1.0"

from docopt import docopt
from config import config

def main():
    arguments = docopt(__doc__, help=True, version=VERSION)
    config_path = arguments['--config']
    keydir = arguments['--keydir']
    config.load(config_path, keydir)
    print("Hello world")
