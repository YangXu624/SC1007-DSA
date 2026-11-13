"""Q8. The k-th smallest number in a sorted matrix.

Given an n x n matrix with each row and each column sorted in non-decreasing
order, return the k-th smallest element. Duplicates count separately.

Input: n and k on the first line, followed by n rows of n integers each.

Sample input:
3 5
1 5 9
10 11 13
12 13 15

Sample output:
11

In this matrix, the 7th and 8th smallest elements are both 13.
Time limit: 0.05 s per input file. Memory: 256 MB. Python 3.

The question text uses kth_smallest_linear, but the supplied code calls
kth_smallest. This template keeps the supplied function and call consistent.
"""


def kth_smallest(matrix, k):
    # insert your codes here
    pass


# read the input
n, k = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# output
print(kth_smallest(matrix, k))
