"""Q7. Find the smallest number greater than the target.

Given a sorted list of integers with no duplicates, return the smallest number
in the list greater than the target, or -1 if no such number exists.

Input: n and x on the first line; n sorted integers on the second line.

Sample input:
5 9
1 2 3 4 5

Sample output:
-1

Consider binary search. Brute force may exceed the time limit.
Time limit: 0.05 s per input file. Memory: 256 MB. Python 3.
"""


def find_smallest_greater(arr, x):
    # insert your codes here
    pass


# read input
n, x = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(find_smallest_greater(arr, x))
