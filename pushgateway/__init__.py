import os
import logging
import argparse
from pushgateway.gateway import run, default_config_file
from pushgateway.unit import register, deregister, printlog

PACKAGENAME = 'pushgateway'
ENTRY_POINT = "pushgateway"
DESCRIPTION = "A push gateway sending webthing properties updates to a openhab server"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--filename', metavar='filename', required=False, type=str,  help='the config filename')
    args = parser.parse_args()

    if args.filename == None:
        filename = default_config_file()
    else:
        filename = args.filename

    run(filename)


if __name__ == '__main__':
    log_level = os.environ.get("LOGLEVEL", "INFO")
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=log_level, datefmt='%Y-%m-%d %H:%M:%S')

    main()

