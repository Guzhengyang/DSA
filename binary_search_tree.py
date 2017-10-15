class BST:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder(subtree):
    res = []
    stack = []
    stack.append(subtree)
    while True:
        current = stack.pop()
        res.append(current.data)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
        if len(stack) == 0:
            break
    return res


def inorder(subtree):
    res = []
    stack = []
    current = subtree
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                res.append(current.data)
                current = current.right
            else:
                break
    return res


def breadth(subtree):
    res = []
    queue = []
    queue.append(subtree)
    while True:
        count = len(queue)
        if count == 0:
            break
        res_level = []
        while count > 0:
            current = queue.pop(0)
            res_level.append(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            count -= 1
        print(res_level)
        res.append(res_level)
    return res


def postorder(subtree):
    if subtree is not None:
        postorder(subtree.left)
        postorder(subtree.right)
        print(subtree.data)


def search(root, data):
    if root is None:
        return None
    if root.data < data:
        return search(root.right, data)
    elif root.data > data:
        return search(root.left, data)
    else:
        return root


def insert(root, data):
    new = BST(data)
    if root is None:
        root = new
    else:
        if root.data > data:
            if root.left is None:
                root.left = new
            else:
                insert(root.left, data)
        if root.data < data:
            if root.right is None:
                root.right = new
            else:
                insert(root.right, data)


def min_node(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current


def succeed(root, node):
    if node is None:
        return None
    if node.right is not None:
        return min_node(node.right)
    current = root
    while current is not None:
        if current.data > node.data:
            successor = current
            current = current.left
        elif current.data < node.data:
            current = current.right
        else:
            break
    return successor

def delete(root, data):
    if root is None:
        return None
    if root.data > data:
        root.left = delete(root.left, data)
    elif root.data < data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = min_node(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root


if __name__ == '__main__':
    root = BST(4)
    insert(root, 7)
    insert(root, 3)
    insert(root, 1)
    insert(root, 2)
    insert(root, 6)
    insert(root, 5)
    insert(root, 8)
    print('breadth: ', breadth(root))
    print('preorder: ', preorder(root))
    print('inorder: ', inorder(root))
    postorder(root)
    print('search result', search(root, 6))

    successor = succeed(root, root)
    print('successor: ', inorder(successor))

    print('breadth: ', breadth(root))
    print('breadth after delete: ', breadth(delete(root, 7)))


