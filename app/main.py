""" Python application for handling retrieval of public IPv4 and 
    IPv6 addresses using public API.
"""
from requests import get


def get_ipv4():
    """Function for retreiving IPv4 address

    returns:
        ipv4['ip']: Public IP address of host

    """
    ipv4 = get(
        "https://api.ipify.org?format=json"
    ).json()  # use request library to get json from ipapi.co
    return ipv4["ip"]


def get_ipv6():
    """Function for retreiving IPv6 address

    returns:
        ipv6["ip"]: Public IPv6 address of host
    """
    ipv6 = get("https://api64.ipify.org?format=json").json()
    return ipv6["ip"]


""" Driver function """
if __name__ == "__main__":
    print(f"Public IPv4 Address: {get_ipv4()}")
    print(f"Public IPv6 Address: {get_ipv6()}")
