#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from experser.BinaryTreePrinter import BinaryTreePrinter
from experser.ExpressionPerser  import ExpressionPerser

"""
メインプログラム
"""
def main():
    expression_list = [
        {
            'content'   : '- + a / b c * d e',
            'type'      : 'preorder'
        },
        {
            'content'   : 'a > ( b * ( c + d ) / e )',
            'type'      : 'inorder'
        },
        {
            'content'   : 'a b / c d * e + <',
            'type'      : 'postorder'
        },
        {
            'content'   : 'a + b',
            'type'      : 'inorder'
        }
    ]
    anExpressionPerser = ExpressionPerser()
    for expression in expression_list:
        aTree = anExpressionPerser.perse_expression(expression['content'], expression['type'])
        aBinaryTreePrinter = BinaryTreePrinter(aTree)
        print(expression['type'] + ' : ' + expression['content'])
        print('Tree:')
        aBinaryTreePrinter.printTree()
        print()
        print('PreorderExpression  : ', end='')
        aBinaryTreePrinter.printPreorderExpression()
        print('InorderExpression   : ', end='')
        aBinaryTreePrinter.printInorderExpression()
        print('PostorderExpression : ', end='')
        aBinaryTreePrinter.printPostorderExpression()
        print()

if __name__ == '__main__':
    import sys
    sys.exit(main())
