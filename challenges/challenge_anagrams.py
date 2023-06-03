def is_anagram(f_string, s_string):
    if f_string == '' and s_string == '':
        return ('', '', False)
    first_list, second_list = list(f_string.lower()), list(s_string.lower())
    merge_sort(first_list)
    merge_sort(second_list)
    ordered_f_string = ''.join(first_list)
    ordered_s_string = ''. join(second_list)
    partial_result = [ordered_f_string, ordered_s_string]
    if first_list == second_list:
        return (*partial_result, True)
    return (*partial_result, False)


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
