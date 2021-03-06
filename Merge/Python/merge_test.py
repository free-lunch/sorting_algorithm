import unittest

from merge import merge_sort


class MergeUnittest(unittest.TestCase):
    @staticmethod
    def checkValid(items, reverse=False):
        n = len(items)
        for i in xrange(0, n-1):
            if not reverse and items[i] > items[i+1]:
                return False
            elif reverse and items[i] < items[i + 1]:
                return False
        return True

    def test_Sort(self):
        items = [1, 5, 4, 2, 8, 9, 10]
        result = merge_sort(items)

        self.assertEquals(True, self.checkValid(result))

    def test_ReverseSort(self):
        items = [1, 5, 4, 2, 8, 9, 10]
        result = merge_sort(items, reverse=True)
        self.assertEquals(True, self.checkValid(result, reverse=True))


if __name__ == "__main__":
    unittest.main()