class Expression:
    '''
    '''
    def __init__(self, l_operand='', r_operand='', operator=''):
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.operator = operator

    def __str__(self):
        return '[%s %s %s]' % (self.l_operand, self.operator, self.r_operand)

class Node:
    '''
    '''
    def __init__(self, l_child=None, r_child=None, expression=None):
        self.l_child = l_child
        self.r_child = r_child
        self.expression = expression
    
    def __str__(self):
        return '{%s %s %s}' % (self.l_child, self.expression, self.r_child)