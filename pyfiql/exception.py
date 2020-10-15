
class FiqlError(Exception):
    '''
        Base error. It fills up the error message with a custom-provided one.
    '''
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class FiqlMalformedParenthesis(FiqlError):
    '''
        Expressely raised in case the parenthesis and so precedence checks do
        not pass.
    '''
    pass

class FiqlMalformedExpression(FiqlError):
    '''
        Expressely raised in case the expression is malformed, i.e. it does not
        respect the pattern defined by the FIQL grammar.
    '''
    pass
