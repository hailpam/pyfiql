import unittest
import sys
sys.path.append(__file__.replace('tests/test_parser.py', ''))

from pyfiql.parser import *

class TestParser(unittest.TestCase):
    def test_blah(self):
        self.assertEqual(4, 4)

if __name__ == "__main__":
    unittest.main()
