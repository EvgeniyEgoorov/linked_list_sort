import unittest
from linked_list import LinkedList, bubble_sort, merge_sort


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.ll = LinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

    def test_append(self):
        self.ll.append(4)
        self.assertEqual(list(self.ll), [1, 2, 3, 4])

    def test_insert(self):
        self.ll.insert(1, 4)
        self.assertEqual(list(self.ll), [1, 2, 4, 3])

    def test_insert_after_nonexistent_value(self):
        with self.assertRaises(ValueError):
            self.ll.insert(100000, 5)

    def test_find(self):
        self.assertEqual(self.ll.find(2).value, 3)

    def test_find_from_empty_list(self):
        empty_list = LinkedList()
        with self.assertRaises(ValueError):
            empty_list.find(2)

    def test_find_nonexistent_value(self):
        with self.assertRaises(ValueError):
            self.ll.find(100000)

    def test_remove(self):
        self.ll.remove(2)
        self.assertEqual(list(self.ll), [1, 2])

    def test_remove_head_value(self):
        self.ll.remove(0)
        self.assertEqual(list(self.ll), [2, 3])

    def test_remove_from_empty_list(self):
        empty_list = LinkedList()
        with self.assertRaises(ValueError):
            empty_list.remove(2)

    def test_remove_nonexistent_value(self):
        with self.assertRaises(ValueError):
            self.ll.remove(100000)

    def test_swap(self):
        self.ll.swap(0, 2)
        self.assertEqual(list(self.ll), [3, 2, 1])

    def test_swap_nonexistent_value(self):
        with self.assertRaises(ValueError):
            self.ll.swap(1, 100000)


if __name__ == '__main__':
    unittest.main()
