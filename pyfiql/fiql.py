import re

# TODO - well formed regexp
REGEXP = r'(?P<loperand>[\w-]+)(?P<operator>=.{0,}=)(?P<roperand>[\"\w-]+)'

class Expression:
    def __init__(self, l_operand='', r_operand='', operator=''):
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.operator = operator

    def __str__(self):
        return '[%s %s %s]' % (self.l_operand, self.operator, self.r_operand)

class Node:
    def __init__(self, l_child=None, r_child=None, expression=None):
        self.l_child = l_child
        self.r_child = r_child
        self.expression = expression
    
    def __str__(self):
        return '{%s %s %s}' % (self.l_child, self.expression, self.r_child)

def is_expression(string):
    return string.find(',') == -1 and string.find(';') == -1

def find_token(string):
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
        ((()))  - correct
        )))(((  - incorrect
        ()()()) - incorrect
        (()()   - incorrect
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
    if len(string) == 0:
        return None
    root = Node()
    idx, string = find_token(string)
    if idx == -1:
        res = re.search(REGEXP, string)
        root.expression = Expression(l_operand=res.group('loperand'), r_operand=res.group('roperand'), operator=res.group('operator'))
    else:
        root.expression = Expression(operator=string[idx])
        root.l_child = scan(string[0:idx])
        root.r_child = scan(string[idx+1:])
    return root

def traverse(root, level):
    pretty = '%s%s' % (''.join(['\t' for x in range(level)]), root.expression)
    print(pretty)
    level += 1
    if root.l_child:
        traverse(root.l_child, level)
    if root.r_child:
        traverse(root.r_child, level)

def main():
    queries = [
        '(((((product=="Apple",product=="Google");(name=="Joe",name=="Alan")));label=!~="text";(qty=gte=1,qty=lte=10)))',
        '(product=="Apple",product=="Google");(name=="Joe",name=="Alan");(qty=gte=1,qty=lte=10)',
        '(qty=gt=1;(qty=gte=1,qty=lte=10));(product=="Apple",product=="HP")',
        '(product=="Apple",qty=lt=1);name=="Joe"',
        'name==bar,dob=gt=1990-01-01'
    ]

    for query in queries:
        print(query)
        root = scan(query)
        traverse(root, 0)

    parenthesis = [
        '((()))',
        ')))(((',
        '()()())',
        '(()()'
    ]
    for p in parenthesis:
        print(p, check_parenthesis(p))

if __name__ == '__main__':
    main()
