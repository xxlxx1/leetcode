"""
快排
https://leetcode-cn.com/problems/sort-an-array/
"""


def patition(nums, start, end):
    target = nums[start]
    while start < end:
        while start < end and nums[end] >= target:
            end -= 1
        nums[start] = nums[end]
        while start < end and nums[start] <= target:
            start += 1
        nums[end] = nums[start]
    nums[start] = target
    return start


def fast_sort(nums, start, end):
    if start < end:
        t = patition(nums, start, end)
        fast_sort(nums, start, t - 1)
        fast_sort(nums, t + 1, end)


nums = [-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,-87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,-6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,-69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,92,52,-45,-2,85,-63,56,55,12,-85,77,-39]
fast_sort(nums, 0, len(nums) - 1)
print(nums)