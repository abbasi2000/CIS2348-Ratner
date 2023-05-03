# 2095022 # EMAD ABBASI
def selection_sort_descend_trace(lst):
    for i in range(len(lst) - 1):
        max_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
        print(' '.join(map(str, lst)), end=' ')
        print()


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    selection_sort_descend_trace(lst)