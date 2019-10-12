#!/usr/bin/env python
"""
Extracts information on .ve domains
"""

"""
Copyright (C) metrodev.io

This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
General Public License as published by the Free Software Foundation, either version 3 of the License,
 or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even 
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public 
License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see the LICENSE file or send message at contact @ metrodev.io
"""

import requests
import logging
import argparse

LOOKUP_URL = 'http://whois.nic.ve/whois/domain/{}/'

"""
Supported TLDs
"""
TLDs = (
    '.com.ve',
    '.net.ve',
    '.org.ve',
    '.info.ve',
    '.web.ve'
)

def lookup(domain: str) -> bool:
    """
    Lookup a .ve domain name

    Returns True if the domain name is available for registration
    """
    valid = False

    for tld in TLDs:
        if domain.endswith(TLDs):
            valid = True
            break

    if not valid:
        logging.getLogger('whois_ve').warn(f"Warning: invalid domain {domain}")
    
    response = requests.get(LOOKUP_URL.format(domain))

    available = "Domain not found" in response.text

    return available

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Lookup .ve domain names')
    parser.add_argument('domain', type=str)

    args = parser.parse_args()

    if lookup(args.domain):
        print(f"Domain {args.domain} is available for registration")
    else:
        print(f"Domain {args.domain} is already registered, more info:")
        print(LOOKUP_URL.format(args.domain))