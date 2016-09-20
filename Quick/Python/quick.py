def compare_item(i, j, reverse=False):
    if not reverse:
        return i < j
    else:
        return i > j


def quick_sort(items, reverse=False):
    if not items:
        return []

    pivot = [x for x in items if x == items[0]]
    left = quick_sort([x for x in items if compare_item(x, items[0], reverse)], reverse)
    right = quick_sort([x for x in items if compare_item(items[0], x, reverse)], reverse)

    # print reverse, items,left, pivot, right
    return left + pivot + right
