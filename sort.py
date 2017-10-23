def search_binary(seq, val):
    low = 0
    high = len(seq)
    mid = int((low + high) / 2)
    while low <= high:
        if seq[mid] > val:
            high = mid - 1
            mid = int((low + high) / 2)
        elif seq[mid] < val:
            low = mid + 1
            mid = int((low + high) / 2)
        else:
            return mid
    return -1


def sort_bubble(seq):
    n = len(seq)
    if n <= 1:
        return seq
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


def sort_selection(seq):
    n = len(seq)
    if n <= 1:
        return seq
    for i in range(n - 1):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                seq[i], seq[j] = seq[j], seq[i]
    return seq


def sort_insertion(seq):
    n = len(seq)
    if n <= 1:
        return seq
    for i in range(1, n):
        pos = i
        while pos >= 1:
            if seq[pos] < seq[pos - 1]:
                seq[pos], seq[pos - 1] = seq[pos - 1], seq[pos]
            pos -= 1
    return seq


def merge(seq1, seq2):
    res = []
    i, j = 0, 0
    while (i < len(seq1)) & (j < len(seq2)):
        if seq1[i] < seq2[j]:
            res.append(seq1[i])
            i += 1
        else:
            res.append(seq2[j])
            j += 1
    if i < len(seq1):
        res += seq1[i:]
    if j < len(seq2):
        res += seq2[j:]
    return res


def sort_merge(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    seq1 = sort_merge(seq[:mid])
    seq2 = sort_merge(seq[mid:])
    return merge(seq1, seq2)


def sort_quick(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[-1]
        left = sort_quick([x for x in seq[:-1] if x < pivot])
        right = sort_quick([x for x in seq[:-1] if x > pivot])
        return left + [pivot] + right


def heapify(seq, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n) and (seq[left] > seq[largest]):
        largest = left
    if (right < n) and (seq[right] > seq[largest]):
        largest = right
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        heapify(seq, n, largest)


def sort_heap(seq):
    n = len(seq)
    for i in range(n - 1, -1, -1):
        heapify(seq, n, i)
    for i in range(n - 1, 0, -1):
        seq[0], seq[i] = seq[i], seq[0]
        heapify(seq, i, 0)
    return seq


if __name__ == '__main__':
    # seq_sorted = [1, 3, 5, 7, 9]
    # print('binary search: ', search_binary(seq_sorted, 5))

    seq_unsorted = [1, 5, 4, 9, 2, 10]
    # print('bubble sort: ', sort_bubble(seq_unsorted))
    # print('selection sort: ', sort_selection(seq_unsorted))
    # print('insertion sort: ', sort_insertion(seq_unsorted))
    # print('merge sort: ', sort_merge(seq_unsorted))
    # print('quick sort: ', sort_quick(seq_unsorted))
    # sort_heap(seq_unsorted)
    print(sort_heap(seq_unsorted))
