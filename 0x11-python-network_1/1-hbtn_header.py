#!/usr/bin/python3
"""
A script that takes a URL, sends a request to the URL,
and displays the value of the X-Request-Id header
variable found in the response.


Usage:
    ./1-hbtn_header.py URL


Arguments:
    URL: The URL to send the request to.


Example:
    ./1-hbtn_header.py https://alx-intranet.hbtn.io

"""


import sys
import urllib.request
import urllib.error


def get_x_request_id(url):
    """
    Sends an HTTP GET request to the given URL
    and returns the value of the X-Request-Id
    header variable.


    Args:
        url (str): The URL to send the request to.


    Returns:
        str: The value of the X-Request-Id header variable.


    Raises:
        urllib.error.URLError: If the request fails due to a network error.
        ValueError: If the response does not contain the X-Request-Id
        header variable.

    """

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id is None:
                raise ValueError("Response does not contain the\
                                 X-Request-Id header variable.")
            return x_request_id
    except urllib.error.URLError as e:
        raise e


if __name__ == "__main__":
    # Check that the script was called with the correct number of arguments
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} URL")
        print(f"For example: {sys.argv[0]} https://example.com")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Get the value of the X-Request-Id header variable
    try:
        x_request_id = get_x_request_id(url)
        print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Failed to get X-Request-Id: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Failed to get X-Request-Id: {e}")
        sys.exit(1)
