"""
二分查找
https://leetcode-cn.com/problems/binary-search/
"""


def erfen(s, t):
    start, end = 0, len(s) - 1
    while end >= start:
        mid = (end + start) // 2
        if s[mid] == t:
            return mid
        elif s[mid] < t:
            start = mid + 1
        else:
            end = mid - 1
    return -1


s = [1, 2]
t = 2
result = erfen(s, t)
print(result, s[result])
