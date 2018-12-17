#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二進木のノードを表すクラス
"""
class BinaryNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.__data   = data
        self.__parent = None
        self.__left = None
        self.__right = None
        if isinstance(left, BinaryNode):
            left.parent = self
            self.__left = left
        else:
            ValueError('Please set BinaryNode object.')
        if isinstance(right, BinaryNode):
            right.parent = self
            self.__right = right
        else:
            ValueError('Please set BinaryNode object.')

    """
    dataプロパティのgetter
    """
    @property
    def data(self):
        return self.__data

    """
    dataプロパティのsetter
    """
    @data.setter
    def data(self, data):
        self.__data = data
        return

    """
    parentプロパティのgetter
    """
    @property
    def parent(self):
        return self.__parent

    """
    parentプロパティのsetter
    通常はこのsetterを呼び出す必要はありません
    このノードをルートとしてこのノード以下を一つの木として切り出したい時に、
    parentにNoneをセットすることでルートとできます
    """
    @parent.setter
    def parent(self, node):
        if isinstance(node, BinaryNode):
            self.__parent = node
            return
        raise ValueError('Please set BinaryNode object.')

    """
    leftプロパティのgetter
    """
    @property
    def left(self):
        return self.__left

    """
    leftプロパティのsetter
    leftプロパティを設定した時に自動的にセットしたノードのparentに自身のノードがセットされます。
    """
    @left.setter
    def left(self, node):
        if isinstance(node, BinaryNode):
            node.parent = self
            self.__left = node
            return
        raise ValueError('Please set BinaryNode object.')

    """
    rightプロパティのgetter
    """
    @property
    def right(self):
        return self.__right

    """
    rightプロパティのsetter
    rightプロパティを設定した時に自動的にセットしたノードのparentに自身のノードがセットされます。
    """
    @right.setter
    def right(self, node):
        if isinstance(node, BinaryNode):
            node.parent = self
            self.__right = node
            return
        raise ValueError('Please set BinaryNode object.')

    """
    自身のノードの深さを返す
    """
    def depth(self):
        return self.__calc_depth(0, self)

    """
    自身のノードの高さを返す
    """
    def height(self):
        return self.__calc_height(0, self)

    """
    自身のノードが葉であるかを返す
    """
    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    """
    自身のノードが根であるかを返す
    """
    def is_root(self):
        if self.parent is None:
            return True
        return False

    """
    自身のノードの高さを再帰的に計算する
    """
    def __calc_depth(self, depth, node):
        if node.is_root():
            return depth
        return self.__calc_depth(depth + 1, node.parent)

    """
    自身のノードの高さを再帰的に計算する
    """
    def __calc_height(self, height, node):
        if node.is_leaf():
            return height
        left_height = 0
        right_height = 0
        if node.left:
            left_height = self.__calc_height(height + 1, node.left)
        if node.right:
            right_height = self.__calc_height(height + 1, node.right)
        return max(left_height, right_height)
