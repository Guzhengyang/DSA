class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self is None:
            return Node
        current = self
        res = []
        while current is not None:
            res.append(current.data)
            current = current.next
        return str(res)

def insert(node, data):
    node_new = Node(data, None)
    if node is None:
        return node_new
    current = node
    if current.next is not None:
        temp = current.next
        current.next = node_new
        node_new.next = temp
    else:
        current.next = node_new

def search(head, data):
    current = head
    while current is not None:
        if current.data == data:
            return True
        current = current.next
    return False


def delete(head, data):
    if head.data == data:
        return head.next
    prev = head
    current = head.next
    while current is not None:
        if current.data == data:
            temp = current.next
            prev.next = temp
            return head
        prev = current
        current = current.next
    return head

def reverse(head):
    current = head
    prev = None
    while current.next is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    current.next = prev
    return current


def reverse_pair(head):
    if head is None:
        return None
    if head.next is None:
        return head
    left = head
    right = head.next.next
    head = head.next
    left.next = right
    head.next = left
    head.next.next = reverse_pair(head.next.next)
    return head


if __name__ == '__main__':

    node4 = Node(8, None)
    node3 = Node(6, node4)
    node2 = Node(4, node3)
    node1 = Node(2, node2)
    head = Node(0, node1)
    print('head: ', head)
    insert(node3, 33)
    print('head after insertion: ', node3)

    print('search result: ', search(head, 7))
    print('delete result: ', delete(head, 6))
    # print('reversed: ', reverse(head))
    print('before reverse pair: ', head)
    print('pair reversed: ', reverse_pair(head))


