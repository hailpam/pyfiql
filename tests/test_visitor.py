import unittest
import sys
sys.path.append(__file__.replace('tests/test_visitor.py', ''))

from pyfiql.model import *
from pyfiql.visitor import *


class TestVisitor(unittest.TestCase):
    def test_sql_visitor_logical_operator(self):
        l_node = ExpressionNode()
        l_node.constraint = Constraint()
        l_node.constraint.operator = '=='
        l_node.constraint.l_operand = 'name'
        l_node.constraint.r_operand = '"Joe"'

        r_node = ExpressionNode()
        r_node.constraint = Constraint()
        r_node.constraint.operator = '=='
        r_node.constraint.l_operand = 'name'
        r_node.constraint.r_operand = '"Brad"'
        
        node = OperatorNode()
        node.l_child = l_node
        node.r_child = r_node
        node.constraint = Constraint()
        node.constraint.operator = ','

        visit = SqlVisitor()
        visit.expressions.append('name = "Joe"')
        visit.expressions.append('name = "Brad"')
        visit.visit_logical_operator(node)

        self.assertEqual(visit.expressions[0], '(name = "Joe" OR name = "Brad")')

    def test_sql_visitor_expression(self):
        node = ExpressionNode()
        node.constraint = Constraint()
        node.constraint.operator = '=='
        node.constraint.l_operand = 'name'
        node.constraint.r_operand = '"Joe"'

        visit = SqlVisitor()
        visit.visit_expression(node)

        self.assertEqual(visit.expressions[0], 'name = "Joe"')

    def test_json_visitor_logical_operator(self):
        pass

    def test_json_visitor_expression(self):
        pass

if __name__ == '__main__':
    unittest.main()
