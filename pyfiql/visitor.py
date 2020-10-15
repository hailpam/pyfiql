
class Visitor():
    '''
        It implements the GoF Visitor Deisng Pattern to traverse and customize the
        output of such traversal.
    '''

    def visit_logical_operator(node):
        '''
        '''
        pass

    def visit_expression(node):
        '''
        '''
        pass

class JsonVisitor(Visitor):
    '''
        It implements a JSON version of the Visitor. The output of the visit is
        a JSON object which can be used to then re-serialize as a string upon needs.
    '''
    def visit_logical_operator(node):
        '''
        '''
        pass

    def visit_expression(node):
        '''
        '''
        pass

class SqlVisitor(Visitor):
    '''
        It implements a SQL version of the Visitor. The output of the visit is a SQL statement
        which may be used as filter in a WHERE clause.
    '''
    def visit_logical_operator(node):
        '''
        '''
        pass

    def visit_expression(node):
        '''
        '''
        pass
