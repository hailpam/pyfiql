import json
import sys
sys.path.append(__file__.replace('examples/fiql.py', ''))

from pyfiql import model, parser, util, visitor

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
        root = parser.scan(query)
        util.pretty_printing(root, 0)

    parenthesis = [
        '((()))',
        ')))(((',
        '()()())',
        '(()()'
    ]
    for p in parenthesis:
        print(p, parser.check_parenthesis(p))

    queries = [
        'name=="bar",date=gt=1990-01-01',
        '(product=="Apple",qty=lt=1);name=="Joe"',
        '(qty=gt=1;(qty=gte=1,qty=lte=10));(product=="Apple",product=="HP")',
        '(product=="Apple",product=="Google");(name=="Joe",name=="Alan");(qty=gte=1,qty=lte=10)',
        '(((((product=="Apple",product=="Google");(name=="Joe",name=="Alan")));label=!~="text";(qty=gte=1,qty=lte=10)))'
    ]
    for query in queries:
        root = parser.scan(query)
        visit = visitor.SqlVisitor()
        visitor.traversal(root, visit)
        print(visit.expressions)
    
    for query in queries:
        root = parser.scan(query)
        visit = visitor.JsonVisitor()
        visitor.traversal(root, visit)
        print(json.dumps(visit.expressions, indent=2))

if __name__ == '__main__':
    main()
