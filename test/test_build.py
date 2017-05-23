from unittest import TestCase
from linked_list import LinkedList, Node


class TestBuild(TestCase):
    def test_check_whether_the_values_are_there(self):
        try:
            from build import is_palindrome
        except ImportError:
            self.assertFalse("no function found")

        linked_list = LinkedList()
        self.assertEqual(is_palindrome(linked_list), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = LinkedList(head)
        self.assertEqual(is_palindrome(linked_list), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        self.assertEqual(is_palindrome(linked_list), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = LinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        self.assertEqual(is_palindrome(linked_list), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = LinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        self.assertEqual(is_palindrome(linked_list), True)
