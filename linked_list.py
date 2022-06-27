import timeit
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


def bubble_sort(linked_list: LinkedList) -> None:
    """The function sorts a given linked list using Bubble sort method"""
    for j in range(len(linked_list) - 1):
        for i in range(len(linked_list) - 1 - j):
            if linked_list.find(i).value > linked_list.find(i + 1).value:
                linked_list.swap(i, i + 1)


def merge_lists(head1: Node, head2: Node) -> Optional['Node']:
    """The function combines two linked lists, while sorting the elements in ascending order"""
    if not head1:
        return head2
    if not head2:
        return head1
    temp_head = tail = Node(314159)
    while head1 and head2:
        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    tail.next = head1 or head2
    return temp_head.next


def list_separator(head: Node) -> tuple[Node, Node | None]:
    """The function takes head of linked list, and splits the list into two"""
    slow = head
    fast = head.next
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
    head1 = head
    head2 = slow.next
    slow.next = None
    return head1, head2


def merge_sort_step(head: Node) -> Node:
    """
    The function takes a head of a linked list and recursively calls the separator,
    dividing the list into sub-lists until only one element remains in each, then sorts them by merging.
    Will return a head of sorted list.
    """
    if not head or not head.next:
        return head
    a, b = list_separator(head)
    a = merge_sort_step(a)
    b = merge_sort_step(b)
    return merge_lists(a, b)


def merge_sort(linked_list: LinkedList) -> LinkedList:
    """The function initiates merge sorting algorithm"""
    linked_list.head = merge_sort_step(linked_list.head)
    return linked_list


def make_linked_list(data: list) -> LinkedList:
    """The function creates a linked list"""
    ll = LinkedList()
    for el in data:
        ll.append(el)
    return ll


def runtime_test(sort_method, data: list) -> None:
    arr_for_test = [make_linked_list(data) for i in range(1000000)]
    print(
        "Average {.__name__} execution time: {: f} sec.".format(
            sort_method, timeit.timeit(lambda: sort_method(arr_for_test.pop()), number=1000000) / 1000000
        )
    )


if __name__ == '__main__':
    elements = []
    with open('input.txt', "r") as f:
        for item in f.readlines():
            elements.append(int(item))

    runtime_test(bubble_sort, elements)
    runtime_test(merge_sort, elements)
