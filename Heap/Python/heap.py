def compare_item(i, j, reverse=False):
    if not reverse:
        return i < j
    else:
        return i > j


def heap_sort(items, reverse=False):
    heapify(items, reverse)

    index = len(items)-1
    while index > 0:
        items[index], items[0] = items[0], items[index]
        index -= 1
        shift_down(items, 0, index, reverse)


def heapify(items, reverse):
    for start in range((len(items)-2)//2, -1, -1):
        shift_down(items, start, len(items)-1, reverse)
        print items


def shift_down(items, start, end, reverse):
    root = start
    while True:
        child = root*2+1
        if child > end:
            break

        if child+1 <= end and compare_item(items[child], items[child+1], reverse):
            child += 1

        if compare_item(items[root], items[child], reverse):
            items[root], items[child] = items[child], items[root]
            root = child
        else:
            break

