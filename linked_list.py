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


