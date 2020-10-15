
class Constraint:
    '''
        According to the FIQL standard, it models a constraint in the form of:

            <l_operand><operator><r_operand>

        Operator is intended as a a language specific one. The set of constraint
        operators may be extendable according to the grammar.
    '''
    def __init__(self, l_operand='', r_operand='', operator=''):
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.operator = operator

    def __str__(self):
        return '[%s %s %s]' % (self.l_operand, self.operator, self.r_operand)

class Node:
    '''
        Abstracts a node of an AST. It has left and right childs as the logical operators 
        are intended as intermediate nodes; leaves are representd by constraints.

        An example:
            ;
                ,
                    l_operand operator r_operand
                    l_operand operator r_operans
                l_operand operator r_operand
        
        The root of the tree starts with a logical operator. According to the depth, one or
        more intermediate levels of logical operatos can alternate to eventually get to the
        leaves.
    '''
    def __init__(self, l_child=None, r_child=None, constraint=None):
        self.l_child = l_child
        self.r_child = r_child

        self.constraint = constraint
    def accept(self, visitor):
        '''
            Accepts a Visito in and according to the node type it is going to apply
            the custom and specific logic, upon any traversal of the AST.
        '''
        raise NotImplementedError('Should be implemented by concrete classes')

    def __str__(self):
        return '{%s %s %s}' % (self.l_child, self.expression, self.r_child)

class OperatorNode(Node):
    '''
        Defines an Operator node. 
    '''
    def accept(self, visitor):
        visitor.visit_logical_operator(self)

class ExpressionNode(Node):
    '''
        Defines an Expression node. 
    '''
    def accept(self, visitor):
        visitor.visit_expression(self)
