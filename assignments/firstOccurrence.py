"""Q6. First occurrence in a sorted array (100 pts).

Given a sorted array of integers (possibly with duplicates), return the index
of the first occurrence of the target, or -1 if it is absent.

Input: n and target on the first line; n sorted integers on the second line.

Sample input:
6 2
1 2 2 2 3 4

Sample output:
1

Consider binary search. Brute force may exceed the time limit.
Time limit: 0.05 s per input file. Memory: 256 MB. Python 3.
"""


def first_occurrence(arr, target):
    # insert your codes
    pass


n, target = map(int, input().split())
arr = list(map(int, input().split()))
result = first_occurrence(arr, target)
print(result)
