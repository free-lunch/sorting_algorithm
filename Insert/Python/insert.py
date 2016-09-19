def compare_item(i, j, reverse=False):
    if not reverse:
        return i < j
    else:
        return i > j


def insert_sort(items, reverse=False):
    for i in range(1, len(items)):
        current_value = items[i]
        index = i
        while index > 0 and compare_item(current_value, items[index - 1], reverse):
            items[index] = items[index - 1]
            index -= 1
        items[index] = current_value
