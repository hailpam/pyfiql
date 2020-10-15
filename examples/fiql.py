import sys
sys.path.append(__file__.replace('examples/fiql.py', ''))

from pyfiql import model, parser

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
        parser.traverse(root, 0)

    parenthesis = [
        '((()))',
        ')))(((',
        '()()())',
        '(()()'
    ]
    for p in parenthesis:
        print(p, parser.check_parenthesis(p))

if __name__ == '__main__':
    main()
