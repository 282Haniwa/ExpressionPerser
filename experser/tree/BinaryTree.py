#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
二進木の木を表すクラス
"""
class BinaryTree(object):
    def __init__(self, root):
        if root.is_root():
            self.__root = root
        else:
            raise ValueError(root + 'is not root node.')

    """
    rootプロパティのgetter
    """
    @property
    def root(self):
        return self.__root

    """
    木自体の高さを返す
    """
    def height(self):
        return self.root.height()

    """
    目当てのノードを探して返す
    存在しなければNoneを返す
    """
    def search(self, x):
        node = self.root
        while node:
            if node.data == x: return True
            if x < node.data:
                node = node.left
            else:
                node = node.right
        return None

    """
    ノードを深さ優先探索の前順で整列してリストとして返す
    """
    def get_preorder_node_list(self):
        stack = []
        node_list = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            node_list.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return node_list

    """
    ノードを深さ優先探索の中順で整列してリストとして返す
    """
    def get_inorder_node_list(self):
        stack = []
        node_list = []
        node = self.root
        done = False
        while not done:
            if node:
                stack.append(node)
                node = node.left
            else:
                if stack:
                    node = stack.pop()
                    node_list.append(node)
                    node = node.right
                else:
                    done = True
        return node_list

    """
    ノードを深さ優先探索の後順で整列してリストとして返す
    """
    def get_postorder_node_list(self):
        stack1 = []
        stack2 = []
        node_list = []
        stack1.append(self.root)
        while stack1:
            node = stack1.pop() 
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            node_list.append(node)
        return node_list

    """
    ノードを幅優先探索の順で整列してリストとして返す
    """
    def get_level_order_node_list(self, node):
        from collections import deque
        queue = deque([])
        node_list = []
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node:
                node_list.append(node)
                queue.append(node.left)
                queue.append(node.right)
        return node_list
