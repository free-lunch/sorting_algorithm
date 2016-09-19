def compare_item(i, j, reverse=False):
    if not reverse:
        return i < j
    else:
        return i > j


def selection_sort(items, reverse=False):
    for i in range(len(items)):
        min_index = i
        for j in range(i, len(items)):
            if compare_item(items[j], items[min_index], reverse):
                min_index = j
        items[min_index], items[i] = items[i], items[min_index]