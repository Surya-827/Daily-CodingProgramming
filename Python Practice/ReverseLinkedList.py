
class Node(object):
    def __init__(self,data):
        self.head = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


if __name__ == "__main__":
    lk1 = LinkedList()
    lk1.head = Node(1)
    lk1.head.next = Node(2)
    lk1.head.next.next = Node(3)
    lk1.reverse()