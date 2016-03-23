#!/usr/bin/env python3

import sys
import urllib.request
from asyncore import socket

def main(argv=None):
    """Main function

    Args:
        argv: Collection of parameters from command line

    Returns:
        Nothing
    """
    min, max = min_max([12, 13, 554, 3235, 221, 923, 1])

    print("Min = {min}, Max = {max}".format(min=min, max=max))

    response = urllib.request.urlopen('http://python.org/')
    html = response.read();


def response_callback(resp):
    print(resp.url)

def min_max(items):
    return min(items), max(items);


if __name__ == "__main__":
    main()