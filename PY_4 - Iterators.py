# 1
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.len_ = len(self.list_of_list)
        self.outer_list_cursor = -1

    def __iter__(self):
        self.outer_list_cursor += 1 
        self.inner_list_cursor = 0  
        return self

    def __next__(self):
        if self.inner_list_cursor == len(self.list_of_list[self.outer_list_cursor]):
            iter(self)
        if self.outer_list_cursor == self.len_:
            raise StopIteration
        self.inner_list_cursor += 1
        return self.list_of_list[self.outer_list_cursor][self.inner_list_cursor-1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    new_hw = FlatIterator([['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], ])
    
    for x in new_hw:
        print(x)
    test_1()

# 2
import types
from collections.abc import Iterable


def flat_generator(list_of_lists, ignore_types=(str, bytes)):
    for x in list_of_lists:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from x
        else:
            yield

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for x in flat_generator(list_of_lists):
        print(x)
