🇻🇪 Domain Whois Lookup 
===

Programatically check if a .ve domain name is available 

# Installation

Using pip
```
pip install git+https://github.com/metro-source/whois_ve.git
```

# Usage

Within python

```python
from whois_ve import lookup

# returns True if the domain is available for registration
lookup('cooldomainname.com.ve')

# False if it's already registered
lookup('bitcoin.com')

# prints a warning using python's logger module if the domain is not .ve
lookup('google.com')

```
From the command line

```bash
python whois_ve.py [domain]
```


```bash
$ python whois_ve.py petro.com.ve

Domain bitcoin.com.ve is already registered, more info:
http://whois.nic.ve/whois/domain/bitcoin.com.ve/
```

# License

GPL, see LICENSE file 