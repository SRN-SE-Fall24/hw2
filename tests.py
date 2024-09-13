import hw2_debugging


def test_with_sorted_array():
    arr = [10, 11, 12, 4, 7, 1, 3]
    sorted_arr = hw2_debugging.merge_sort(arr)

    assert sorted(arr) == sorted_arr
