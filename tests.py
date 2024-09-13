import hw2_debugging


def test_with_sorted_array():
    arr = [10, 11, 12, 4, 7, 1, 3]
    sorted_arr = hw2_debugging.merge_sort(arr)

    assert sorted(arr) == sorted_arr


def test_reverse_sorted_array():
    arr = [10, 8, 6, 5, 3, 2, 1]
    sorted_arr = hw2_debugging.merge_sort(arr)

    assert sorted(arr) == sorted_arr


def test_array_with_duplicates():
    arr = [10, 8, 1, 2, 5, 3, 3, 10, 2, 1]
    sorted_arr = hw2_debugging.merge_sort(arr)

    assert sorted(arr) == sorted_arr
