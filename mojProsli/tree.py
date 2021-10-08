class EmptyTreeException(Exception):
    pass


class TreeNode(object):

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def is_root(self):
        if self.parent is None:
            return True
        return False

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        return False

    def add_child(self, new_node):
        new_node.parent = self
        self.children.append(new_node)

    def __str__(self):
        return str(self.data)


class Tree(object):

    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def depth(self, new_node):
        if new_node.is_root():
            return 0
        else:
            return 1 + self.depth(new_node.parent)

    def _height(self, new_node):
        if new_node.is_leaf():
            return 0
        else:
            return 1 + max(self._height(i) for i in new_node.children)

    def height(self):
        return self._height(self.root)

    def preorder(self, new_node):
        if not self.is_empty():
            print(new_node.data)
            for i in new_node.children:
                self.preorder(i)

    def postorder(self, new_node):
        if not self.is_empty():
            for i in new_node.children:
                self.postorder(i)
            print(new_node.data)
