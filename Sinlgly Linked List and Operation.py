# Time Complexity of singly Linkedlist is
# space complexity of singly Linkedlist is O(n) as it increases linearly with each node

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next    # will store address of next node and on index +1 again store address of next node
                    index += 1
                nextNode = tempNode.next    # tempNode now has address of node next after specified location
                tempNode.next = newNode
                newNode.next = nextNode

    # Traversing in single linkedlist
    def traverse_single_liked_list(self):           # time complexity---------- O(n)
        if self.head is None:                       # ---------- O(1)
            print("Sll does not exist!")
        else:
            node = self.head                        # ---------- O(1)
            while node is not None:                 # ---------- O(n)
                print(node.value)
                node = node.next                    # ---------- O(1)

    # search in A SLL                         time Complexity  ---------- O(n)
    def searching_sll(self, NodeValue):
        if self.head is None:                   # ---------- O(1)
            return "Empty SLL"
        else:
            node = self.head                    # ----TC O(1) & Space Complexity = O(1) as creating a node only
            while node is not None:             # ---------- O(n)
                if node.value == NodeValue:     # ---------- O(1)
                    return node.value
                node = node.next                # ---------- O(1)
            return "NodeValue not in this list"

    def delete_in_sll(self, location):
        if self.head is None:
            print("LinkedLIst is Empty")
        else:
            node = self.head
            if location == 0:
                if self.head == self.tail:  # for condition where sll has one node only thus head & tail
                                            # has same address
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next    # as self.head has addr of first node

            elif location == 1:
                if self.head == self.tail:  # for condition where sll has one node only thus head & tail
                                            # has have same address
                    self.head = None
                    self.tail = None
                else:
                    # for traversing through the list
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:    # as self.tail has addr of last node
                            break
                        node = node.next
                        # below node is the second last node as while loop stopped just before last node
                        node.next = None
                        self.tail = node


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(44, 0)
singlyLinkedList.insertSLL(25, 1)
singlyLinkedList.insertSLL(100, 2)

#singlyLinkedList.traverse_single_liked_list()
print([node.value for node in singlyLinkedList])
print(singlyLinkedList.searching_sll(44))



