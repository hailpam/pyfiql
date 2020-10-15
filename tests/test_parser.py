import unittest
import sys
sys.path.append(__file__.replace('tests/test_parser.py', ''))

from pyfiql.parser import *

class TestParser(unittest.TestCase):
    def test_check_parenthesis_positive(self):
        parenthesis = [
            '((()))',
            '(()()()()())',
            '(())(()()()()())'
        ]
        for p in parenthesis:
            self.assertTrue(check_parenthesis(p))

    def test_check_parenthesis_negative(self):
        parenthesis = [
            ')))(((',
            '()()())',
            '(()()',
            '()()())('
        ]
        for p in parenthesis:
            self.assertFalse(check_parenthesis(p))
    
    def test_is_expression_positive(self):
        expression = [
            'name=="a"',
            '(name=="a")'
        ]
        for e in expression:
            self.assertTrue(is_expression(e))
    
    def test_is_expression_negative(self):
        expression = [
            'name=="a",name=="b"',
            'name=="a";name=="b"',
            '(name=="a",name=="b");qty=lt=100'
        ]
        for e in expression:
            self.assertFalse(is_expression(e))
    
    def test_find_token_positive(self):
        expression = [
            'name=="Joe",name=="Pit"',
            '(name=="Joe",name=="Brad");(surname=="Joe",surname=="Pit")',
            '((name=="Joe";surname=="Doe"),address=!=="");qty=lt=100',
            '((name=="Joe";surname=="Doe"),(name=="Brad";surname=="Pit"))'
        ]
        for i, e in enumerate(expression):
            idx, text = find_token(e)
            if i == 0:
                self.assertEqual(idx, 11)
                self.assertEqual(text, 'name=="Joe",name=="Pit"')
            if i == 1:
                self.assertEqual(idx, 26)
                self.assertEqual(text, '(name=="Joe",name=="Brad");(surname=="Joe",surname=="Pit")')
            if i == 2:
                self.assertEqual(idx, 44)
                self.assertEqual(text, '((name=="Joe";surname=="Doe"),address=!=="");qty=lt=100')
            if i == 3:
                self.assertEqual(idx, 28)
                self.assertEqual(text, '(name=="Joe";surname=="Doe"),(name=="Brad";surname=="Pit")')

    def test_find_token_negative(self):
        expression = [
            'name=="Joe"',
            'qty=lte=100',
            'date=lt=2020-10-10'
        ]
        for e in expression:
            idx, text = find_token(e)
            self.assertEqual(idx, -1)
            self.assertTrue(text != '')

if __name__ == "__main__":
    unittest.main()
