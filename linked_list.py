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

