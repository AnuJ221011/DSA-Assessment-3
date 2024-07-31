class Node:
    def __init__(self, value):
        self.value = value
        self.height = 0
        self.balance_factor = 0
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.nodes_count = 0
        self.root = None

    def find(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        elif target > node.value:
            return self._contains(node.right, target)
        else:
            return self._contains(node.left, target)

    def insert(self, value):
        if value is None:
            return False
        if self.find(value):
            return False
        else:
            self.root = self._insert(self.root, value)
            self.nodes_count += 1
            return True

    def _insert(self, node, target):
        if node is None:
            return Node(target)

        if target > node.value:
            node.right = self._insert(node.right, target)
        else:
            node.left = self._insert(node.left, target)

        self._update(node)
        return self._balance(node)

    def _update(self, node):
        left_height = -1 if node.left is None else node.left.height
        right_height = -1 if node.right is None else node.right.height

        node.height = 1 + max(left_height, right_height)
        node.balance_factor = right_height - left_height

    def _balance(self, node):
        if node.balance_factor == 2:
            if node.right.balance_factor >= 0:
                return self._right_right_case(node)
            else:
                return self._right_left_case(node)
        elif node.balance_factor == -2:
            if node.left.balance_factor <= 0:
                return self._left_left_case(node)
            else:
                return self._left_right_case(node)
        return node

    def _left_left_case(self, node):
        return self._rotate_right(node)

    def _left_right_case(self, node):
        node.left = self._rotate_left(node.left)
        return self._left_left_case(node)

    def _right_right_case(self, node):
        return self._rotate_left(node)

    def _right_left_case(self, node):
        node.right = self._rotate_right(node.right)
        return self._right_right_case(node)

    def _rotate_right(self, node):
        B = node.left
        node.left = B.right
        B.right = node

        self._update(node)
        self._update(B)
        return B

    def _rotate_left(self, node):
        B = node.right
        node.right = B.left
        B.left = node

        self._update(node)
        self._update(B)
        return B

    def remove(self, value):
        if value is None:
            return False
        if not self.find(value):
            return False
        else:
            self.root = self._remove(self.root, value)
            self.nodes_count -= 1
            return True

    def _remove(self, node, target):
        if node is None:
            return None

        if target == node.value:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.left
                while successor.right is not None:
                    successor = successor.right

                node.value = successor.value
                node.left = self._remove(node.left, successor.value)
        elif target > node.value:
            node.right = self._remove(node.right, target)
        else:
            node.left = self._remove(node.left, target)

        self._update(node)
        return self._balance(node)

    def size(self):
        return self.nodes_count

    def get_root(self):
        return self.root

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def __str__(self):
        values = []
        self._inorder(self.root, values)
        return ' '.join(map(str, values))

    def _inorder(self, node, values):
        if node is not None:
            self._inorder(node.left, values)
            values.append(node.value)
            self._inorder(node.right, values)

if __name__ == "__main__":
    tree = AVLTree()
    values = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18]
    for value in values:
        tree.insert(value)

    print("Size:", tree.size())
    print("Root:", tree.get_root().value)
    print("Inorder Traversal:")
    tree.inorder(tree.get_root())
    print()
