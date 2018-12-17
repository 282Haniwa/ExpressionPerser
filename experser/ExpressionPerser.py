#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

from experser.tree.BinaryNode   import BinaryNode
from experser.tree.BinaryTree   import BinaryTree
from experser.TokenDefinition   import TokenDefinition

"""
Expressionをperseするためのクラス
"""
class ExpressionPerser(object):
    def __init__(self):
        import copy
        self.__TOKEN_TYPE = copy.deepcopy(TokenDefinition.TOKEN_TYPE)
        self.__TOKEN_TYPE_PATTERN = {key: re.compile(pattern) for key, pattern in TokenDefinition.TOKEN_TYPE.items()}
        self.__SYNTAX_TYPE = {
            'preorder'  : self.__preorder_perse,
            'inorder'   : self.__inorder_perse,
            'postorder' : self.__postorder_perse
        }

    """
    TOKEN_TYPEプロパティのgetter
    """
    @property
    def TOKEN_TYPE(self):
        return self.__TOKEN_TYPE

    """
    Expressionをperseするメソッド
    syntax_typeで['preorder', 'inorder', 'postorder']を指定して、どの記法で記述されているかを指定する。
    """
    def perse_expression(self, expression, syntax_type):
        token_list = self.__scan_token(expression)
        expression_tree = None
        if syntax_type in self.__SYNTAX_TYPE.keys():
            expression_tree = self.__SYNTAX_TYPE[syntax_type](token_list)
        return expression_tree

    """
    字句解析を行いトークンのリストを出力する
    """
    def __scan_token(self, expression):
        word_list = expression.split()
        token_list = []
        for word in word_list:
            for key, pattern in self.__TOKEN_TYPE_PATTERN.items():
                if pattern.fullmatch(word):
                    token = {'type': key, 'word': word}
                    token_list.append(token)
        return token_list

    """
    前置記法のトークンのリストから木を作り出す。
    """
    def __preorder_perse(self, token_list):
        stack = []
        item_count_stack = [0]
        # print('__preorder_perse()')
        # print('token_list:',  [token['word'] for token in token_list])
        for token in token_list:
            if token['type'] == 'id':
                stack.append(BinaryNode(token))
                item_count_stack[-1] += 1
                while item_count_stack[-1] == 2:
                    right = stack.pop()
                    left = stack.pop()
                    current_node = stack.pop()
                    current_node.left = left
                    current_node.right = right
                    stack.append(current_node)
                    item_count_stack.pop()
                    item_count_stack[-1] += 1
                    # print('stack:', [node.data['word'] for node in stack])
                    # print('item_count_stack:', item_count_stack)
                    # print()
            else:
                item_count_stack.append(0)
                stack.append(BinaryNode(token))
            # print('stack:', [node.data['word'] for node in stack])
            # print('item_count_stack:', item_count_stack)
            # print()
        if len(stack) == 1:
            return BinaryTree(stack.pop())
        raise Exception('Invalid syntax.')

    """
    操車場のアルゴリズムで中置記法から木を作り出す。
    """
    def __inorder_perse(self, token_list):
        from collections import deque
        stack = []
        queue = deque([])
        # print('__inorder_perse()')
        # print('token_list:',  [token['word'] for token in token_list])
        for token in token_list:
            if token['type'] == 'id':
                queue.append(token)
            if token['type'] == 'operator':
                while stack and not self.__is_prior_operater(stack, token):
                    poped_token = stack.pop()
                    queue.append(poped_token)
                stack.append(token)
            if token['type'] == 'left_paren':
                stack.append(token)
            if token['type'] == 'right_paren':
                while stack[-1]['type'] != 'left_paren':
                    poped_token = stack.pop()
                    queue.append(poped_token)
                else:
                    stack.pop()
            # print('stack:',  [token['word'] for token in stack])
            # print('queue:',  [token['word'] for token in queue])
            # print()
        for token in stack:
            poped_token = stack.pop()
            queue.append(poped_token)
        try:
            return self.__postorder_perse(list(queue))
        except Exception as exception:
            raise exception

    """
    後置記法のトークンのリストから木を作り出す。
    """
    def __postorder_perse(self, token_list):
        stack = []
        # print('__postorder_perse()')
        # print('token_list:',  [token['word'] for token in token_list])
        for token in token_list:
            if token['type'] == 'id':
                stack.append(BinaryNode(token))
            else:
                right = stack.pop()
                left = stack.pop()
                current_node = BinaryNode(token, left, right)
                stack.append(current_node)
            # print('stack:', [node.data['word'] for node in stack])
        if len(stack) == 1:
            return BinaryTree(stack.pop())
        raise Exception('Invalid syntax.')

    """
    スタックのトップにあるトークンと第２引数のトークンを比較し、
    第２引数のトークンの方が優先度の高いオペレータであった時のみTrueを返す。
    """
    def __is_prior_operater(self, stack, token):
        if not stack:
            return False
        # オペレータの優先度がstackのトップにあるオペレータの優先度より高いか調べる
        if stack[-1]['type'] != 'operater' or TokenDefinition.OPERATOR_PRIORITY[token['word']] > TokenDefinition.OPERATOR_PRIORITY[stack[-1]['word']]:
            return True
        return False
