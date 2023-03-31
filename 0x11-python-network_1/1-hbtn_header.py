#!/usr/bin/python3
"""
A script that takes a URL, sends a request to the URL,
and displays the value of the X-Request-Id header
variable found in the response.
"""


import sys
from urllib.request import urlopen
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    with urlopen(url) as res:
        print(dict(res.headers).get('X-Request-Id'))
