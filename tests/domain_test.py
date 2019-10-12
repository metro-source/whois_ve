import whois_ve
import unittest
import logging
class DomainTestCase(unittest.TestCase):
    def test_domain_unvaialable(self):
        self.assertFalse(whois_ve.lookup('petro.com.ve'))
        self.assertFalse(whois_ve.lookup('cantv.net.ve'))
        self.assertFalse(whois_ve.lookup('bitcoin.com.ve'))
    
    def test_domain_available(self):
        self.assertTrue(whois_ve.lookup('sadzxncvbjxvc9191ad.info.ve'))
        self.assertTrue(whois_ve.lookup('madurooooooooooooooo.org.ve'))

    def test_invalid_tld(self):
        for domain in ('bitcoin.com', 'petro.gob.ve', 'nic.ve'):
            with self.assertLogs(logging.getLogger(), level='INFO'):
                whois_ve.lookup(domain)
