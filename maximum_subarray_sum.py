# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or
# list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) # should be 6: [4, -1, 2, 1] Easy case is when the list is made up of
# only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative
# numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid
# sublist/subarray.


def max_sequence(arr):
    if len(arr) == 0:
        return 0
    result = 0
    j = 1
    while j <= len(arr):
        for i in range(0, len(arr) - j + 1):
            sum_sub_arr = sum(arr[i:i+j])
            if sum_sub_arr > result:
                result = sum_sub_arr
        j += 1
    return result
