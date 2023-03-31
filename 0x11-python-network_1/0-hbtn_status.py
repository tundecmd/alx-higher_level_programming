#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
using urllib and displays the body of the response.
"""


if __name__ == "__main__":
    from urllib.request import urlopen

    def getStatus(url):
        """
        A function that fetches the contents of a URL
        using urlopen and displays its contents.

        Args:
            url (str): The URL to fetch.

        Returns:
            None. The function only prints the contents of the URL.

        """

        # Open the URL as a response object
        with urlopen(url) as res:

            # Read the contents of the response
            status = res.read()

            # Display the body of the response in the required format
            print("Body response:")
            print("\t- type: {}".format(type(status)))
            print("\t- content: {}".format(status))
            print("\t- utf8 content: {}".format(status.decode('utf-8')))

    # URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Call the getStatus function with the URL
    getStatus(url)
