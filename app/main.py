""" Python application for handling retrieval of public IPv4 and 
    IPv6 addresses using public API.
"""
import requests


def get_ipv4():
    """Function for retreiving IPv4 address"""
    pass


def get_ipv6():
    """Function for retreiving IPv6 address"""
    response = requests.get("https://api64.ipify.org?format=json")
    ip = response.json()["ip"]
    return ip


""" Driver function """
if __name__ == "__main__":
    print(f"Public IPv4 Address: {get_ipv4()}")
    print(f"Public IPv6 Address: {get_ipv6()}")
