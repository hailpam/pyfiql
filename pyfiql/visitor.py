
from pyfiql.definition import *

NOT_IMPLEMENTED_ERROR = 'Method to be implemented with specific logic'

class Visitor():
    '''
        It implements the GoF Visitor Deisng Pattern to traverse and customize the
        output of such traversal.
    '''

    def visit_logical_operator(self, node):
        '''
            Upon a visit of an operator, ties a specific handler to implement 
            custom transformation/mediation logic.
        '''
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

    def visit_expression(self, node):
        '''
            Upon a visit of an expression, ties a specific handler to implement 
            custom transformation/mediation logic.
        '''
        raise NotImplementedError(NOT_IMPLEMENTED_ERROR)

class JsonVisitor(Visitor):
    '''
        It implements a JSON version of the Visitor. The output of the visit is
        a JSON object which can be used to then re-serialize as a string upon needs.
    '''
    def __init__(self):
        self.expressions = []

    def visit_logical_operator(self, node):
        '''
            A specific implementation. It serializes the content of the AST with the
            Polish notation.

                {
                    '<logical_operator>': [
                        <expression>
                    ]
                }
        '''
        r_expression = self.expressions.pop()
        l_expression = self.expressions.pop()
        operator = SQL_LOGICAL_OPERATOR[node.constraint.operator]
        self.expressions.append({
            operator: [
                l_expression,
                r_expression
            ]
        })

    def visit_expression(self, node):
        '''
            A specific implementation. It serializes the content of the AST with the
            Polish notation.

            {
                '<constraint_operator>': [
                    <l_operand>, 
                    <r_operand>
                ]
            }
        '''
        operator = SQL_CONSTRAINT_OPERATOR[node.constraint.operator]
        self.expressions.append({
            operator: [
                node.constraint.l_operand,
                node.constraint.r_operand
            ]
        })

class SqlVisitor(Visitor):
    '''
        It implements a SQL version of the Visitor. The output of the visit is a SQL statement
        which may be used as filter in a WHERE clause.
    '''
    def __init__(self):
        self.expressions = []

    def visit_logical_operator(self, node):
        '''
            A specific implementation. It serializes the content of the AST with the
            Infix notation.

             (<l_expression> <logical_operator> <r_expression>)
        '''
        r_expression = self.expressions.pop()
        l_expression = self.expressions.pop()
        operator = SQL_LOGICAL_OPERATOR[node.constraint.operator]
        expression = '(%s %s %s)' % (l_expression, operator, r_expression)
        self.expressions.append(expression)

    def visit_expression(self, node):
        '''
            A specific implementation. It serializes the content of the AST with the
            Infix notation.

                <l_operand> <constraint_operator> <r_operand>
        '''
        operator = SQL_CONSTRAINT_OPERATOR[node.constraint.operator]
        constraint = '%s %s %s' % (node.constraint.l_operand, operator, node.constraint.r_operand)
        self.expressions.append(constraint)

def traversal(root, visitor):
    '''
        Implemnts a generic traversal algorithm which applies the specific visitor instance
        provided in input.
    '''
    if root:
        if root.l_child:
            traversal(root.l_child, visitor)
        if root.r_child:
            traversal(root.r_child, visitor)
        root.accept(visitor)
