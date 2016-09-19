def compare_item(i, j, reverse=False):
    if not reverse:
        return i < j
    else:
        return i > j


def merge_sort(items, reverse=False):
    if len(items) < 2:
        return items

    n = len(items) // 2
    head_result = merge_sort(items[:n], reverse)
    tail_result = merge_sort(items[n:], reverse)

    index_head = 0
    index_tail = 0
    ret = []
    while True:
        if compare_item(head_result[index_head], tail_result[index_tail], reverse):
            ret.append(head_result[index_head])
            index_head += 1
        else:
            ret.append(tail_result[index_tail])
            index_tail += 1

        if index_head == len(head_result):
            ret += tail_result[index_tail:]
            break

        if index_tail == len(tail_result):
            ret += head_result[index_head:]
            break

    return ret
