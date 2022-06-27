from typing import Optional


class Node:
    def __init__(self, value: int, next_node: Optional['Node'] = None) -> None:
        self.__value = value
        self.__next = next_node

    @property
    def value(self) -> int:
        return self.__value

    @property
    def next(self) -> Optional['Node']:
        return self.__next

    @next.setter
    def next(self, elem: Optional['Node']) -> None:
        self.__next = elem


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.nodes_counter = 0

    def __str__(self) -> str:
        return ' -> '.join([str(node) for node in self])

    def __iter__(self) -> int:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self.nodes_counter

    def append(self, value_to_append: int) -> None:
        """The function appends a new node at the end of the linked list"""
        new_node = Node(value_to_append)
        if not self.head:
            self.head = new_node
            self.nodes_counter += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.nodes_counter += 1

    def insert(self, prev_position, value_to_insert: int) -> None:
        """The function inserts a new node after the given position number in linked list"""
        current = self.find(prev_position)
        new_node = Node(value_to_insert)
        new_node.next = current.next
        current.next = new_node
        self.nodes_counter += 1

    def find(self, position: int) -> Node:
        """The function search a node by specified position number in the linked list"""
        if position > (len(self) - 1):
            raise ValueError('The specified position ({}) is out of the current linked list length'.format(position))
        current = self.head
        pointer = 0
        while current:
            if pointer == position:
                return current
            current = current.next
            pointer += 1

    def remove(self, position: int) -> None:
        """The function removes a node at the specified position of the linked list"""
        if not self.head:
            raise ValueError('The linked list is empty -> nothing to remove')
        if position == 0:
            self.head = self.head.next
            self.nodes_counter -= 1
            return
        current = self.find(position)
        prev = self.find(position - 1)
        current = current.next
        prev.next = current
        self.nodes_counter -= 1

    def swap(self, position1: int, position2: int) -> None:
        """The function swaps two nodes at the specified positions in the linked list"""
        node1 = self.find(position1)
        node2 = self.find(position2)
        prev_node1 = self.find(position1 - 1)
        prev_node2 = self.find(position2 - 1)
        if prev_node1:
            prev_node1.next = node2
        else:
            self.head = node2
        if prev_node2:
            prev_node2.next = node1
        else:
            self.head = node1
        current = node1.next
        node1.next = node2.next
        node2.next = current



