import re

from pyfiql.model import *
from pyfiql.exception import *
from pyfiql.definition import *


def is_expression(string):
    '''
        Checks whether the input string represents a basic FIQL expression (i.e. one which
        does not get any logical operator).

        Parameters:
        string (str): input string to be checked.

        Returns:
        bool: True in case of basic expression, False otherwise
    '''
    return string.find(',') == -1 and string.find(';') == -1

def find_token(string):
    '''
        Finds the first index of a token, respecting the parenthesis and related precedence.
        It gets rid of non-meaningful parenthesis in the process of iterative scanning. Tokens
        are intended as logical operators by the definition of the FIQL standard.

        Parameters:
        string (str): input string to be scanned in search of the next token.

        Returns:
        int: -1 in case of any no match with lofical operators, matched position otherwise
        str: current version of the string (unuseful parenthesis may be stripped off)
    '''
    while not is_expression(string):
        cntr = 0
        for i, c in enumerate(string):
            if c == '(':
                cntr += 1
            if c == ')':
                cntr -= 1
            if cntr == 0 and (c == ',' or c == ';'):
                return i, string
        if string[0] == '(' and string[-1] == ')':
            string = string[1:-1]

    return -1, string

def check_parenthesis(string):
    '''
        Scans the parenthesis looking for incorrect coupling, meaning incorrect precedence.

        Parameters:
        string (str): input string to be checked for correctness.

        Returns:
        bool: True in case of correct precedence, False otherwise
    '''
    c = 0
    l = []
    for _, s in enumerate(string):
        if s == '(':
            c += 1
            l.append(s)
        if s == ')':
            c -= 1
            if len(l) > 0 and l[-1] == '(':
                l.pop()
    if c != 0 or len(l) > 0:
        return False
    
    return True

def scan(string):
    '''
        Scans recursively the input string and builds incrementally an Abstract Syntax Tree (AST). 
        It returns systematically the root node which is linked to the contextual subtree.

        Parameters:
        string (str): input string container the serialized version of the FIQL composite expression.

        Returns:
        Node: AST root node.
    '''
    if not check_parenthesis(string):
        raise FiqlMalformedParenthesis('%s has inconsistent precendence(s)' % string)
    if len(string) == 0:
        return None
    root = None
    idx, string = find_token(string)
    if idx == -1:
        res = re.search(REGEXP_CONSTRAINT, string)
        try:
            root = ExpressionNode()
            root.constraint = Constraint(l_operand=res.group('loperand'), r_operand=res.group('roperand'), operator=res.group('operator'))
        except Exceptio as e:
            raise FiqlMalformedExpression('%s cannot be matched: %s' % (string, e))
    else:
        root = OperatorNode()
        root.constraint = Constraint(operator=string[idx])
        root.l_child = scan(string[0:idx])
        root.r_child = scan(string[idx+1:])
    return root
