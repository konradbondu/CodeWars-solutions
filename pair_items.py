# Task
# Write a function with the following properties:
#
# takes two lists
# returns a list of all ways to pair the items of both objects, maintaining the order of the items
# output format is a list of lists of tuples, or a list of empty lists, if no pairs are possible
# inner lists can be of any order (see 2nd and 7th test)
# Example 1
# Pair elements of the following two lists:
#
# ['electric', 'horse', 'fly']
# ['1st', '2nd']
# Valid result:
#
# [[('electric', '1st'), ('horse', '2nd')],
#  [('electric', '1st'), ('fly', '2nd')],
#  [('horse', '1st'), ('fly', '2nd')]]
# Example 2
# Pair elements of ['a', 'b', 'c'] with elements of ['x', 'y']
#
# Valid Result:
#
# [[('a', 'x'), ('b', 'y')],
#  [('a', 'x'), ('c', 'y')],
#  [('b', 'x'), ('c', 'y')]]
# Example 3
# Pair elements of [1, 2] with elements of [6, 7, 8, 9]
#
# Valid Result:
#
# [[(1, 6), (2, 7)],
#  [(1, 6), (2, 8)],
#  [(1, 6), (2, 9)],
#  [(1, 7), (2, 8)],
#  [(1, 7), (2, 9)],
#  [(1, 8), (2, 9)]]


from itertools import combinations


def pair_items(list1, list2):
    n = min(len(list1), len(list2))
    return [list(zip(x, y)) for x in combinations(list1, n) for y in combinations(list2, n)]
