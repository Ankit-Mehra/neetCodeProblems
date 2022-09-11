"""Binary search tree data structure implementation
Author : Ankit Mehra
Date : 22 August 2022
"""


from operator import contains


class BinarySearchTree:
    """Binary search tree data structure implementation"""

    class Node:
        """Node Class as primary unit in the BST"""

        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None

        def __repr__(self) -> str:
            return str(self.value)

    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        """Insert a value in binary Tree"""
        new_node = self.Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node


def main():
    bs_tree = BinarySearchTree()
    bs_tree.insert(9)
    bs_tree.insert(1)
    bs_tree.insert(3)
    bs_tree.insert(5)
    bs_tree.insert(10)
    bs_tree.insert(18)
    bs_tree.insert(11)

    print(bs_tree.root.value)
    print(bs_tree.root.right.value)
    print(bs_tree.root.left.value)
    print(bs_tree.contains(11))
    print(bs_tree.min_value_node(bs_tree.root))
    print(bs_tree.max_value_node(bs_tree.root))


if __name__ == "__main__":
    main()
