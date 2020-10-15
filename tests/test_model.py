import unittest
import sys
sys.path.append(__file__.replace('tests/test_model.py', ''))

from pyfiql.model import *

class TestModel(unittest.TestCase):
    def test_blah(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
