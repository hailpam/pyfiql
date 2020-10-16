import unittest
import sys
sys.path.append(__file__.replace('tests/test_model.py', ''))

from pyfiql.model import *

class TestModel(unittest.TestCase):
    def test_composition(self):
        node = Node()
        constraint = Constraint()
        
        node.constraint = constraint
        node.constraint.operator = ','

        self.assertEqual('[ , ]', str(node.constraint))

if __name__ == "__main__":
    unittest.main()
