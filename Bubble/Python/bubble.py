def bubble_sort(items, reverse=False):
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if reverse and items[i] < items[j]:
                items[i], items[j] = items[j], items[i]
            elif not reverse and items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
