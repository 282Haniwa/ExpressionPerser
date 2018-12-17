#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
木を出力するためのクラス
"""
class BinaryTreePrinter(object):
    def __init__(self, tree):
        self.__tree = tree

    """
    treeプロパティのgetter
    """
    @property
    def tree(self):
        return self.__tree

    """
    木を標準出力に出力する
    """
    def printTree(self):
        node_list = self.tree.get_preorder_node_list()
        for node in node_list:
            if node.is_root():
                print(node.data['word'])
            else:
                print('    ' * (node.depth() - 1) + '|-- ' + node.data['word'])

    """
    木から式を前置記法にして標準出力に出力する
    """
    def printPreorderExpression(self):
        node_list = self.tree.get_preorder_node_list()
        for node in node_list:
            print(' ' + node.data['word'], end='')
        print()

    """
    木から式を中置記法にして標準出力に出力する
    """
    def printInorderExpression(self):
        node_list = self.tree.get_inorder_node_list()
        for node in node_list:
            print(' ' + node.data['word'], end='')
        print()

    """
    木から式を後置記法にして標準出力に出力する
    """
    def printPostorderExpression(self):
        node_list = self.tree.get_postorder_node_list()
        for node in node_list:
            print(' ' + node.data['word'], end='')
        print()
